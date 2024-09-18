import json
from behave import given, when, then
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from app.models import CustomUser


@given("I am a new user")
def step_impl(context):
    context.client = APIClient()


@when("I register with the following details")
def step_impl(context):
    data = {row["key"]: row["value"] for row in context.table}
    response = context.client.post(reverse("user-list"), data, format="json")
    context.response = response


@then("I should receive a confirmation with status {status_code}")
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)


@then("the response should contain the following details")
def step_impl(context):
    response_data = context.response.json()
    for row in context.table:
        key = row["key"]
        value = row["value"]
        assert response_data.get(key) == value


@given("I am authenticated")
def step_impl(context):
    context.client.credentials(HTTP_AUTHORIZATION="Bearer fake-access-token")


@when("I create a user with the following details")
def step_impl(context):
    data = {row["key"]: row["value"] for row in context.table}
    response = context.client.post(reverse("user-list"), data, format="json")
    context.response = response


@when('I retrieve the user with username "{username}"')
def step_impl(context, username):
    user = CustomUser.objects.get(username=username)
    response = context.client.get(reverse("user-detail", args=[user.pk]))
    context.response = response


@when("I update the user's email with the following details")
def step_impl(context):
    data = {row["key"]: row["value"] for row in context.table}
    user = CustomUser.objects.get(username="updateuser")
    response = context.client.patch(
        reverse("user-detail", args=[user.pk]), data, format="json"
    )
    context.response = response


@when('I delete the user with username "{username}"')
def step_impl(context, username):
    user = CustomUser.objects.get(username=username)
    response = context.client.delete(reverse("user-detail", args=[user.pk]))
    context.response = response


@then("the details should contain the following information")
def step_impl(context):
    response_data = context.response.json()
    for row in context.table:
        key = row["key"]
        value = row["value"]
        assert response_data.get(key) == value


@then("the user should no longer exist")
def step_impl(context):
    user = CustomUser.objects.filter(username="deleteuser")
    assert user.count() == 0
