# AuthDRF
Tehran payment task

### PreInstallation requirements
in notification service create a config.ini file with below content :

    [ghasedak]
    api_key = <api-key>
    line_number = <phone-number>
    
    [grpc]
    host = 0.0.0.0
    port = 50051
    max_workers = 10

### Build
in auth directory run below command in ubuntu 24.04

    sudo docker compose build --no-cache

### Run
below run unittest and integration test then run the app 

    sudo docker compose up -d


### Get otp code
     curl -X POST http://localhost:8000/api/register/ -H "Content-Type: application/json" -d '{ "phone_number": <phone-number>}'
after read otp code in your mobile or logs of otp_service then :

    curl -X POST -u "<client-id>:<client-secret>" -d "grant_type=password&username=<username>&password=<password>&phone_number=<phone-number>&otp_code=<otp-code>" http://localhost:8000/oauth/token/

