from abc import ABC, abstractmethod

class Instrument(ABC):
    def info(self):
        return self.name

    @abstractmethod
    def play(self):
        pass


class Guitar(Instrument):
    def play(self):
        pass

def play_instrument(person, instrument: Instrument):
    return instrument.play()