import unittest
from project.spaceship.spaceship import Spaceship

class SpaceShipTest(unittest.TestCase):
    def setUp(self):
        self.spaceship = Spaceship("Vasil", 5)

    def add(self, astronaut_name: str):
        result = len(self.astronauts) == self.capacity
        expected_result = "Added astronaut {}"
        self.assertEqual(result, expected_result)

    def remove(self):
        result = self.astronaut_name not in self.astronauts
        expected_result = "Removed {}"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()