class Human:
    def __init__(self, name):
        self.name = name

    def say_my_name(self):
        return self.name

class Communist(Human):
    def say_my_name(self):
        res = super().say_my_name()
        return f"Таварищ {res}"
vasil = Communist('Панов')
print(vasil.say_my_name())