import os
import django
import subprocess
import time
from rest_framework.test import APIClient
from oauth2_provider.models import Application


server_process = None

def before_scenario(context, scenario):
    context.client = APIClient()
    app, created = Application.objects.get_or_create(
        client_id='QRNWDlFbdrzyD8YZiHxugnjU7vuhkPMjPMatDHj6',
        client_secret='my_client',
        user=None,
        client_type=Application.CLIENT_CONFIDENTIAL,
        authorization_grant_type=Application.GRANT_PASSWORD,
        name="Test App"
    )
    print("Application.GRANT_PASSWORD : ", Application.GRANT_PASSWORD)
    print(f"Client created: {created}. ID: {app.client_id}, Secret: {app.client_secret}")
    context.application = app


def before_all(context):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth.settings')
    django.setup()

    global server_process
    if server_process is None:
        server_process = subprocess.Popen(
            ["python", "start_server.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(5)


def after_all(context):
    global server_process
    if server_process:
        server_process.terminate()
        server_process.wait()