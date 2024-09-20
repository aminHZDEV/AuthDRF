import subprocess
import time
import os


def start_server():
    server_process = subprocess.Popen(
        ["python", "manage.py", "runserver"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    time.sleep(5)

    return server_process


if __name__ == "__main__":
    start_server()
