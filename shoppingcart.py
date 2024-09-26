class ShoppingCart:
    def __init__(self):
        self.items = []
    def AddItem(self, item):
        self.items.append(item)
    def RemoveItem(self, item):
        if item in self.items:
            self.items.remove(item)
    def TotalPrice(self):
        return sum(item.price for item in self.items)
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price