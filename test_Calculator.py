import unittest
from Calculator import Calculator
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.c = Calculator()
    def test_add(self):
        self.assertEqual(self.c.add(2, 3), 5)
    def test_subtract(self):
        self.assertEqual(self.c.subtract(2,3), -1)
    def test_multiply(self):
        self.assertEqual(self.c.multiply(2, 3), 6)
    def test_divide(self):
        self.assertEqual(self.c.divide(10,2), 5) 
    def test_divideByZero(self):
        with self.assertRaises(ValueError):
            self.c.divide(10, 0)
if __name__ == '__main__':
    unittest.main()