from project.rooms.room import Room
from project.aplliances.appliance import TV
from project.aplliances.appliance import Fridge
from project.aplliances.appliance import Laptop


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children: str ):
        super().__init__(family_name, budget = salary_one + salary_two, 2 + len(children))
        self.room_cost = 30

        self.appliances = [[TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]]
        for _ in range(len(children)):
            self.appliances.append([TV(), Fridge(), Laptop(), ])

        self.calculate(*self.appliances)


