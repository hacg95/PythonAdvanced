from unittest import TestCase
import unittest
from palindrome import is_palindrome
from prime import is_prime


class TestingFunctions(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("Ana"), True)
        self.assertEqual(is_palindrome("Harold"), False)
        self.assertEqual(is_palindrome("Ligar es ser agil"), True)
        self.assertEqual(is_palindrome("Esto no es un palindromo"), False)

    def test_is_prime(self):
        self.assertEqual(is_prime(17), True)
        self.assertEqual(is_prime(73), True)
        self.assertEqual(is_prime(15), False)
        self.assertEqual(is_prime(55), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)