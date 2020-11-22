class Mammal:
    __kingdom = 'animals'

    def __init__(self, name, kind, sound):
        self.name = name
        self.kind = kind
        self.sound = sound

    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f'{self.name} is of type {self.kind}'


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
