import unittest
import pandas
from quote_functions import get_json


class TestFileName(unittest.TestCase):
    def test_get_json(self):
        url = 'https://api.quotable.io/random'
        json = get_json(url)
        self.assertNotEqual(json, None)


if __name__ == '__main__':
    unittest.main()
