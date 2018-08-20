from urlparse import parse_qs

class KeyValidator:
    def __init__(self,event):
        self.event = event
    
    def get_body(self):
        return self.event['body']
