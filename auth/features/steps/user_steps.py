from behave import given, when, then
from django.urls import reverse
from django.utils.http import urlencode
from rest_framework import status


@given("I am a new user")
def step_impl(context):
    pass


@when("I register with the following details")
def step_impl(context):
    data = {
        heading: row[heading]
        for heading in context.table.headings
        for row in context.table
    }
    response = context.client.post(reverse("user-register"), data, format="json")
    context.response = response


@then("I should receive a confirmation with status 201")
def step_impl(context):
    assert context.response.status_code == status.HTTP_201_CREATED


@then("the response should contain the following details after register")
def step_impl(context):
    expected_data = {
        heading: row[heading]
        for heading in context.table.headings
        for row in context.table
    }
    response_data = context.response.json()
    for key, value in expected_data.items():
        assert response_data[key] == value


@given("I am authenticated with the following credentials")
def step_impl(context):
    data = {
        heading: row[heading]
        for heading in context.table.headings
        for row in context.table
    }
    response = context.client.post(reverse("user-register"), data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    first_row = context.table[0]
    response = context.client.post(
        reverse("oauth2_provider:token"),
        data=urlencode(
            {
                "grant_type": "password",
                "username": first_row["username"],
                "password": first_row["password"],
                "client_id": "QRNWDlFbdrzyD8YZiHxugnjU7vuhkPMjPMatDHj6",
                "client_secret": "my_client",
            }
        ),
        content_type="application/x-www-form-urlencoded",
    )
    context.response = response
    assert response.status_code == status.HTTP_200_OK
    context.auth_token = response.json().get("access_token")


@when("I request an access token")
def step_impl(context):
    assert context.auth_token is not None


@then("I should receive a token with status 200")
def step_impl(context):
    assert context.response.status_code == status.HTTP_200_OK


@then("the token response should contain the following details")
def step_impl(context):
    expected_data = {
        heading: row[heading]
        for heading in context.table.headings
        for row in context.table
    }
    response_data = context.response.json()
    for key, value in expected_data.items():
        if key == "access_token":
            assert "access_token" in response_data
        else:
            try:
                value = int(value)
            except Exception as e:
                pass
            assert response_data[key] == value


@then("I should store the access token for subsequent requests")
def step_impl(context):
    if "auth_token" not in context or context.auth_token is None:
        raise AssertionError("Authentication token not found.")


@given("I am authenticated with the stored access token")
def step_impl(context):
    data = {
        heading: row[heading]
        for heading in context.table.headings
        for row in context.table
    }
    response = context.client.post(reverse("user-register"), data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    first_row = context.table[0]
    response = context.client.post(
        reverse("oauth2_provider:token"),
        data=urlencode(
            {
                "grant_type": "password",
                "username": first_row["username"],
                "password": first_row["password"],
                "client_id": "QRNWDlFbdrzyD8YZiHxugnjU7vuhkPMjPMatDHj6",
                "client_secret": "my_client",
            }
        ),
        content_type="application/x-www-form-urlencoded",
    )
    context.response = response
    assert response.status_code == status.HTTP_200_OK
    context.auth_token = response.json().get("access_token")
    if "auth_token" in context and context.auth_token is not None:
        context.client.credentials(HTTP_AUTHORIZATION=f"Bearer {context.auth_token}")
    else:
        raise AssertionError(
            "Authentication token not found. Please obtain an access token first."
        )


@when("I request the list of users")
def step_impl(context):
    response = context.client.get(reverse("user-list"))
    context.response = response


@then("I should receive a list of users with status 200")
def step_impl(context):
    assert context.response.status_code == status.HTTP_200_OK


@then("the response should contain the following details")
def step_impl(context):
    expected_data = [
        {heading: row[heading] for heading in context.table.headings}
        for row in context.table
    ]
    response_data = context.response.json()
    response_user_dict = {user["username"]: user for user in response_data}
    for expected_user in expected_data:
        username = expected_user["username"]
        assert (
            username in response_user_dict
        ), f"User {username} not found in response data."
        assert (
            response_user_dict[username]["phone_number"]
            == expected_user["phone_number"]
        ), f"Phone number for {username} does not match: expected {expected_user['phone_number']}, actual {response_user_dict[username]['phone_number']}"
        assert (
            response_user_dict[username]["email"] == expected_user["email"]
        ), f"Email for {username} does not match: expected {expected_user['email']}, actual {response_user_dict[username]['email']}"
