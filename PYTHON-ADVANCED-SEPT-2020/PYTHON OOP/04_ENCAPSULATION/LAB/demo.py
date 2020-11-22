class BankAccount:
    def __init__(self, id: int, pin: int, name: str):

        self.name = name     # public attribute
        self._id = id        # protected attribute
        self.__pin = pin     # private attribute

    def get_pin(self, __pin):       # getter
        return __pin

    def set_pin(self, __pin):  # setter
        self.__pin = pin


bank_account = BankAccount(101010101, 2486, "Vasil Panov")


class Person:
    def __init__(self, age=0):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            self.__age = 18
        else:
            self.__age = age


Vasil = Person(43)
Vasil.age = 42
print(Vasil.age)
