import unittest
from MathUtils import *

class TestMathUtils(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2,3),6)
        self.assertEqual(multiply(-2,5),-10)
        self.assertEqual(multiply(0,7),0)
        self.assertEqual(multiply(3.5, 2), 7.0)
    def test_factorial(self):
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)
    def test_isEven(self):
        self.assertTrue(IsEven(10))
        self.assertFalse(IsEven(5))
if __name__ =='__main__':
    unittest.main()