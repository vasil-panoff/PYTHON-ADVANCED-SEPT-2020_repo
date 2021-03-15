from project.factory.factory import Factory

class ChocolateFactory(Factory):
    recipes: dict = {}
    products: dict = {}

    
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity

    def add_ingredient(self, ingredient_type: str, quantity: int):
        self.ingredient_type = ingredient_type
        self.quantity = quantity


    def remove_ingredient(ingredient_type: str, quantity: int):
        self.ingredient_type = ingredient_type
        self.quantity = quantity

