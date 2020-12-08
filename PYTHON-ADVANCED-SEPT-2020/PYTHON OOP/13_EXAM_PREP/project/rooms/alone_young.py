from project.rooms.room import Room
from project.appliances.appliance import TV
from project.appliances.appliance import Fridge
from project.appliances.appliance import Stove

class AloneYoung(Room):
    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, budget = salary, members_count = 1)
        self.room_cost = 10
        self.calculate_expenses([TV()])


