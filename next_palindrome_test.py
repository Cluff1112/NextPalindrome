import unittest

from next_palindrome import next_palindrome


class MyTestCase(unittest.TestCase):
    def test_basic_odd(self):
        self.assertEqual(next_palindrome(1), 2)
        self.assertEqual(next_palindrome(121), 131)
        self.assertEqual(next_palindrome(120), 121)
        self.assertEqual(next_palindrome(192), 202)
        self.assertEqual(next_palindrome(12345), 12421)

    def test_basic_even(self):
        self.assertEqual(next_palindrome(11), 22)
        self.assertEqual(next_palindrome(1222), 1331)
        self.assertEqual(next_palindrome(1221), 1331)
        self.assertEqual(next_palindrome(1220), 1221)

    def test_boundary_odd(self):
        self.assertEqual(next_palindrome(9), 11)
        self.assertEqual(next_palindrome(999), 1001)
        self.assertEqual(next_palindrome(99999), 100001)

    def test_boundary_even(self):
        self.assertEqual(next_palindrome(99), 101)
        self.assertEqual(next_palindrome(9999), 10001)
        self.assertEqual(next_palindrome(3 ** 39), 4052555153515552504)


if __name__ == '__main__':
    unittest.main()
