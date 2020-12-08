from project.rooms.room import Room
from project.aplliances.appliance import TV
from project.aplliances.appliance import Fridge
from project.aplliances.appliance import Laptop


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float ):
        super().__init__(family_name, budget = salary_one + salary_two, members_count = 2)
        self.room_cost = 20
        self.calculate_expenses([TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()])

