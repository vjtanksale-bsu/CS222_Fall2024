import unittest
from Shopping import ShoppingCart, Product

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        product = Product("Apple", 1.50, 3)
        self.cart.AddProduct(product)
    def test_AddProduct(self):
        self.assertEqual(self.cart.products[0].name, "Apple")
    def test_RemoveProduct(self):
        self.cart.RemoveProduct("Apple")
        self.assertNotIn("Apple", self.cart.products)
    def test_UpdateQuantity(self):
        self.cart.UpdateQuantity("Apple", 5)
        self.assertEqual(self.cart.products[0].quantity, 5)
    def test_CalculateTotal(self):
        self.cart.AddProduct(Product("Banana", 0.50, 6))
        self.assertEqual(self.cart.CalculateTotal(), 7.50)
    def test_ListProducts(self):
        self.cart.AddProduct(Product("Banana", 0.50, 6))
        self.assertEqual(len(self.cart.ListProducts()), 2)
if __name__ == '__main__':
    unittest.main()