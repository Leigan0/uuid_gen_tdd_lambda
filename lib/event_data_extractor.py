from urlparse import parse_qs
import re 

class EventDataExtractor:
    def __init__(self,event):
        self.event = event
    
    def get_data(self):
        return self.get_args()
    
    def get_args(self):
        body = body = parse_qs(self.event['body'])
        try:
            text = body['text']
            params = text[0].split()
        except KeyError as error:
            print('Body missing {} key'.format(error))
            raise
        
        try:
            values = {
                "token": body['token'][0],
                "pattern": re.sub('\.$', '', params[0]),
                "systemCode": params[1],
                "email": params[2]
                }
        except IndexError as error:
            print(error)
            print("A mandatory field is missing")
            raise

        return values
