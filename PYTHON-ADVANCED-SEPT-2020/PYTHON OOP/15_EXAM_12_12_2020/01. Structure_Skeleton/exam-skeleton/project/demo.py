class Store:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    def additem(self, item, price):
        self.items[str(item)] = float(price)

    def delitem(self, item):
        del self.items[str(item)]

    def displayinventory(self):
        return self.items