from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory

class EasterShop:
    def __init__(self, name: str, chocolate_factory: ChocolateFactory, egg_factory: EggFactory, paint_factory: PaintFactory):
        self.chocolate_factory = ChocolateFactory
        self.egg_factory = EggFactory
        self.paint_factory = PaintFactory

    def add_chocolate_ingredient(self, type: str, quantity: int):
        pass

    def add_chocolate_ingredient(self, type: str, quantity: int): # adds an ingredient in the chocolate_factory
        pass

    def add_egg_ingredient(self, type: str, quantity: int): #adds an ingredient in the egg_factory
        pass

    def add_paint_ingredient(self, type: str, quantity: int): # adds an ingredient in the paint_factory
        pass

    def make_chocolate(self, recipe: str): # makes a chocolate in the chocolate_factory and add the chocolate to the storage
        pass

    def paint_egg(self, color: str, egg_type: str): #check the egg factory to see if you have at least one egg of the given egg type and check the paint factory if you have at least one piece of the given color
        pass