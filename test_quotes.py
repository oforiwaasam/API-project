import unittest
from einstein import get_json


class TestFileName(unittest.TestCase):
    def test_function1(self):
        url = 'https://api.quotable.io/random'
        json = get_json(url)
        self.assertNotEqual(json, None)


if __name__ == '__main__':
    unittest.main()
