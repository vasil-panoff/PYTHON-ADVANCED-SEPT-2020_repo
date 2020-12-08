from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, username, health):
        self.username = usernamed
        self.health = health

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Player's username cannot be an empty string.")
        self.username = value

        #TODO • card_repository: CardRepository - new card repository upon initialization.

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self.health = value

    @property
    def is_dead(self):
        return False if self.health > 0 else True
