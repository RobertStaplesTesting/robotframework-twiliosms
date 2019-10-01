*** Settings ***
Library  ../src/Twiliosms.py

Documentation  https://www.twilio.com/docs/sms/api/message-resource

*** Variables ***
${ID}    AC50f9970b2a2544d64628eb4c6966462e
${AUTH}  3e165af44d64480bf93378e23cbf8d5b
${Body}  Hi there! This is an automated message from Robert Staples' Programable Twilio SMS library for the robot framework. please send him money.
${From}  +61480015691
${To}    +61421718105

*** Test Cases ***
Example that calls a Python keyword
    create session  ${ID}  ${AUTH}
    #${result}=  send message  ${From}  ${To}  ${Body}
    ${result}=  Message list
    Log  ${result}