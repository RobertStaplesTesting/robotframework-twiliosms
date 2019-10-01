# robotframework-twiliosms
Robot Framework SMS Verification Test Library using Twilio SMS API

Please see doc/Twiliosms.html for current functionality

## Running the tests from docker 
```docker stop myfirstdockertest
docker container rm myfirstdockertest
docker build -t myfirstdockertest .
docker run --name myfirstdockertest -td -v ${PWD} myfirstdockertest
docker exec -t myfirstdockertest robot robot/test/test.robot```

## Creating keyword library
`python3 -m robot.libdoc src/Twiliosms.py doc/Twiliosms.html`