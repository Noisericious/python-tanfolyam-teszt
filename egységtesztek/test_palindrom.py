import unittest

from egységtesztek.palindrom import is_palindrom


class TestPalindrom(unittest.TestCase):
    def test_palindrom_true(self):
        self.assertTrue(is_palindrom("legel"))

    def test_palindrom_false(self):
        self.assertFalse(is_palindrom("valami"))

if __name__ == '__main__':
    unittest.main()
