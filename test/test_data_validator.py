import unittest
import mock 
import os

from lib.data_validator import DataValidator
mock_data = { "token": "123345","pattern":"datatechnology.etldashboard", "systemCode":"citrixxendesktop", "email":"test.email@ft.com"}
class EventDataExtractorTestSpec(unittest.TestCase):
    def setUp(self):
        self.dataValidator = DataValidator(mock_data)

    @mock.patch.dict(os.environ,{'SLACK_TOKEN':'123345'})
    def test_validToken_returns_true_when_valid(self):
        self.assertTrue(self.dataValidator.validToken())
    
    @mock.patch.dict(os.environ,{'SLACK_TOKEN':'123345897'})
    def test_validToken_raises_exception_when_invalid(self):
        with self.assertRaises(Exception) as context:
            self.dataValidator.validToken()
        self.assertEqual('Bad Request, Slack token invalid',str(context.exception))