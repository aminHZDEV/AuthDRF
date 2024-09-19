import grpc
from app.otp import otp_pb2
from app.otp import otp_pb2_grpc

def generate_otp(phone_number):
    with grpc.insecure_channel('otp_service:50051') as channel:
        stub = otp_pb2_grpc.OTPServiceStub(channel)
        response = stub.GenerateOTP(otp_pb2.OTPRequest(phone_number=phone_number))
        return response.status

def verify_otp(phone_number, otp_code):
    with grpc.insecure_channel('otp_service:50051') as channel:
        stub = otp_pb2_grpc.OTPServiceStub(channel)
        response = stub.VerifyOTP(otp_pb2.VerifyOTPRequest(phone_number=phone_number, otp_code=otp_code))
        return response.status