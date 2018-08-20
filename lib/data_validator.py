import os 

class DataValidator:
    def __init__(self,data):
        self.data = data
    
    def validToken(self):
        if self.data['token'] != os.environ["SLACK_TOKEN"]:
            raise Exception("Bad Request, Slack token invalid")
        return True 