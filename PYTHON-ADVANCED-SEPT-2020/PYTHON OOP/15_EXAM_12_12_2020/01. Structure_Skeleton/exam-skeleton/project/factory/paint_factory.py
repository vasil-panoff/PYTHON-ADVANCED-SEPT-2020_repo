from project.factory.factory import Factory

class PaintFactory(Factory):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity

    def add_ingredient(self, ingredient_type: str, quantity: int):
        self.ingredient_type = ingredient_type
        self.quantity = quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        self.ingredient_type = ingredient_type
        self.quantity = quantity


