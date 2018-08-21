import os
import re
from botocore.vendored import requests

class DataValidator:
    def __init__(self,data):
        self.data = data
    
    def isDataValid(self):
        return self.validToken() and self.validPattern() and self.validSystemCode()
    
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
    
    def validPattern(self):
        pattern = self.data['pattern']
        if ("--" in pattern or pattern.startswith("-") or pattern.endswith("-") or pattern.startswith("_")):
            raise Exception("Bad request, pattern does not pass validation")
        elif not bool(re.match("^[A-Za-z0-9.\-_]+$", pattern)):
            raise Exception("Bad request, pattern does not pass validation")
        return True

