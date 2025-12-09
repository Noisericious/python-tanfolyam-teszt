import unittest

from egységtesztek.számologép import add


class TestSzamologep(unittest.TestCase):

    def test_app_positive_number(self):
        self.assertEqual(add(2,3), 5)

    def test_app_negative_number(self):
        self.assertEqual(add(-2, -3), -5)

    def test_app_mixed_number(self):
        self.assertEqual(add(-2, 3), 1)

    def test_app_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)


if __name__ == '__main__':
    unittest.main()

