import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.e = Employee("John", "Doe", 50000)
    def test_GiveRaise(self):
        self.e.GiveRaise(5000)
        self.assertEqual(self.e.salary, 55000)
        
if __name__ == '__main__':
    unittest.main()