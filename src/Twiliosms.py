from twilio.rest import Client

class Twiliosms(object):
    """A Library used to send and recieve data from twilio
        all message can either be returned as a twilio messageInstance or a dictionary this is set with result_format"""
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
                    body=None,
                    messaging_service_sid=None,
                    media_url=None,
                    result_format='messagInstance',
                    **kwargs):
        """Sends message from your Twilio Account. 
        \n 
        \n``phone_from`` is optional if ``messaging_service_id`` is filled and vice vera.
        \n``media_url`` is optional if ``body`` is filled and vice vera.
            * ``status_callback``
            * ``application_sid``
            * ``max_price``
            * ``provide_feedback``
            * ``validity_period``
            * ``force_delivery``
            * ``smart_encoded``

            |${result}=|Send Message|#fakenum|#fakenum|Hello|
            |${result}=|Send Message|#fakenum|#fakenum|Hello|
            ``result_format`` can either be dictionary or a messageInstance."""

        if phone_from == None and messaging_service_sid == None:
            raise ValueError('either phone_from or messaging_service_sid must have value')
        elif body == None and media_url == None:
            raise ValueError('either body or media_url must have value')

        client = Client(self._accid, self._token)

        message = client.messages.create(
                                body=body,
                                from_=phone_from,
                                to=phone_to,
                                media_url=media_url,
                                messaging_service_sid=messaging_service_sid,
                                status_callback=kwargs.values('status_callback'),
                                application_sid=kwargs.values('application_sid'),
                                max_price=kwargs.values('max_price'),
                                provide_feedback=kwargs.values('provide_feedback'),
                                validity_period=kwargs.values('validity_period'),
                                force_delivery=kwargs.values('force_delivery'),
                                smart_encoded=kwargs.values('smart_encoded')
                            )
        return message

    def get_message(self, 
                    sid,
                    result_format='messageInstance'):
        """uses ``sid`` to get matching message. ``result_format is ``"""
    
        client = Client(self._accid, self._token)
        message = client.messages.get(sid).fetch()

        if result_format.lower() == 'messageinstance':
            return message
        elif result_format.lower() == 'dictionary':
            message = self.__convert_message_to_dict__(message)
            return message
        else:
            raise Exception('non-valid return_format')

    def message_list(self,
                     limit=20,
                     result_format='messagInstance',
                     **kwargs):
        """gets a list of messages with a limit of ``limit``. returns as a list of dictionaries"""
    
        client = Client(self._accid, self._token)

        messages = client.messages.list(limit=limit)
        messageslist = []
        for record in messages:
            messageslist.append(self.__convert_message_to_dict__(record))

        return messageslist

        
