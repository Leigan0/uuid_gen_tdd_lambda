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
    'body': 'token=123345&team_id=testTeam&team_domain=financialtimes&channel_id=12**12**&channel_name=directmessage&user_id=testUser**&user_name=test_user&command=%2Fgraphiteuuid&text=datatechnology.etldashboard+citrixxendesktop+test.email%40ft.com&response_url=https%3A%2F%2Fhooks.slack.com',
    'isBase64Encoded': False
    }

class KeyValidatorTestSpec(unittest.TestCase):

    def setUp(self):
        self.keyValidator = KeyValidator(mock_event)

    def test_it_extracts_token_patten_systemCode_email_from_request(self):
        self.assertEqual(self.keyValidator.get_keys(), { "token": "123345","pattern":"datatechnology.etldashboard", "systemCode":"citrixxendesktop", "email":"test.email@ft.com"})

    def test_it_raises_error_if_not_passed_test_key_within_body(self):
        mock_event['body'] = 'token=123345'
        keyValidator = KeyValidator(mock_event)
        with self.assertRaises(KeyError) as context:
            keyValidator.get_keys()
        self.assertTrue('text' in context.exception)
        
    def test_it_raises_error_if_not_passed_test_three_arguments_within_text_key(self):
        mock_event['body'] = 'token=123345&text=pattern+systemCode'
        keyValidator = KeyValidator(mock_event)
        with self.assertRaises(IndexError) as context:
            keyValidator.get_keys()
        self.assertTrue('list index out of range' in context.exception)

