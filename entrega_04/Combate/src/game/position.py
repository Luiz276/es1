from game.player import Player
from game.peca import Peca


class Position:
    def __init__(self, coord_x: int, coord_y: int):
        self._coord_x = coord_x
        self._coord_y = coord_y
        self._ocupado = False
        self._ocupante: Peca

    def belongsTo(self, pos_peca, player: Player):
        pass

    def getCoords(self):
        return [self._coord_x, self._coord_y]

    def setOccupant(self, occupant: Peca):
        self._ocupante = occupant

    def getOccupant(self):
        pass

    def setOcupado(self, ocupado: bool):
        self._ocupado = ocupado

    def getOcupado(self, pos_peca):
        pass

# TODO verificar a disparidade de piece e peca nos diagramas