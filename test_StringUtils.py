import unittest
from StringUtils import IsPalindrome

class TestStringUtils(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(IsPalindrome("Racecar"))
        self.assertFalse(IsPalindrome("Hello"))
        self.assertTrue(IsPalindrome(""))
        self.assertTrue(IsPalindrome("A man a plan a canal Panama"))
if __name__ =='__main__':
    unittest.main()