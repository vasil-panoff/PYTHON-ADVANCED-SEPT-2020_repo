class Vasso:
    def __init__(self):
        self.__a = 'Vasil Panov'

    @property
    def a(self):
        return self.__a

    def set_a(self, value):
        self.__a = value

vasso = Vasso()
vasso.set_a('Vasil Stoykov Panov')
print(vasso.a)