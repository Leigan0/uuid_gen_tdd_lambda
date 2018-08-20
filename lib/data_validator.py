import os
from botocore.vendored import requests

class DataValidator:
    def __init__(self,data):
        self.data = data
    
    def validToken(self):
        if self.data['token'] != os.environ["SLACK_TOKEN"]:
            raise Exception("Bad Request, Slack token invalid")
        return True 
    
    def validSystemCode(self):
        print(self.data)
        systemCode = self.data['systemCode']
        print(systemCode)
        url = 'https://cmdb.in.ft.com/v3/items/system/{}'.format(systemCode)
        headers = {'x-api-key': os.environ['CMDB_API_KEY']}
        r = requests.get(url, headers=headers)
        if (r.status_code) != 200:
            raise Exception("Bad Request, SystemCode invalid")
        return True
