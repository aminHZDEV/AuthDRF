from oauth2_provider.oauth2_validators import OAuth2Validator
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from app.otp.grpc_client import verify_otp

USER_MODEL = get_user_model()


class MyOAuth2Validator(OAuth2Validator):

    def validate_user(self, username, password, client, request, *args, **kwargs):
        for item in request.decoded_body:
            if "phone_number" in item:
                phone_number = item[1]
            if "otp_code" in item:
                otp_code = item[1]
        try:
            print("phone : ", phone_number, " | ", "otp : ", otp_code)
            user = USER_MODEL.objects.get(phone_number=phone_number)
            print("user : ", user)
            otp_status = verify_otp(phone_number, otp_code)
            if otp_status == "OTP verified" and user.is_active:
                request.user = user
                return True
        except ObjectDoesNotExist:
            return False
        return False
