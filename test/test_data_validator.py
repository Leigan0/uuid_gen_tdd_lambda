import unittest
from lib.data_validator import DataValidator

class EventDataExtractorTestSpec(unittest.TestCase):
    def setUp(self):
        self.DataValidator = DataValidator()

    def test_token_value_is_valid(self):
        self.assertTrue(self.DataValidator())