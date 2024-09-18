from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from otp.grpc_client import generate_otp, verify_otp
from oauth2_provider.models import AccessToken, Application
from django.utils.timezone import now
from datetime import timedelta
from oauthlib.common import generate_token



class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserRegister(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')

        otp_status = generate_otp(phone_number)

        if otp_status == "OTP sent":
            return Response({"detail": "OTP sent to your phone. Verify to complete registration."},
                            status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Failed to send OTP"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VerifyOTPView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        otp_code = request.data.get('otp_code')

        verification_status = verify_otp(phone_number, otp_code)

        if verification_status == "OTP verified":
            serializer = UserRegisterSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()

                app = Application.objects.get(name="Test app")  # Use correct application name
                token = generate_token()
                expires = now() + timedelta(hours=1)
                access_token = AccessToken.objects.create(
                    user=user,
                    application=app,
                    token=token,
                    expires=expires,
                    scope="read write"
                )
                return Response({
                    "detail": "OTP verified, registration complete.",
                    "access_token": access_token.token,
                    "expires": expires
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)