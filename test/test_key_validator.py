import unittest
from lib.key_validator import KeyValidator


mock_event = {
    'resource': '/getgraphiteuuid',
    'path': '/getgraphiteuuid',
    'httpMethod': 'POST',
    'headers': {
    },
    'queryStringParameters': None,
    'pathParameters': None,
    'stageVariables': None,
    'requestContext': {
    },
    'body': 'token=123345&team_id=testTeam&team_domain=financialtimes&channel_id=12**12**&channel_name=directmessage&user_id=testUser**&user_name=test_user&command=%2Fgraphiteuuid&text=datatechnology.etldashboard+etl-dashboard+data.platform%40ft.com&response_url=https%3A%2F%2Fhooks.slack.com',
    'isBase64Encoded': False
    }

class KeyValidatorTestSpec(unittest.TestCase):

    def setUp(self):
        self.keyValidator = KeyValidator(mock_event)

    def test_it_extracts_body_from_request(self):
        self.assertEqual(self.keyValidator.get_body(), 'token=123345&team_id=testTeam&team_domain=financialtimes&channel_id=12**12**&channel_name=directmessage&user_id=testUser**&user_name=test_user&command=%2Fgraphiteuuid&text=datatechnology.etldashboard+etl-dashboard+data.platform%40ft.com&response_url=https%3A%2F%2Fhooks.slack.com')
