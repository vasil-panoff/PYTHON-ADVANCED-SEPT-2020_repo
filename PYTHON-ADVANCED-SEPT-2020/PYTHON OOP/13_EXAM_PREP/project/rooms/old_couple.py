from project.rooms.room import Room
from project.appliances.appliance import TV
from project.appliances.appliance import Fridge
from project.appliances.appliance import Stove

class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float ):
        super().__init__(family_name, budget = pension_one + pension_two, members_count = 2)
        self.room_cost = 15
        self.calculate_expenses([TV(), Fridge(), Stove(), TV(), Fridge(), Stove()])

