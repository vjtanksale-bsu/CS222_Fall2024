import unittest
from shoppingcart import ShoppingCart, Item
class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
    def test_AddItem(self):
        item = Item("Laptop", 1500.00)
        self.cart.AddItem(item)
        self.assertIn(item, self.cart.items)
    def test_RemoveItem(self):
        item = Item("Laptop", 1500.00)
        self.cart.AddItem(item)
        self.cart.RemoveItem(item)
        self.assertNotIn(item, self.cart.items)
    def test_TotalPrice(self):
        item0 = Item("Laptop", 1500.00)
        item1 = Item("Printer", 300.00)
        self.cart.AddItem(item0)
        self.cart.AddItem(item1)
        self.assertEqual(self.cart.TotalPrice(), 1800.00)
if __name__ == '__main__':
    unittest.main()