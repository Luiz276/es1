from game.position import *
from game.player import Player


class Peca:
    def __init__(self):
        self.poder: int
        self.position: Position
        self.jogador_dono: Player

    def get_power(self):
        pass
