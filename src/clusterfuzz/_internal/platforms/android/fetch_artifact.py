# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Fetch a build artifact (ported from google3 with
minor modifications, especially without any google3 specific library
dependencies)."""

import io
import json
import os
import re

import apiclient
from oauth2client.service_account import ServiceAccountCredentials

from clusterfuzz._internal.config import db_config
from clusterfuzz._internal.google_cloud_utils import storage
from clusterfuzz._internal.metrics import logs
from clusterfuzz._internal.system import environment

from . import adb

# 20 MB default chunk size.
DEFAULT_CHUNK_SIZE = 20 * 1024 * 1024

# Maximum number of retries for artifact access.
MAX_RETRIES = 5

STABLE_CUTTLEFISH_BUILD = {
    'bid': '11655237',
    'branch': 'git_main',
    'target': 'cf_x86_64_phone-next-userdebug'
}

DEFAULT_STABLE_CUTTLEFISH_BUILD_INFO = (
    "gs://android-haiku/target-cuttlefish/stable_build_info.json")


def execute_request_with_retries(request):
  """Executes request and retries on failure."""
  result = None
  for _ in range(MAX_RETRIES):
    try:
      result = request.execute()
      break
    except Exception as e:
      logs.log_error(f'Error calling endpoint {request.uri}: Error {e}')

  return result


def download_artifact(client, bid, target, attempt_id, name, output_directory,
                      output_filename):
  """Download one artifact."""
  logs.log('reached download_artifact')
  logs.log('artifact to download: %s' % name)
  logs.log('output_directory: %s' % output_directory)
  logs.log('output_filename: %s' % output_filename)
  artifact_query = client.buildartifact().get(
      buildId=bid, target=target, attemptId=attempt_id, resourceId=name)
  artifact = execute_request_with_retries(artifact_query)
  if artifact is None:
    logs.log_error(
        'Artifact unreachable with name %s, target %s and build id %s.' %
        (name, target, bid))
    return None

  # Lucky us, we always have the size.
  size = int(artifact['size'])

  chunksize = -1
  if size >= DEFAULT_CHUNK_SIZE:
    chunksize = DEFAULT_CHUNK_SIZE

  # Just like get, except get_media.
  dl_request = client.buildartifact().get_media(
      buildId=bid, target=target, attemptId=attempt_id, resourceId=name)

  if output_filename:
    file_name = output_filename
  else:
    file_name = name.replace('signed/', '')

  output_path = os.path.join(output_directory, file_name)
  # If the artifact already exists, then bail out.
  if os.path.exists(output_path) and os.path.getsize(output_path) == size:
    logs.log('Artifact %s already exists, skipping download.' % name)
    return output_path

  logs.log('Downloading artifact %s.' % name)
  output_dir = os.path.dirname(output_path)
  logs.log('Output dir: %s' % output_dir)
  if not os.path.exists(output_dir):
    logs.log(f'Creating directory {output_dir}')
    os.mkdir(output_dir)

  with io.FileIO(output_path, mode='wb') as file_handle:
    downloader = apiclient.http.MediaIoBaseDownload(
        file_handle, dl_request, chunksize=chunksize)
    done = False

    while not done:
      status, done = downloader.next_chunk()
      if status:
        size_completed = int(status.resumable_progress)
        percent_completed = (size_completed * 100.0) / size
        logs.log('%.1f%% complete.' % percent_completed)

  return output_path


def get_artifacts_for_build(client, bid, target, attempt_id='latest'):
  """Return list of artifacts for a given build."""
  request = client.buildartifact().list(
      buildId=bid, target=target, attemptId=attempt_id)

  request_str = (f'{request.uri}, {request.method}, '
                 f'{request.body}, {request.methodId}')

  artifacts = []
  results = []
  while request:
    result = execute_request_with_retries(request)
    if not result:
      break
    results.append(result)
    if result and 'artifacts' in result:
      for artifact in result['artifacts']:
        artifacts.append(artifact)
    request = client.buildartifact().list_next(request, result)

  if not artifacts:
    logs.log_error(f'No artifact found for target {target}, build id {bid}.\n'
                   f'request {request_str}, results {results}')
    adb.bad_state_reached()

  return artifacts


def get_client():
  """Return client with connection to build apiary."""
  # Connect using build apiary service account credentials.
  build_apiary_service_account_private_key = db_config.get_value(
      'build_apiary_service_account_private_key')
  if not build_apiary_service_account_private_key:
    logs.log(
        'Android build apiary credentials are not set, skip artifact fetch.')
    return None

  credentials = ServiceAccountCredentials.from_json_keyfile_dict(
      json.loads(build_apiary_service_account_private_key),
      scopes='https://www.googleapis.com/auth/androidbuild.internal')
  client = apiclient.discovery.build(
      'androidbuildinternal',
      'v3',
      credentials=credentials,
      static_discovery=False)

  return client


def get_stable_build_info():
  """Return stable artifact for cuttlefish branch and target."""
  logs.log('Reached get_stable_build_info')
  stable_build_info = STABLE_CUTTLEFISH_BUILD

  try:
    build_info_data = storage.read_data(DEFAULT_STABLE_CUTTLEFISH_BUILD_INFO)
    if build_info_data:
      logs.log('Loading stable cuttlefish image from %s' %
               DEFAULT_STABLE_CUTTLEFISH_BUILD_INFO)
      stable_build_info = json.loads(build_info_data)
  except Exception as e:
    logs.log_error(
        'Error loading remote data: %s!\nUsing default build info!' % e)

  logs.log('Using stable cuttlefish image - %s' % stable_build_info)
  return stable_build_info


def get_latest_artifact_info(branch, target, signed=False):
  """Return latest artifact for a branch and target."""
  client = get_client()
  if not client:
    return None

  # TODO(https://github.com/google/clusterfuzz/issues/3950)
  # After stabilizing the Cuttlefish image, revert this
  if environment.is_android_cuttlefish():
    return get_stable_build_info()

  request = client.build().list(  # pylint: disable=no-member
      buildType='submitted',
      branch=branch,
      target=target,
      successful=True,
      maxResults=1,
      signed=signed)
  request_str = (f'{request.uri}, {request.method}, '
                 f'{request.body}, {request.methodId}')

  builds = execute_request_with_retries(request)
  if not builds:
    logs.log_error(f'No build found for target {target}, branch {branch}, '
                   f'request: {request_str}.')
    return None

  build = builds['builds'][0]
  bid = build['buildId']
  target = build['target']['name']
  return {'bid': bid, 'branch': branch, 'target': target}


def get(bid, target, regex, output_directory, output_filename=None):
  """Return artifact for a given build id, target and file regex."""
  client = get_client()
  if not client:
    return None

  # Run the script to fetch the artifact.
  return run_script(
      client=client,
      bid=bid,
      target=target,
      regex=regex,
      output_directory=output_directory,
      output_filename=output_filename)


def run_script(client, bid, target, regex, output_directory, output_filename):
  """Download artifacts as specified."""
  artifacts = get_artifacts_for_build(
      client=client, bid=bid, target=target, attempt_id='latest')
  if not artifacts:
    logs.log_error('Artifact could not be fetched for target %s, build id %s.' %
                   (target, bid))
    return None

  regex = re.compile(regex)
  result = []

  for artifact in artifacts:
    artifact_name = artifact['name']

    # Exclude signature files.
    if artifact_name.endswith('.SIGN_INFO'):
      continue

    if regex.match(artifact_name):
      loop_result = download_artifact(
          client=client,
          bid=bid,
          target=target,
          attempt_id='latest',
          name=artifact_name,
          output_directory=output_directory,
          output_filename=output_filename)

      if loop_result is not None:
        result.append(loop_result)

  return result
