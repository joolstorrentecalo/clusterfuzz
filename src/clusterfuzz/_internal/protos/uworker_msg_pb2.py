# Copyright 2023 Google LLC
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

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clusterfuzz/_internal/protos/uworker_msg.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.clusterfuzz/_internal/protos/uworker_msg.proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf9\x02\n\nSetupInput\x12)\n\x06\x66uzzer\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x88\x01\x01\x12\x18\n\x0b\x66uzzer_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\"\n\x15\x66uzzer_log_upload_url\x18\x04 \x01(\tH\x02\x88\x01\x01\x12 \n\x13\x66uzzer_download_url\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\"\n\x15testcase_download_url\x18\x06 \x01(\tH\x04\x88\x01\x01\x12$\n\x1cglobal_blacklisted_functions\x18\x07 \x03(\t\x12/\n\x14\x64\x61ta_bundle_corpuses\x18\x08 \x03(\x0b\x32\x11.DataBundleCorpusB\t\n\x07_fuzzerB\x0e\n\x0c_fuzzer_nameB\x18\n\x16_fuzzer_log_upload_urlB\x16\n\x14_fuzzer_download_urlB\x18\n\x16_testcase_download_url\")\n\x10\x41nalyzeTaskInput\x12\x15\n\rbad_revisions\x18\x01 \x03(\x03\"P\n\x12SymbolizeTaskInput\x12!\n\x14old_crash_stacktrace\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x17\n\x15_old_crash_stacktrace\"C\n\rBlobUploadUrl\x12\x10\n\x03key\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03url\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x06\n\x04_keyB\x06\n\x04_url\"\xa1\x03\n\rFuzzTaskInput\x12\'\n\x1asample_testcase_upload_key\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\'\n\x1asample_testcase_upload_url\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\"\n\x15script_log_upload_url\x18\x03 \x01(\tH\x02\x88\x01\x01\x12.\n\x0b\x66uzz_target\x18\x04 \x01(\x0b\x32\x14.google.protobuf.AnyH\x03\x88\x01\x01\x12&\n\x06\x63orpus\x18\x05 \x01(\x0b\x32\x11.FuzzTargetCorpusH\x04\x88\x01\x01\x12$\n\x1cglobal_blacklisted_functions\x18\x06 \x03(\t\x12)\n\x11\x63rash_upload_urls\x18\x07 \x03(\x0b\x32\x0e.BlobUploadUrlB\x1d\n\x1b_sample_testcase_upload_keyB\x1d\n\x1b_sample_testcase_upload_urlB\x18\n\x16_script_log_upload_urlB\x0e\n\x0c_fuzz_targetB\t\n\x07_corpus\"\x89\x01\n\x10\x44\x61taBundleCorpus\x12.\n\x0b\x64\x61ta_bundle\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x88\x01\x01\x12\x14\n\x07gcs_url\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x0b\x63orpus_urls\x18\x03 \x03(\tB\x0e\n\x0c_data_bundleB\n\n\x08_gcs_url\"|\n\x10\x46uzzTargetCorpus\x12\x1c\n\x06\x63orpus\x18\x01 \x01(\x0b\x32\x07.CorpusH\x00\x88\x01\x01\x12(\n\x12regressions_corpus\x18\x02 \x01(\x0b\x32\x07.CorpusH\x01\x88\x01\x01\x42\t\n\x07_corpusB\x15\n\x13_regressions_corpus\"\xf2\x01\n\x06\x43orpus\x12,\n\x0b\x63orpus_urls\x18\x01 \x03(\x0b\x32\x17.Corpus.CorpusUrlsEntry\x12:\n\x11last_updated_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x12\x14\n\x07gcs_url\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x0bupload_urls\x18\x04 \x03(\t\x1a\x31\n\x0f\x43orpusUrlsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x14\n\x12_last_updated_timeB\n\n\x08_gcs_url\"\x92\x02\n\x11MinimizeTaskInput\x12 \n\x13testcase_upload_url\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1f\n\x12testcase_blob_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12!\n\x14stacktrace_blob_name\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\"\n\x15stacktrace_upload_url\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x11\n\targuments\x18\x05 \x03(\tB\x16\n\x14_testcase_upload_urlB\x15\n\x13_testcase_blob_nameB\x17\n\x15_stacktrace_blob_nameB\x18\n\x16_stacktrace_upload_url\",\n\x13RegressionTaskInput\x12\x15\n\rbad_revisions\x18\x01 \x03(\x03\"\x81\x02\n\x14ProgressionTaskInput\x12\x1a\n\rcustom_binary\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x15\n\rbad_revisions\x18\x02 \x03(\x03\x12$\n\x17regression_testcase_url\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tblob_name\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\"\n\x15stacktrace_upload_url\x18\x05 \x01(\tH\x03\x88\x01\x01\x42\x10\n\x0e_custom_binaryB\x1a\n\x18_regression_testcase_urlB\x0c\n\n_blob_nameB\x18\n\x16_stacktrace_upload_url\"\xcb\x01\n\x19\x43rossPollinateFuzzerProto\x12.\n\x0b\x66uzz_target\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x88\x01\x01\x12\x1f\n\x12\x62\x61\x63kup_bucket_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1f\n\x12\x63orpus_engine_name\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x0e\n\x0c_fuzz_targetB\x15\n\x13_backup_bucket_nameB\x15\n\x13_corpus_engine_name\"\x95\x05\n\x16\x43orpusPruningTaskInput\x12.\n\x0b\x66uzz_target\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x88\x01\x01\x12\"\n\x15last_execution_failed\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12;\n\x17\x63ross_pollinate_fuzzers\x18\x03 \x03(\x0b\x32\x1a.CrossPollinateFuzzerProto\x12&\n\x06\x63orpus\x18\x04 \x01(\x0b\x32\x11.FuzzTargetCorpusH\x02\x88\x01\x01\x12\x31\n\x11quarantine_corpus\x18\x05 \x01(\x0b\x32\x11.FuzzTargetCorpusH\x03\x88\x01\x01\x12%\n\x18\x63orpus_crashes_blob_name\x18\x06 \x01(\tH\x04\x88\x01\x01\x12&\n\x19\x63orpus_crashes_upload_url\x18\x07 \x01(\tH\x05\x88\x01\x01\x12!\n\x14\x64\x61ted_backup_gcs_url\x18\x08 \x01(\tH\x06\x88\x01\x01\x12\"\n\x15latest_backup_gcs_url\x18\t \x01(\tH\x07\x88\x01\x01\x12$\n\x17\x64\x61ted_backup_signed_url\x18\n \x01(\tH\x08\x88\x01\x01\x42\x0e\n\x0c_fuzz_targetB\x18\n\x16_last_execution_failedB\t\n\x07_corpusB\x14\n\x12_quarantine_corpusB\x1b\n\x19_corpus_crashes_blob_nameB\x1c\n\x1a_corpus_crashes_upload_urlB\x17\n\x15_dated_backup_gcs_urlB\x18\n\x16_latest_backup_gcs_urlB\x1a\n\x18_dated_backup_signed_url\"\xdb\n\n\x05Input\x12+\n\x08testcase\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x88\x01\x01\x12;\n\x18testcase_upload_metadata\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x01\x88\x01\x01\x12\x18\n\x0btestcase_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x12+\n\x0buworker_env\x18\x04 \x03(\x0b\x32\x16.Input.UworkerEnvEntry\x12\x15\n\x08job_type\x18\x06 \x01(\tH\x03\x88\x01\x01\x12&\n\x19uworker_output_upload_url\x18\x07 \x01(\tH\x04\x88\x01\x01\x12\x32\n\x12variant_task_input\x18\x08 \x01(\x0b\x32\x11.VariantTaskInputH\x05\x88\x01\x01\x12\x18\n\x0b\x66uzzer_name\x18\t \x01(\tH\x06\x88\x01\x01\x12%\n\x0bsetup_input\x18\n \x01(\x0b\x32\x0b.SetupInputH\x07\x88\x01\x01\x12\x32\n\x12\x61nalyze_task_input\x18\x0b \x01(\x0b\x32\x11.AnalyzeTaskInputH\x08\x88\x01\x01\x12?\n\x19\x63orpus_pruning_task_input\x18\x0c \x01(\x0b\x32\x17.CorpusPruningTaskInputH\t\x88\x01\x01\x12,\n\x0f\x66uzz_task_input\x18\r \x01(\x0b\x32\x0e.FuzzTaskInputH\n\x88\x01\x01\x12\x34\n\x13minimize_task_input\x18\x0e \x01(\x0b\x32\x12.MinimizeTaskInputH\x0b\x88\x01\x01\x12:\n\x16progression_task_input\x18\x0f \x01(\x0b\x32\x15.ProgressionTaskInputH\x0c\x88\x01\x01\x12\x38\n\x15regression_task_input\x18\x10 \x01(\x0b\x32\x14.RegressionTaskInputH\r\x88\x01\x01\x12\x36\n\x14symbolize_task_input\x18\x11 \x01(\x0b\x32\x13.SymbolizeTaskInputH\x0e\x88\x01\x01\x12\x18\n\x0bmodule_name\x18\x12 \x01(\tH\x0f\x88\x01\x01\x12>\n\x15preprocess_start_time\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x10\x88\x01\x01\x12$\n\x1cglobal_blacklisted_functions\x18\x14 \x03(\t\x12.\n\x0b\x66uzz_target\x18\x15 \x01(\x0b\x32\x14.google.protobuf.AnyH\x11\x88\x01\x01\x1a\x31\n\x0fUworkerEnvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0b\n\t_testcaseB\x1b\n\x19_testcase_upload_metadataB\x0e\n\x0c_testcase_idB\x0b\n\t_job_typeB\x1c\n\x1a_uworker_output_upload_urlB\x15\n\x13_variant_task_inputB\x0e\n\x0c_fuzzer_nameB\x0e\n\x0c_setup_inputB\x15\n\x13_analyze_task_inputB\x1c\n\x1a_corpus_pruning_task_inputB\x12\n\x10_fuzz_task_inputB\x16\n\x14_minimize_task_inputB\x19\n\x17_progression_task_inputB\x18\n\x16_regression_task_inputB\x17\n\x15_symbolize_task_inputB\x0e\n\x0c_module_nameB\x18\n\x16_preprocess_start_timeB\x0e\n\x0c_fuzz_target\"H\n\x10VariantTaskInput\x12\x1e\n\x11original_job_type\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x14\n\x12_original_job_type\"\xc7\x02\n\x13SymbolizeTaskOutput\x12\x17\n\ncrash_type\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rcrash_address\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0b\x63rash_state\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1d\n\x10\x63rash_stacktrace\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x17\n\nsymbolized\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x1b\n\x0e\x63rash_revision\x18\x06 \x01(\x03H\x05\x88\x01\x01\x12\x16\n\tbuild_url\x18\x07 \x01(\tH\x06\x88\x01\x01\x42\r\n\x0b_crash_typeB\x10\n\x0e_crash_addressB\x0e\n\x0c_crash_stateB\x13\n\x11_crash_stacktraceB\r\n\x0b_symbolizedB\x11\n\x0f_crash_revisionB\x0c\n\n_build_url\"\x93\x06\n\x11\x41nalyzeTaskOutput\x12\x1b\n\x0e\x63rash_revision\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x1a\n\rabsolute_path\x18\x02 \x01(\tH\x01\x88\x01\x01\x12 \n\x13minimized_arguments\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1d\n\x10\x63rash_stacktrace\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1b\n\x0e\x63rash_info_set\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x16\n\thttp_flag\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12\x17\n\ncrash_type\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x1a\n\rcrash_address\x18\x08 \x01(\tH\x07\x88\x01\x01\x12\x18\n\x0b\x63rash_state\x18\t \x01(\tH\x08\x88\x01\x01\x12\x1a\n\rsecurity_flag\x18\n \x01(\x08H\t\x88\x01\x01\x12\x1e\n\x11security_severity\x18\x0b \x01(\x05H\n\x88\x01\x01\x12\"\n\x15one_time_crasher_flag\x18\x0c \x01(\x08H\x0b\x88\x01\x01\x12\x16\n\tbuild_key\x18\r \x01(\tH\x0c\x88\x01\x01\x12\x16\n\tbuild_url\x18\x0e \x01(\tH\r\x88\x01\x01\x12\x14\n\x07gn_args\x18\x0f \x01(\tH\x0e\x88\x01\x01\x12\x15\n\x08platform\x18\x10 \x01(\tH\x0f\x88\x01\x01\x12\x18\n\x0bplatform_id\x18\x11 \x01(\tH\x10\x88\x01\x01\x42\x11\n\x0f_crash_revisionB\x10\n\x0e_absolute_pathB\x16\n\x14_minimized_argumentsB\x13\n\x11_crash_stacktraceB\x11\n\x0f_crash_info_setB\x0c\n\n_http_flagB\r\n\x0b_crash_typeB\x10\n\x0e_crash_addressB\x0e\n\x0c_crash_stateB\x10\n\x0e_security_flagB\x14\n\x12_security_severityB\x18\n\x16_one_time_crasher_flagB\x0c\n\n_build_keyB\x0c\n\n_build_urlB\n\n\x08_gn_argsB\x0b\n\t_platformB\x0e\n\x0c_platform_id\"\xd1\x02\n\tCrashInfo\x12\x13\n\x06is_new\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x12\n\x05\x63ount\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x17\n\ncrash_type\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x0b\x63rash_state\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1a\n\rsecurity_flag\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x16\n\tunit_name\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x1a\n\rcrash_address\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x1d\n\x10\x63rash_stacktrace\x18\x08 \x01(\tH\x07\x88\x01\x01\x42\t\n\x07_is_newB\x08\n\x06_countB\r\n\x0b_crash_typeB\x0e\n\x0c_crash_stateB\x10\n\x0e_security_flagB\x0c\n\n_unit_nameB\x10\n\x0e_crash_addressB\x13\n\x11_crash_stacktrace\"\x8f\x02\n\x1bStoreFuzzerRunResultsOutput\x12\x1f\n\x12\x66uzzer_return_code\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12&\n\x19generated_testcase_string\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1b\n\x0e\x63onsole_output\x18\x03 \x01(\tH\x02\x88\x01\x01\x12%\n\x18uploaded_sample_testcase\x18\x04 \x01(\x08H\x03\x88\x01\x01\x42\x15\n\x13_fuzzer_return_codeB\x1c\n\x1a_generated_testcase_stringB\x11\n\x0f_console_outputB\x1b\n\x19_uploaded_sample_testcase\"\xa4\x07\n\rFuzzTaskCrash\x12\x16\n\tfile_path\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\ncrash_time\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x18\n\x0breturn_code\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x15\n\rresource_list\x18\x04 \x03(\t\x12\x10\n\x08gestures\x18\x05 \x03(\t\x12\x16\n\targuments\x18\x06 \x01(\tH\x03\x88\x01\x01\x12\x1a\n\x12\x66uzzing_strategies\x18\x07 \x03(\t\x12\x1a\n\rsecurity_flag\x18\x08 \x01(\x08H\x04\x88\x01\x01\x12\x1e\n\x11should_be_ignored\x18\t \x01(\x08H\x05\x88\x01\x01\x12\x16\n\thttp_flag\x18\n \x01(\x08H\x06\x88\x01\x01\x12%\n\x18\x61pplication_command_line\x18\x0b \x01(\tH\x07\x88\x01\x01\x12*\n\x1dunsymbolized_crash_stacktrace\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x17\n\ncrash_type\x18\r \x01(\tH\t\x88\x01\x01\x12\x1a\n\rcrash_address\x18\x0e \x01(\tH\n\x88\x01\x01\x12\x18\n\x0b\x63rash_state\x18\x0f \x01(\tH\x0b\x88\x01\x01\x12\x1d\n\x10\x63rash_stacktrace\x18\x10 \x01(\tH\x0c\x88\x01\x01\x12\x18\n\x10\x63rash_categories\x18\x11 \x03(\t\x12\x10\n\x03key\x18\x12 \x01(\tH\r\x88\x01\x01\x12\x15\n\x08is_valid\x18\x14 \x01(\x08H\x0e\x88\x01\x01\x12\x17\n\nfuzzed_key\x18\x15 \x01(\tH\x0f\x88\x01\x01\x12\x1a\n\rabsolute_path\x18\x16 \x01(\tH\x10\x88\x01\x01\x12\x1d\n\x10\x61rchive_filename\x18\x17 \x01(\tH\x11\x88\x01\x01\x42\x0c\n\n_file_pathB\r\n\x0b_crash_timeB\x0e\n\x0c_return_codeB\x0c\n\n_argumentsB\x10\n\x0e_security_flagB\x14\n\x12_should_be_ignoredB\x0c\n\n_http_flagB\x1b\n\x19_application_command_lineB \n\x1e_unsymbolized_crash_stacktraceB\r\n\x0b_crash_typeB\x10\n\x0e_crash_addressB\x0e\n\x0c_crash_stateB\x13\n\x11_crash_stacktraceB\x06\n\x04_keyB\x0b\n\t_is_validB\r\n\x0b_fuzzed_keyB\x10\n\x0e_absolute_pathB\x13\n\x11_archive_filename\"\xe5\x02\n\x0b\x46uzzContext\x12\x14\n\x07redzone\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x1a\n\rdisable_ubsan\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x1c\n\x0fwindow_argument\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1f\n\x12timeout_multiplier\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12\x19\n\x0ctest_timeout\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12\x39\n\x0f\x66uzzer_metadata\x18\x06 \x03(\x0b\x32 .FuzzContext.FuzzerMetadataEntry\x1a\x35\n\x13\x46uzzerMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\n\n\x08_redzoneB\x10\n\x0e_disable_ubsanB\x12\n\x10_window_argumentB\x15\n\x13_timeout_multiplierB\x0f\n\r_test_timeout\"\xdb\x01\n\x12\x46uzzTaskCrashGroup\x12\"\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x0c.FuzzContextH\x00\x88\x01\x01\x12\x1f\n\x07\x63rashes\x18\x02 \x03(\x0b\x32\x0e.FuzzTaskCrash\x12\'\n\nmain_crash\x18\x03 \x01(\x0b\x32\x0e.FuzzTaskCrashH\x01\x88\x01\x01\x12\"\n\x15one_time_crasher_flag\x18\x04 \x01(\x08H\x02\x88\x01\x01\x42\n\n\x08_contextB\r\n\x0b_main_crashB\x18\n\x16_one_time_crasher_flag\"\x93\x04\n\x0e\x46uzzTaskOutput\x12(\n\x1b\x66ully_qualified_fuzzer_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x0e\x63rash_revision\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1e\n\x11job_run_timestamp\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x1f\n\x12testcases_executed\x18\x06 \x01(\x03H\x03\x88\x01\x01\x12=\n\x12\x66uzzer_run_results\x18\x08 \x01(\x0b\x32\x1c.StoreFuzzerRunResultsOutputH\x04\x88\x01\x01\x12\x1e\n\x11new_targets_count\x18\t \x01(\x05H\x05\x88\x01\x01\x12\x1c\n\x0f\x66uzzer_revision\x18\n \x01(\x05H\x06\x88\x01\x01\x12\x14\n\x0c\x66uzz_targets\x18\x0b \x03(\t\x12\x1a\n\x12testcase_run_jsons\x18\x0c \x03(\t\x12)\n\x0c\x63rash_groups\x18\r \x03(\x0b\x32\x13.FuzzTaskCrashGroupB\x1e\n\x1c_fully_qualified_fuzzer_nameB\x11\n\x0f_crash_revisionB\x14\n\x12_job_run_timestampB\x15\n\x13_testcases_executedB\x15\n\x13_fuzzer_run_resultsB\x14\n\x12_new_targets_countB\x12\n\x10_fuzzer_revision\"\xd7\x05\n\x12MinimizeTaskOutput\x12L\n\x16last_crash_result_dict\x18\x01 \x03(\x0b\x32,.MinimizeTaskOutput.LastCrashResultDictEntry\x12\x18\n\x0b\x66laky_stack\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12&\n\x19security_severity_updated\x18\x03 \x01(\x08H\x01\x88\x01\x01\x12\x1e\n\x11security_severity\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12\x1f\n\x12minimization_phase\x18\x05 \x01(\x05H\x03\x88\x01\x01\x12\x10\n\x08gestures\x18\x06 \x03(\t\x12\x1b\n\x0eminimized_keys\x18\x07 \x01(\tH\x04\x88\x01\x01\x12 \n\x13minimized_arguments\x18\x08 \x01(\tH\x05\x88\x01\x01\x12\x1a\n\rarchive_state\x18\t \x01(\x05H\x06\x88\x01\x01\x12\x1a\n\rabsolute_path\x18\n \x01(\tH\x07\x88\x01\x01\x12G\n\x13memory_tool_options\x18\x0b \x03(\x0b\x32*.MinimizeTaskOutput.MemoryToolOptionsEntry\x1a:\n\x18LastCrashResultDictEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x38\n\x16MemoryToolOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0e\n\x0c_flaky_stackB\x1c\n\x1a_security_severity_updatedB\x14\n\x12_security_severityB\x15\n\x13_minimization_phaseB\x11\n\x0f_minimized_keysB\x16\n\x14_minimized_argumentsB\x10\n\x0e_archive_stateB\x10\n\x0e_absolute_path\"\xef\x02\n\x14RegressionTaskOutput\x12#\n\x16regression_range_start\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12!\n\x14regression_range_end\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12 \n\x13last_regression_min\x18\x03 \x01(\x03H\x02\x88\x01\x01\x12 \n\x13last_regression_max\x18\x04 \x01(\x03H\x03\x88\x01\x01\x12#\n\x0f\x62uild_data_list\x18\x05 \x03(\x0b\x32\n.BuildData\x12%\n\x18is_testcase_reproducible\x18\x06 \x01(\x08H\x04\x88\x01\x01\x42\x19\n\x17_regression_range_startB\x17\n\x15_regression_range_endB\x16\n\x14_last_regression_minB\x16\n\x14_last_regression_maxB\x1b\n\x19_is_testcase_reproducible\"\xa3\x02\n\x11VariantTaskOutput\x12\x13\n\x06status\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x15\n\x08revision\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x17\n\ncrash_type\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x0b\x63rash_state\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1a\n\rsecurity_flag\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x17\n\nis_similar\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12\x15\n\x08platform\x18\x07 \x01(\tH\x06\x88\x01\x01\x42\t\n\x07_statusB\x0b\n\t_revisionB\r\n\x0b_crash_typeB\x0e\n\x0c_crash_stateB\x10\n\x0e_security_flagB\r\n\x0b_is_similarB\x0b\n\t_platform\"\xe7\x01\n\tBuildData\x12\x15\n\x08revision\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x19\n\x0cis_bad_build\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\'\n\x1ashould_ignore_crash_result\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12%\n\x18\x62uild_run_console_output\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x0b\n\t_revisionB\x0f\n\r_is_bad_buildB\x1d\n\x1b_should_ignore_crash_resultB\x1b\n\x19_build_run_console_output\"\xbc\x04\n\x15ProgressionTaskOutput\x12\x19\n\x0cmin_revision\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x19\n\x0cmax_revision\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x1c\n\x0f\x63rash_on_latest\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12$\n\x17\x63rash_on_latest_message\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1b\n\x0e\x63rash_revision\x18\x05 \x01(\x03H\x04\x88\x01\x01\x12)\n\x1clast_tested_crash_stacktrace\x18\x06 \x01(\tH\x05\x88\x01\x01\x12!\n\x14last_progression_min\x18\x07 \x01(\x03H\x06\x88\x01\x01\x12!\n\x14last_progression_max\x18\x08 \x01(\x03H\x07\x88\x01\x01\x12#\n\x16\x63lear_min_max_metadata\x18\t \x01(\x08H\x08\x88\x01\x01\x12#\n\x0f\x62uild_data_list\x18\x0b \x03(\x0b\x32\n.BuildDataB\x0f\n\r_min_revisionB\x0f\n\r_max_revisionB\x12\n\x10_crash_on_latestB\x1a\n\x18_crash_on_latest_messageB\x11\n\x0f_crash_revisionB\x1f\n\x1d_last_tested_crash_stacktraceB\x17\n\x15_last_progression_minB\x17\n\x15_last_progression_maxB\x19\n\x17_clear_min_max_metadata\"\xc6\x03\n\x1a\x43rossPollinationStatistics\x12#\n\x16project_qualified_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07sources\x18\x02 \x01(\tH\x01\x88\x01\x01\x12 \n\x13initial_corpus_size\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x18\n\x0b\x63orpus_size\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\"\n\x15initial_edge_coverage\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12\x1a\n\redge_coverage\x18\x06 \x01(\x05H\x05\x88\x01\x01\x12%\n\x18initial_feature_coverage\x18\x07 \x01(\x05H\x06\x88\x01\x01\x12\x1d\n\x10\x66\x65\x61ture_coverage\x18\x08 \x01(\x05H\x07\x88\x01\x01\x42\x19\n\x17_project_qualified_nameB\n\n\x08_sourcesB\x16\n\x14_initial_corpus_sizeB\x0e\n\x0c_corpus_sizeB\x18\n\x16_initial_edge_coverageB\x10\n\x0e_edge_coverageB\x1b\n\x19_initial_feature_coverageB\x13\n\x11_feature_coverage\"\x97\x04\n\x13\x43overageInformation\x12\x19\n\x0cproject_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x32\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x88\x01\x01\x12\x1e\n\x11\x63orpus_size_units\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x1e\n\x11\x63orpus_size_bytes\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x1c\n\x0f\x63orpus_location\x18\x05 \x01(\tH\x04\x88\x01\x01\x12#\n\x16\x63orpus_backup_location\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\"\n\x15quarantine_size_units\x18\x07 \x01(\x05H\x06\x88\x01\x01\x12\"\n\x15quarantine_size_bytes\x18\x08 \x01(\x05H\x07\x88\x01\x01\x12 \n\x13quarantine_location\x18\t \x01(\tH\x08\x88\x01\x01\x42\x0f\n\r_project_nameB\x0c\n\n_timestampB\x14\n\x12_corpus_size_unitsB\x14\n\x12_corpus_size_bytesB\x12\n\x10_corpus_locationB\x19\n\x17_corpus_backup_locationB\x18\n\x16_quarantine_size_unitsB\x18\n\x16_quarantine_size_bytesB\x16\n\x14_quarantine_location\"\x81\x03\n\x17\x43orpusPruningTaskOutput\x12\x41\n\x17\x63ross_pollination_stats\x18\x01 \x01(\x0b\x32\x1b.CrossPollinationStatisticsH\x00\x88\x01\x01\x12\x30\n\rcoverage_info\x18\x02 \x01(\x0b\x32\x14.CoverageInformationH\x01\x88\x01\x01\x12\x1f\n\x12\x66uzzer_binary_name\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1b\n\x0e\x63rash_revision\x18\x04 \x01(\x03H\x03\x88\x01\x01\x12\x1b\n\x07\x63rashes\x18\x05 \x03(\x0b\x32\n.CrashInfo\x12#\n\x16\x63orpus_backup_uploaded\x18\x06 \x01(\x08H\x04\x88\x01\x01\x42\x1a\n\x18_cross_pollination_statsB\x10\n\x0e_coverage_infoB\x15\n\x13_fuzzer_binary_nameB\x11\n\x0f_crash_revisionB\x19\n\x17_corpus_backup_uploaded\"\x87\t\n\x06Output\x12#\n\nerror_type\x18\x03 \x01(\x0e\x32\n.ErrorTypeH\x00\x88\x01\x01\x12\"\n\ruworker_input\x18\x04 \x01(\x0b\x32\x06.InputH\x01\x88\x01\x01\x12\x19\n\x0ctest_timeout\x18\x05 \x01(\x02H\x02\x88\x01\x01\x12\x17\n\ncrash_time\x18\x06 \x01(\x02H\x03\x88\x01\x01\x12$\n\x17\x63rash_stacktrace_output\x18\x07 \x01(\tH\x04\x88\x01\x01\x12\x15\n\x08\x62ot_name\x18\x12 \x01(\tH\x05\x88\x01\x01\x12\x18\n\x0bplatform_id\x18\x13 \x01(\tH\x06\x88\x01\x01\x12\x34\n\x13\x61nalyze_task_output\x18\x08 \x01(\x0b\x32\x12.AnalyzeTaskOutputH\x07\x88\x01\x01\x12.\n\x10\x66uzz_task_output\x18\t \x01(\x0b\x32\x0f.FuzzTaskOutputH\x08\x88\x01\x01\x12\x36\n\x14minimize_task_output\x18\n \x01(\x0b\x32\x13.MinimizeTaskOutputH\t\x88\x01\x01\x12:\n\x16regression_task_output\x18\x0b \x01(\x0b\x32\x15.RegressionTaskOutputH\n\x88\x01\x01\x12<\n\x17progression_task_output\x18\x0c \x01(\x0b\x32\x16.ProgressionTaskOutputH\x0b\x88\x01\x01\x12\x38\n\x15symbolize_task_output\x18\r \x01(\x0b\x32\x14.SymbolizeTaskOutputH\x0c\x88\x01\x01\x12\x34\n\x13variant_task_output\x18\x0e \x01(\x0b\x32\x12.VariantTaskOutputH\r\x88\x01\x01\x12\x41\n\x1a\x63orpus_pruning_task_output\x18\x10 \x01(\x0b\x32\x18.CorpusPruningTaskOutputH\x0e\x88\x01\x01\x12\x32\n\x0eissue_metadata\x18\x11 \x03(\x0b\x32\x1a.Output.IssueMetadataEntry\x12\x1a\n\rerror_message\x18\x0f \x01(\tH\x0f\x88\x01\x01\x1a\x34\n\x12IssueMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\r\n\x0b_error_typeB\x10\n\x0e_uworker_inputB\x0f\n\r_test_timeoutB\r\n\x0b_crash_timeB\x1a\n\x18_crash_stacktrace_outputB\x0b\n\t_bot_nameB\x0e\n\x0c_platform_idB\x16\n\x14_analyze_task_outputB\x13\n\x11_fuzz_task_outputB\x17\n\x15_minimize_task_outputB\x19\n\x17_regression_task_outputB\x1a\n\x18_progression_task_outputB\x18\n\x16_symbolize_task_outputB\x16\n\x14_variant_task_outputB\x1d\n\x1b_corpus_pruning_task_outputB\x10\n\x0e_error_message*\xdd\x08\n\tErrorType\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x17\n\x13\x41NALYZE_BUILD_SETUP\x10\x01\x12\x14\n\x10\x41NALYZE_NO_CRASH\x10\x02\x12\x1d\n\x19\x41NALYZE_NO_REVISIONS_LIST\x10\x03\x12\x1d\n\x19\x41NALYZE_NO_REVISION_INDEX\x10\x04\x12\x12\n\x0eTESTCASE_SETUP\x10\x05\x12\r\n\tUNHANDLED\x10\x06\x12\x17\n\x13VARIANT_BUILD_SETUP\x10\x07\x12\x12\n\x0eMINIMIZE_SETUP\x10\x08\x12\x1c\n\x18\x46UZZ_BUILD_SETUP_FAILURE\x10\t\x12\"\n\x1e\x46UZZ_DATA_BUNDLE_SETUP_FAILURE\x10\n\x12\x12\n\x0e\x46UZZ_NO_FUZZER\x10\x0b\x12 \n\x1c\x46UZZ_NO_FUZZ_TARGET_SELECTED\x10\r\x12#\n\x1fPROGRESSION_REVISION_LIST_ERROR\x10\x0e\x12\x1f\n\x1bPROGRESSION_BUILD_NOT_FOUND\x10\x0f\x12\x18\n\x14PROGRESSION_NO_CRASH\x10\x10\x12!\n\x1dPROGRESSION_BAD_STATE_MIN_MAX\x10\x11\x12\x17\n\x13PROGRESSION_TIMEOUT\x10\x12\x12\x19\n\x15PROGRESSION_BAD_BUILD\x10\x13\x12!\n\x1dPROGRESSION_BUILD_SETUP_ERROR\x10\x14\x12\"\n\x1eREGRESSION_REVISION_LIST_ERROR\x10\x15\x12\x1e\n\x1aREGRESSION_BUILD_NOT_FOUND\x10\x16\x12 \n\x1cREGRESSION_BUILD_SETUP_ERROR\x10\x17\x12\x1e\n\x1aREGRESSION_BAD_BUILD_ERROR\x10\x18\x12\x17\n\x13REGRESSION_NO_CRASH\x10\x19\x12\x1c\n\x18REGRESSION_TIMEOUT_ERROR\x10\x1a\x12\x31\n-REGRESSION_LOW_CONFIDENCE_IN_REGRESSION_RANGE\x10\x1b\x12\x1f\n\x1bSYMBOLIZE_BUILD_SETUP_ERROR\x10\x1c\x12!\n\x1dMINIMIZE_UNREPRODUCIBLE_CRASH\x10\x1d\x12\x1c\n\x18MINIMIZE_CRASH_TOO_FLAKY\x10\x1e\x12\x1e\n\x1aMINIMIZE_DEADLINE_EXCEEDED\x10\x1f\x12\x31\n-MINIMIZE_DEADLINE_EXCEEDED_IN_MAIN_FILE_PHASE\x10 \x12)\n%LIBFUZZER_MINIMIZATION_UNREPRODUCIBLE\x10!\x12!\n\x1dLIBFUZZER_MINIMIZATION_FAILED\x10\"\x12&\n\"CORPUS_PRUNING_FUZZER_SETUP_FAILED\x10#\x12\x18\n\x14\x43ORPUS_PRUNING_ERROR\x10$b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'clusterfuzz._internal.protos.uworker_msg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CORPUS_CORPUSURLSENTRY']._options = None
  _globals['_CORPUS_CORPUSURLSENTRY']._serialized_options = b'8\001'
  _globals['_INPUT_UWORKERENVENTRY']._options = None
  _globals['_INPUT_UWORKERENVENTRY']._serialized_options = b'8\001'
  _globals['_FUZZCONTEXT_FUZZERMETADATAENTRY']._options = None
  _globals['_FUZZCONTEXT_FUZZERMETADATAENTRY']._serialized_options = b'8\001'
  _globals['_MINIMIZETASKOUTPUT_LASTCRASHRESULTDICTENTRY']._options = None
  _globals['_MINIMIZETASKOUTPUT_LASTCRASHRESULTDICTENTRY']._serialized_options = b'8\001'
  _globals['_MINIMIZETASKOUTPUT_MEMORYTOOLOPTIONSENTRY']._options = None
  _globals['_MINIMIZETASKOUTPUT_MEMORYTOOLOPTIONSENTRY']._serialized_options = b'8\001'
  _globals['_OUTPUT_ISSUEMETADATAENTRY']._options = None
  _globals['_OUTPUT_ISSUEMETADATAENTRY']._serialized_options = b'8\001'
  _globals['_ERRORTYPE']._serialized_start=13050
  _globals['_ERRORTYPE']._serialized_end=14167
  _globals['_SETUPINPUT']._serialized_start=111
  _globals['_SETUPINPUT']._serialized_end=488
  _globals['_ANALYZETASKINPUT']._serialized_start=490
  _globals['_ANALYZETASKINPUT']._serialized_end=531
  _globals['_SYMBOLIZETASKINPUT']._serialized_start=533
  _globals['_SYMBOLIZETASKINPUT']._serialized_end=613
  _globals['_BLOBUPLOADURL']._serialized_start=615
  _globals['_BLOBUPLOADURL']._serialized_end=682
  _globals['_FUZZTASKINPUT']._serialized_start=685
  _globals['_FUZZTASKINPUT']._serialized_end=1102
  _globals['_DATABUNDLECORPUS']._serialized_start=1105
  _globals['_DATABUNDLECORPUS']._serialized_end=1242
  _globals['_FUZZTARGETCORPUS']._serialized_start=1244
  _globals['_FUZZTARGETCORPUS']._serialized_end=1368
  _globals['_CORPUS']._serialized_start=1371
  _globals['_CORPUS']._serialized_end=1613
  _globals['_CORPUS_CORPUSURLSENTRY']._serialized_start=1530
  _globals['_CORPUS_CORPUSURLSENTRY']._serialized_end=1579
  _globals['_MINIMIZETASKINPUT']._serialized_start=1616
  _globals['_MINIMIZETASKINPUT']._serialized_end=1890
  _globals['_REGRESSIONTASKINPUT']._serialized_start=1892
  _globals['_REGRESSIONTASKINPUT']._serialized_end=1936
  _globals['_PROGRESSIONTASKINPUT']._serialized_start=1939
  _globals['_PROGRESSIONTASKINPUT']._serialized_end=2196
  _globals['_CROSSPOLLINATEFUZZERPROTO']._serialized_start=2199
  _globals['_CROSSPOLLINATEFUZZERPROTO']._serialized_end=2402
  _globals['_CORPUSPRUNINGTASKINPUT']._serialized_start=2405
  _globals['_CORPUSPRUNINGTASKINPUT']._serialized_end=3066
  _globals['_INPUT']._serialized_start=3069
  _globals['_INPUT']._serialized_end=4440
  _globals['_INPUT_UWORKERENVENTRY']._serialized_start=4002
  _globals['_INPUT_UWORKERENVENTRY']._serialized_end=4051
  _globals['_VARIANTTASKINPUT']._serialized_start=4442
  _globals['_VARIANTTASKINPUT']._serialized_end=4514
  _globals['_SYMBOLIZETASKOUTPUT']._serialized_start=4517
  _globals['_SYMBOLIZETASKOUTPUT']._serialized_end=4844
  _globals['_ANALYZETASKOUTPUT']._serialized_start=4847
  _globals['_ANALYZETASKOUTPUT']._serialized_end=5634
  _globals['_CRASHINFO']._serialized_start=5637
  _globals['_CRASHINFO']._serialized_end=5974
  _globals['_STOREFUZZERRUNRESULTSOUTPUT']._serialized_start=5977
  _globals['_STOREFUZZERRUNRESULTSOUTPUT']._serialized_end=6248
  _globals['_FUZZTASKCRASH']._serialized_start=6251
  _globals['_FUZZTASKCRASH']._serialized_end=7183
  _globals['_FUZZCONTEXT']._serialized_start=7186
  _globals['_FUZZCONTEXT']._serialized_end=7543
  _globals['_FUZZCONTEXT_FUZZERMETADATAENTRY']._serialized_start=7400
  _globals['_FUZZCONTEXT_FUZZERMETADATAENTRY']._serialized_end=7453
  _globals['_FUZZTASKCRASHGROUP']._serialized_start=7546
  _globals['_FUZZTASKCRASHGROUP']._serialized_end=7765
  _globals['_FUZZTASKOUTPUT']._serialized_start=7768
  _globals['_FUZZTASKOUTPUT']._serialized_end=8299
  _globals['_MINIMIZETASKOUTPUT']._serialized_start=8302
  _globals['_MINIMIZETASKOUTPUT']._serialized_end=9029
  _globals['_MINIMIZETASKOUTPUT_LASTCRASHRESULTDICTENTRY']._serialized_start=8743
  _globals['_MINIMIZETASKOUTPUT_LASTCRASHRESULTDICTENTRY']._serialized_end=8801
  _globals['_MINIMIZETASKOUTPUT_MEMORYTOOLOPTIONSENTRY']._serialized_start=8803
  _globals['_MINIMIZETASKOUTPUT_MEMORYTOOLOPTIONSENTRY']._serialized_end=8859
  _globals['_REGRESSIONTASKOUTPUT']._serialized_start=9032
  _globals['_REGRESSIONTASKOUTPUT']._serialized_end=9399
  _globals['_VARIANTTASKOUTPUT']._serialized_start=9402
  _globals['_VARIANTTASKOUTPUT']._serialized_end=9693
  _globals['_BUILDDATA']._serialized_start=9696
  _globals['_BUILDDATA']._serialized_end=9927
  _globals['_PROGRESSIONTASKOUTPUT']._serialized_start=9930
  _globals['_PROGRESSIONTASKOUTPUT']._serialized_end=10502
  _globals['_CROSSPOLLINATIONSTATISTICS']._serialized_start=10505
  _globals['_CROSSPOLLINATIONSTATISTICS']._serialized_end=10959
  _globals['_COVERAGEINFORMATION']._serialized_start=10962
  _globals['_COVERAGEINFORMATION']._serialized_end=11497
  _globals['_CORPUSPRUNINGTASKOUTPUT']._serialized_start=11500
  _globals['_CORPUSPRUNINGTASKOUTPUT']._serialized_end=11885
  _globals['_OUTPUT']._serialized_start=11888
  _globals['_OUTPUT']._serialized_end=13047
  _globals['_OUTPUT_ISSUEMETADATAENTRY']._serialized_start=12649
  _globals['_OUTPUT_ISSUEMETADATAENTRY']._serialized_end=12701
# @@protoc_insertion_point(module_scope)
