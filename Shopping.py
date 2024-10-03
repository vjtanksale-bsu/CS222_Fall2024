class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
class ShoppingCart:
    def __init__(self):
        self.products = []
    def AddProduct(self, product):
        self.products.append(product)
    def CalculateTotal(self):
        total = 0.0
        for p in self.products:
            total += p.price * p.quantity
        return total
    def RemoveProduct(self, name):
        self.products = [p for p in self.products if p.name != name]
    def UpdateQuantity(self, name, quantity):
        for p in self.products:
            if p.name == name:
                p.quantity = quantity
                break
    def ListProducts(self):
        return self.products