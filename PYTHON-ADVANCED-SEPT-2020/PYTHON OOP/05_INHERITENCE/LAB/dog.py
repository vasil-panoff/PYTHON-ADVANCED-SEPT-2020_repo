class Animal:
    def eat(self):
        return 'eating...'

class Dog(Animal):
    def bark(self):
        return 'barking...'

    def dog(self):
        return 'Dog'


dog = Dog()
print(dog.dog())
print(dog.eat())
print(dog.bark())
