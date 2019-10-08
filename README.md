# robotframework-twiliosms
Robot Framework SMS Verification Test Library using Twilio SMS API

Please see [Keyword Library](https://robertstaplestesting.github.io/robotframework-twiliosms/Twiliosms.html) for current functionality

## Running the tests from docker 
Set environment variables using `.env.example` template.
```
acc_sid=your account_sid
auth_token=your_authtoken
```

```
docker stop myfirstdockertest
docker container rm myfirstdockertest
docker build -t myfirstdockertest .
docker run --name myfirstdockertest -td -v ${PWD} myfirstdockertest
docker exec -t myfirstdockertest robot robot/test/test.robot
```

## Creating keyword library
`python3 -m robot.libdoc src/Twiliosms.py docs/Twiliosms.html`