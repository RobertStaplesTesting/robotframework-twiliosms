from twilio.rest import Client

class Twiliosms(object):
    """A Library used to send and recieve data from twilio"""
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
            self._accid = 0
            self._token = 0

    def __convert_message_to_dict__(self, message):
        messageDict = {
            "account_sid":message.account_sid,
            "api_version": message.api_version,
            "body": message.body,
            "date_created": message.date_created,
            "date_sent": message.date_sent,
            "date_updated": message.date_updated,
            "direction": message.direction,
            "error_code": message.error_code,
            "error_message": message.error_message,
            "from": message.from_,
            "messaging_service_sid": message.messaging_service_sid,
            "num_media": message.num_media,
            "num_segments": message.num_segments,
            "price": message.price,
            "price_unit": message.price_unit,
            "sid": message.sid,
            "status": message.status,
            "subresource_uris": message.subresource_uris,
            "to": message.to,
            "uri": message.uri
        }
        return messageDict

    def create_session(self,
                        account_sid,
                        auth_token):
        """Creates a Session. taking in your twilio ``account_sid`` and *auth_token*"""
        self._accid = account_sid
        self._token = auth_token

    def send_message(self,
                    phone_to,
                    phone_from=None,
                    messaging_service_sid=None,
                    body=None,
                    media_url=None,
                    **kwargs
                    ):
        """Sends message from your Twilio Account."""
        if phone_from == None and messaging_service_sid == None:
            raise ValueError('either phone_from or messaging_service_sid must have value')
        elif body == None and media_url == None:
            raise ValueError('either body or media_url must have value')

        client = Client(self._accid, self._token)

        message = client.messages.create(
                                body=body,
                                from_=phone_from,
                                to=phone_to
                 )
        return message

    def get_message(self, sid):
        """uses ``sid`` to get matching message. returns as a dictionary"""
        client = Client(self._accid, self._token)
        message = client.messages.get(sid).fetch()

        messageDict = self.__convert_message_to_dict__(message)

        return messageDict

    def message_list(self, limit=20):
        """gets a list of messages with a limit of ``limit``. returns as a list of dictionaries"""
        client = Client(self._accid, self._token)

        messages = client.messages.list(limit=limit)
        messageslist = []
        for record in messages:
            messageslist.append(self.__convert_message_to_dict__(record))

        return messageslist

        
