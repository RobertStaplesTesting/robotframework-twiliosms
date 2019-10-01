FROM ubuntu:16.04
COPY . /robot

RUN apt-get update && apt-get install --quiet --assume-yes python3 python3-pip
RUN pip3 install --upgrade robotframework twilio