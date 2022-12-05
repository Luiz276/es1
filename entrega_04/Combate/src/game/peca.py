from game.location import Location

class Peca:
    def __init__(self, power: int, location: Location, owner):
        self._poder = power
        self.location = location
        self.jogador_dono = owner

    def get_power(self):
        return self._poder
