# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: otp.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'otp.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\totp.proto\x12\x03otp\"\"\n\nOTPRequest\x12\x14\n\x0cphone_number\x18\x01 \x01(\t\"/\n\x0bOTPResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x10\n\x08otp_code\x18\x02 \x01(\t\":\n\x10VerifyOTPRequest\x12\x14\n\x0cphone_number\x18\x01 \x01(\t\x12\x10\n\x08otp_code\x18\x02 \x01(\t\"#\n\x11VerifyOTPResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2z\n\nOTPService\x12\x30\n\x0bGenerateOTP\x12\x0f.otp.OTPRequest\x1a\x10.otp.OTPResponse\x12:\n\tVerifyOTP\x12\x15.otp.VerifyOTPRequest\x1a\x16.otp.VerifyOTPResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'otp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_OTPREQUEST']._serialized_start=18
  _globals['_OTPREQUEST']._serialized_end=52
  _globals['_OTPRESPONSE']._serialized_start=54
  _globals['_OTPRESPONSE']._serialized_end=101
  _globals['_VERIFYOTPREQUEST']._serialized_start=103
  _globals['_VERIFYOTPREQUEST']._serialized_end=161
  _globals['_VERIFYOTPRESPONSE']._serialized_start=163
  _globals['_VERIFYOTPRESPONSE']._serialized_end=198
  _globals['_OTPSERVICE']._serialized_start=200
  _globals['_OTPSERVICE']._serialized_end=322
# @@protoc_insertion_point(module_scope)
