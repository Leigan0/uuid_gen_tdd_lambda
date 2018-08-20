import unittest
from lib.event_data_extractor import EventDataExtractor


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

class EventDataExtractorTestSpec(unittest.TestCase):

    def setUp(self):
        self.eventDataExtractor = EventDataExtractor(mock_event)

    def test_it_extracts_token_patten_systemCode_email_from_request(self):
        self.assertEqual(self.eventDataExtractor.get_data(), { "token": "123345","pattern":"datatechnology.etldashboard", "systemCode":"citrixxendesktop", "email":"test.email@ft.com"})

    def test_it_raises_error_if_not_passed_test_key_within_body(self):
        mock_event['body'] = 'token=123345'
        eventDataExtractor = EventDataExtractor(mock_event)
        with self.assertRaises(KeyError) as context:
            eventDataExtractor.get_data()
        self.assertTrue('text' in context.exception)
        
    def test_it_raises_error_if_not_passed_test_three_arguments_within_text_key(self):
        mock_event['body'] = 'token=123345&text=pattern+systemCode'
        eventDataExtractor = EventDataExtractor(mock_event)
        with self.assertRaises(IndexError) as context:
            eventDataExtractor.get_data()
        self.assertTrue('list index out of range' in context.exception)

