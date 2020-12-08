class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expences = 0

    @property
    def expences(self):
        return self.expences

    @expences.setter
    def expences(self, val):
        if val < 0:
            raise ValueError('Expenses cannot be negative')
        self.expences = val
    def calculate_expences(self, *args):
        pass

