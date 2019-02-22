"""
Module creates a test case for get_status_code()
"""
import unittest
from programming_lang import get_status_code

class ProgrammingLangTestCase(unittest.TestCase):
    """
    Tests for 'programming_lang.py'.
    The methods should start with "test_" so they can run automatically
    """

    def test_status_code(self):
        """status code is 200 when the api call is successful"""
        formatted_status_code = get_status_code('python')
        self.assertEqual(formatted_status_code, 200) #compares the test result with the result expected

unittest.main() #runs the tests in this file
