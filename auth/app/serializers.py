from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(allow_null=False)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone_number", "password"]


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    phone_number = PhoneNumberField(allow_null=True, required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone_number", "password"]

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            phone_number=validated_data["phone_number"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user
