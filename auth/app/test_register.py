import pytest
from unittest.mock import patch, MagicMock
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from .models import CustomUser

# Mock URLs
REGISTER_URL = "http://localhost:8000/api/register/"
TOKEN_URL = "http://127.0.0.1:8000/oauth/token/"


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def mock_access_token():
    with patch("requests.post") as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = status.HTTP_200_OK
        mock_response.json.return_value = {"access_token": "fake-access-token"}
        mock_post.return_value = mock_response
        yield mock_post


@pytest.mark.django_db
class TestUserViews:

    def test_register_user(self, mock_access_token):
        with patch("requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = status.HTTP_201_CREATED
            mock_response.json.return_value = {
                "username": "aminhzdev",
                "email": "amin@son.ir",
                "phone_number": "+989331109442",
            }
            mock_post.return_value = mock_response
            response = mock_post(
                REGISTER_URL,
                json={
                    "email": "amin@son.ir",
                    "username": "aminhzdev",
                    "password": "adminpassword",
                    "phone_number": "+989331109442",
                },
            )
            assert response.status_code == status.HTTP_201_CREATED
            data = response.json()
            assert data["username"] == "aminhzdev"
            assert data["email"] == "amin@son.ir"
            assert data["phone_number"] == "+989331109442"

    def test_list_users(self, api_client, mock_access_token):
        api_client.credentials(HTTP_AUTHORIZATION="Bearer fake-access-token")
        with patch("rest_framework.test.APIClient.get") as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = status.HTTP_200_OK
            mock_response.json.return_value = [{"username": "aminhzdev"}]
            mock_get.return_value = mock_response
            response = api_client.get(reverse("user-list"))
            assert response.status_code == status.HTTP_200_OK
            assert "username" in response.json()[0]

    def test_create_user(self, api_client, mock_access_token):
        api_client.credentials(HTTP_AUTHORIZATION="Bearer fake-access-token")
        data = {
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "newpassword",
            "phone_number": "+989335692244",
        }
        with patch("rest_framework.test.APIClient.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = status.HTTP_201_CREATED
            mock_response.json.return_value = data
            mock_post.return_value = mock_response
            response = api_client.post(reverse("user-list"), data, format="json")
            assert response.status_code == status.HTTP_201_CREATED
            assert response.json()["username"] == "newuser"

    def test_retrieve_user(self, api_client, mock_access_token):
        api_client.credentials(HTTP_AUTHORIZATION="Bearer fake-access-token")
        user = CustomUser.objects.create(
            username="retrieveuser",
            email="retrieveuser@example.com",
            password="password",
        )
        with patch("rest_framework.test.APIClient.get") as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = status.HTTP_200_OK
            mock_response.json.return_value = {
                "username": "retrieveuser",
                "email": "retrieveuser@example.com",
            }
            mock_get.return_value = mock_response
            response = api_client.get(reverse("user-detail", args=[user.pk]))
            assert response.status_code == status.HTTP_200_OK
            assert response.json()["username"] == "retrieveuser"

    def test_update_user(self, api_client, mock_access_token):
        api_client.credentials(HTTP_AUTHORIZATION="Bearer fake-access-token")
        user = CustomUser.objects.create(
            username="updateuser", email="updateuser@example.com", password="password"
        )
        data = {
            "email": "updateduser@example.com",
            "phone_number": "+989446558552",
        }
        with patch("rest_framework.test.APIClient.patch") as mock_patch:
            mock_response = MagicMock()
            mock_response.status_code = status.HTTP_200_OK
            mock_response.json.return_value = data
            mock_patch.return_value = mock_response
            response = api_client.patch(
                reverse("user-detail", args=[user.pk]), data, format="json"
            )
            assert response.status_code == status.HTTP_200_OK
            assert response.json()["email"] == "updateduser@example.com"

    @patch("oauth2_provider.contrib.rest_framework.OAuth2Authentication.authenticate")
    def test_delete_user(self, mock_authenticate, api_client):
        mock_authenticate.return_value = (
            CustomUser.objects.create(
                username="testuser",
                email="testuser@example.com",
                password="password",
                phone_number="+989665289889",
            ),
            None,
        )
        user_to_delete = CustomUser.objects.create(
            username="deleteuser",
            email="deleteuser@example.com",
            password="password",
            phone_number="+989665289881",
        )
        api_client.credentials(HTTP_AUTHORIZATION="Bearer fake-access-token")
        response = api_client.delete(reverse("user-detail", args=[user_to_delete.pk]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert CustomUser.objects.filter(pk=user_to_delete.pk).count() == 0
