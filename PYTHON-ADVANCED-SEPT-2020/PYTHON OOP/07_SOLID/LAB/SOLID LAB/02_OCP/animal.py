from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @abstractmethod
    def make_sound(self):
        pass

def animal_sound(animals: list[Animal]):
    for animal in animals:
        print(animal.make_sound())

class Cat(Animal):
    def make_sound(self):
        return 'meow'

class Dog(Animal):
    def make_sound(self):
        return 'woff-woff'

class Chicken(Animal):
    def make_sound(self):
        return 'chik-chirik'


animals = [Cat('cat'), Dog('dog'), Chicken('chicken')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни

