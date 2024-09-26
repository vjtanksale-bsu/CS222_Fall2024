from maxmin import MaxMin
import unittest
class TestMaxMin(unittest.TestCase):
    def test_MaxMin(self):
        self.assertEqual(MaxMin([1,2,3,4,5]), (5,1))
if __name__ == '__main__':
    unittest.main()