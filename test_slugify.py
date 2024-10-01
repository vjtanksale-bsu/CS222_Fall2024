import unittest
from Slugify import slugify

class TestSlugify(unittest.TestCase):
    def test_Basic(self):
        self.assertEqual(slugify("Hello World"), "hello-world")
    def test_Punctuation(self):
        self.assertEqual(slugify("Python is the best!"), "python-is-the-best")
    def test_MultipleSpace(self):
        self.assertEqual(slugify("     Python      is    awesome"), "python-is-awesome")
    def test_Empty(self):
        self.assertEqual(slugify(""), "")
    def test_SpecialCharacters(self):
        self.assertEqual(slugify("@#%^"), "")
if __name__ =='__main__':
    unittest.main()