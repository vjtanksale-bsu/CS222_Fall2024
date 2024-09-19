import unittest

from ListUtils import RemoveDuplicates

class TestListUtils(unittest.TestCase):
    def test_RemoveDuplicates(self):
        self.assertEqual(RemoveDuplicates([1,2,2,3,4,4,4]),[1,2,3,4])
        self.assertEqual(RemoveDuplicates([]),[])
        self.assertEqual(RemoveDuplicates([1,2,3]),[1,2,3])
if __name__ == '__main__':
    unittest.main()
