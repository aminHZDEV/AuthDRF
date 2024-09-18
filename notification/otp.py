import grpc
from concurrent import futures
import otp_pb2
import otp_pb2_grpc
import random
import configparser
from twilio.rest import Client

config = configparser.ConfigParser()
config.read('config.ini')

otp_store = {}


class OTPServiceServicer(otp_pb2_grpc.OTPServiceServicer):
    def GenerateOTP(self, request, context):
        otp_code = str(random.randint(100000, 999999))
        phone_number = request.phone_number
        otp_store[phone_number] = otp_code
        send_otp_via_sms(phone_number, otp_code)
        return otp_pb2.OTPResponse(status="OTP sent", otp_code=otp_code)

    def VerifyOTP(self, request, context):
        phone_number = request.phone_number
        otp_code = request.otp_code

        if phone_number in otp_store and otp_store[phone_number] == otp_code:
            return otp_pb2.VerifyOTPResponse(status="OTP verified")
        else:
            return otp_pb2.VerifyOTPResponse(status="Invalid OTP")


def send_otp_via_sms(phone_number, otp_code):
    account_sid = config['twilio']['account_sid']
    auth_token = config['twilio']['auth_token']
    from_number = config['twilio']['from_number']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Your OTP is: {otp_code}',
        from_=from_number,
        to=phone_number
    )
    print(f"Sent OTP {otp_code} to {phone_number}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    otp_pb2_grpc.add_OTPServiceServicer_to_server(OTPServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("OTP gRPC server started on port 50051")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()