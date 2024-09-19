FROM python:3.12.4-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get install -y g++ make && apt-get clean


RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 50051

CMD ["python", "otp.py"]