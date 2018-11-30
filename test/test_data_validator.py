import unittest
import mock 
import os

from lib.data_validator import DataValidator
mock_data = { "token": "123345","pattern":"datatechnology.etldashboard", "systemCode":"citrixxendesktop", "email":"test.email@ft.com"}

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
         def __init__(self, statusCode):
            self.status_code = statusCode

            # should be biz ops
        
    if args[0] == 'https://cmdb.in.ft.com/v3/items/system/citrixxendesktop' and kwargs == {'headers': {'x-api-key': 'API_KEY'}}:
        return MockResponse(200)
        
    return MockResponse(404)

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
    
    @mock.patch.dict(os.environ,{'CMDB_API_KEY':'API_KEY'})
    @mock.patch('botocore.vendored.requests.get',side_effect=mocked_requests_get)
    def test_validSystemCode_sends_request_with_url_and_api_key(self,mockRequest):
        self.dataValidator.validSystemCode()
        mockRequest.assert_called_once_with("https://cmdb.in.ft.com/v3/items/system/citrixxendesktop",  headers={'x-api-key': 'API_KEY'})
        
    @mock.patch.dict(os.environ,{'CMDB_API_KEY':'API_KEY'})
    @mock.patch('botocore.vendored.requests.get',side_effect=mocked_requests_get)
    def test_validSystemCode_returns_true_when_valid(self, mockRequest):
        self.assertTrue(self.dataValidator.validSystemCode())
    
    @mock.patch.dict(os.environ,{'CMDB_API_KEY':'API_KEY'})
    @mock.patch('botocore.vendored.requests.get',side_effect=mocked_requests_get)
    def test_validSystemCode_raises_error_when_invalid_systemCode(self, mockRequest):
        mock_data_invalid_systemCode = { "token": "123345","pattern":"datatechnology.etldashboard", "systemCode":"invalidSystemCode", "email":"test.email@ft.com"}
        dataValidator = DataValidator(mock_data_invalid_systemCode)
        with self.assertRaises(Exception) as context:
            self.assertTrue(dataValidator.validSystemCode())
        self.assertEqual('Bad Request, SystemCode invalid',str(context.exception))
    
    @mock.patch.dict(os.environ,{'CMDB_API_KEY':'INVALID_KEY'})
    @mock.patch('botocore.vendored.requests.get',side_effect=mocked_requests_get)
    def test_validSystemCode_raises_error_when_invalid_API_KEY(self, mockRequest):
        with self.assertRaises(Exception) as context:
            self.assertTrue(self.dataValidator.validSystemCode())
        self.assertEqual('Bad Request, SystemCode invalid',str(context.exception))
    
    def test_validPattern_raises_error_with_invalid_start_end_pattern(self):
        mock_pattern = {"pattern": "--"}
        dataValidator = DataValidator(mock_pattern)
        with self.assertRaises(Exception) as context:
            dataValidator.validPattern()
        self.assertEqual('Bad request, pattern does not pass validation',str(context.exception))
        mock_pattern = {"pattern": "-pattern"}
        dataValidator = DataValidator(mock_pattern)
        with self.assertRaises(Exception) as context:
            dataValidator.validPattern()
        self.assertEqual('Bad request, pattern does not pass validation',str(context.exception))
        mock_pattern = {"pattern": "pattern-"}
        dataValidator = DataValidator(mock_pattern)
        with self.assertRaises(Exception) as context:
            dataValidator.validPattern()
        self.assertEqual('Bad request, pattern does not pass validation',str(context.exception))
        mock_pattern = {"pattern": "_pattern"}
        dataValidator = DataValidator(mock_pattern)
        with self.assertRaises(Exception) as context:
            dataValidator.validPattern()
        self.assertEqual('Bad request, pattern does not pass validation',str(context.exception))
    
    def test_validPattern_raises_error_with_non_alphanumeric_characters(self):
        mock_pattern = {"pattern": "ft.id*"}
        dataValidator = DataValidator(mock_pattern)
        with self.assertRaises(Exception) as context:
            dataValidator.validPattern()
        self.assertEqual('Bad request, pattern does not pass validation',str(context.exception))
    
        mock_pattern = {"pattern": "ft.id!"}
        dataValidator = DataValidator(mock_pattern)
        with self.assertRaises(Exception) as context:
            dataValidator.validPattern()
        self.assertEqual('Bad request, pattern does not pass validation',str(context.exception))
    
        mock_pattern = {"pattern": "ft.id@"}
        dataValidator = DataValidator(mock_pattern)
        with self.assertRaises(Exception) as context:
            dataValidator.validPattern()
        self.assertEqual('Bad request, pattern does not pass validation',str(context.exception))

    # @mock.patch.dict(os.environ,{'SLACK_TOKEN':'123345','CMDB_API_KEY':'API_KEY'})
    # @mock.patch('botocore.vendored.requests.get',side_effect=mocked_requests_get)
    # def test_isDataValid_returns_true_valid_data(self):
    #     self.assertTrue(self.dataValidator.isDataValid())
    






