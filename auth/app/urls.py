from django.urls import path
from .views import UserList, UserDetail, UserRegister, VerifyOTPView

urlpatterns = [
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user-detail"),
    path("register/", UserRegister.as_view(), name="user-register"),
    path("verify-otp/", VerifyOTPView.as_view(), name="verify-otp"),
]
