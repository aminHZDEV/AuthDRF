# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import otp_pb2 as otp__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in otp_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class OTPServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateOTP = channel.unary_unary(
                '/otp.OTPService/GenerateOTP',
                request_serializer=otp__pb2.OTPRequest.SerializeToString,
                response_deserializer=otp__pb2.OTPResponse.FromString,
                _registered_method=True)
        self.VerifyOTP = channel.unary_unary(
                '/otp.OTPService/VerifyOTP',
                request_serializer=otp__pb2.VerifyOTPRequest.SerializeToString,
                response_deserializer=otp__pb2.VerifyOTPResponse.FromString,
                _registered_method=True)


class OTPServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GenerateOTP(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyOTP(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OTPServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateOTP': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateOTP,
                    request_deserializer=otp__pb2.OTPRequest.FromString,
                    response_serializer=otp__pb2.OTPResponse.SerializeToString,
            ),
            'VerifyOTP': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyOTP,
                    request_deserializer=otp__pb2.VerifyOTPRequest.FromString,
                    response_serializer=otp__pb2.VerifyOTPResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'otp.OTPService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('otp.OTPService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class OTPService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GenerateOTP(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/otp.OTPService/GenerateOTP',
            otp__pb2.OTPRequest.SerializeToString,
            otp__pb2.OTPResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def VerifyOTP(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/otp.OTPService/VerifyOTP',
            otp__pb2.VerifyOTPRequest.SerializeToString,
            otp__pb2.VerifyOTPResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
