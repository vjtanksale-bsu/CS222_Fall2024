from stack import Stack
import unittest
class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.items, [1, 2])
    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
    def test_isEmpty(self):
        self.assertTrue(self.stack.isEmpty())
if __name__ == '__main__':
    unittest.main()