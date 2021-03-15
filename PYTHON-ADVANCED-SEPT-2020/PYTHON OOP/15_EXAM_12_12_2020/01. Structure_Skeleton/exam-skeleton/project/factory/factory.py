from abc import abstractmethod, ABC


class Factory(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def can_add(self, value: int):
        return self.value
