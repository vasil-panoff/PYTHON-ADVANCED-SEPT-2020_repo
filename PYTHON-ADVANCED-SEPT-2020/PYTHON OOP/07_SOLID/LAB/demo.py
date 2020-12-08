class Parent:
    def __init__(self, name, age, eye_color='brown'):
        self.name = name
        self.age = age
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, name, age, gender, eye_color='brown'):
        self.gender = gender
        super().__init__(
            name=name,
            age=age,
            eye_color=eye_color,
        )

child = Child("Mihaela", 2, "F")
parent = Parent("Violeta", 35, "brown")
print(f'{parent.name} mother of')
print(child.name)
print(f'{child.age} years old')
print(f'{child.eye_color} eyes')
print(child.gender)