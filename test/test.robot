*** Settings ***
Library  ../src/Twiliosms.py

Documentation  https://www.twilio.com/docs/sms/api/message-resource

*** Variables ***
${ID}    %{acc_sid}
${AUTH}  %{auth_token}
${Body}  Hi there! This is an automated message from Robert Staples' Programable Twilio SMS library for the robot framework. please send him money.
${from}  +61480015691
${to}    +61421718105

${ERR_NO_FROM_OR_MESS_SID}   ValueError: either phone_from or messaging_service_sid must have value
${ERR_NO_BODY_OR_MEDIA_URL}  ValueError: either body or media_url must have value
${ERR_NON_VALID_RETURN}      non-valid return_format
${SID_VALUE}  SM8eafb0f8c827457a9a90af3b2b5c53bd

*** Test Cases ***
Send messages
    [Documentation]  Integration testing for Send messages
    create session   ${ID}  ${AUTH}
    Run Keyword And Expect Error  ${ERR_NO_FROM_OR_MESS_SID}   send message  ${To}
    Run Keyword And Expect Error  ${ERR_NO_BODY_OR_MEDIA_URL}  send message  ${To}  phone_from=${from}

Fetch a message
    ${message}=  Get message  ${SID_VALUE}  result_format=messageinstance
    Should be equal  ${message.sid}  ${SID_VALUE}
    ${message}=  Get message  ${SID_VALUE}  result_format=dictionary
    Should be equal  ${message}[sid]  ${SID_VALUE}
    ${message}=  Get message  ${SID_VALUE}  result_format=MessageInstance
    Should be equal  ${message.sid}  ${SID_VALUE}
    ${message}=  Get message  ${SID_VALUE}  result_format=Dictionary
    Should be equal  ${message}[sid]  ${SID_VALUE}
    Run Keyword And Expect Error  ${ERR_NON_VALID_RETURN}  Get message  ${SID_VALUE}  result_format=nonresultformat
