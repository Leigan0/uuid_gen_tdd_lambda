from lib.lambda_handler import handle

import unittest
import mock 

class EventDataExtractorTestSpec(unittest.TestCase):

    @mock.patch('lib.lambda_handler.EventDataExtractor.get_data')
    def test_it_returns_data_from_event_extractor(self, mockEventExtractor):
        handle("event","context")
        self.assertTrue(mockEventExtractor.called)
