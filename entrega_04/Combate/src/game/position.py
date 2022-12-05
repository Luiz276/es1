from game.player import Player
from game.peca import Peca


class Position:
    def __init__(self):
        self.coord_x: int
        self.coord_y: int
        self.ocupado = False
        self.ocupante: Peca

    def getOccupant(self):
        pass

    def belongsTo(self, pos_peca, player: Player):
        pass

    def getOcupado(self, pos_peca):
        pass

# TODO verificar a disparidade de piece e peca nos diagramas