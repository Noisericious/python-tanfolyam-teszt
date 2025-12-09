import unittest

from egységtesztek.div import divide


class TestDiv(unittest.TestCase):

    def test_divide_valid(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "b can't be zero")


if __name__ == '__main__':
    unittest.main()
