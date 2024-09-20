from xml.dom import ValidationErr

import grpc
from concurrent import futures
import otp_pb2
import otp_pb2_grpc
import random
import configparser
import ghasedak_sms
import traceback


config = configparser.ConfigParser()
config.read("config.ini")

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
    api_key = config["ghasedak"]["api_key"]
    line_number = config["ghasedak"]["line_number"]
    print(f"Send sms to {phone_number}, otp code is {otp_code}")
    # sms = ghasedak_sms.Ghasedak(api_key=api_key)
    #
    # try:
    #     response = sms.send_single_sms(
    #         message=f"Your OTP is: {otp_code}",  # The OTP message
    #         receptor=phone_number,  # The recipient's phone number
    #         linenumber=line_number,  # Your sender line number
    #         senddate='',  # Optional, you can specify if needed
    #         checkid=''  # Optional, you can specify if needed
    #     )
    #     if response.status_code == 200:
    #         print(f"Sent OTP {otp_code} to {phone_number}")
    #     else:
    #         raise ValidationErr(f"Status is {response.status_code} with message {response.message}")
    # except Exception as e:
    #     print(f"Error sending OTP: {e}")


def serve():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=int(config["grpc"]["max_workers"]))
    )
    otp_pb2_grpc.add_OTPServiceServicer_to_server(OTPServiceServicer(), server)
    server.add_insecure_port(f"{config['grpc']['host']}:{config['grpc']['port']}")
    server.start()
    print(f"OTP gRPC server started on port {config['grpc']['port']}")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
