from math import sqrt


class Point:
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    def set_x(self, new_x: int) -> None:
        self.x = new_x

    def set_y(self, new_y: int) -> None:
        self.y = new_y

    def distance(self, other_x, other_y) -> float:
        dist = sqrt((self.x - other_x) ** 2 + (self.y - other_y) ** 2)
        return dist


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))