from urlparse import parse_qs
import re 

class KeyValidator:
    def __init__(self,event):
        self.event = event
    
    def get_keys(self):
        return self.get_args()
    
    def get_args(self):
        body = body = parse_qs(self.event['body'])
        try:
            text = body['text']
            values = text[0].split()
        except KeyError as error:
            print('Body missing {} key'.format(error))
            raise
        
        try:
            keys = {
                "token": body['token'][0],
                "pattern": re.sub('\.$', '', values[0]),
                "systemCode": values[1],
                "email": values[2]
                }
        except IndexError as error:
            print(error)
            print("A mandatory field is missing")
            raise

        return keys
