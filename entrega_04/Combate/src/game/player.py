from game.position import *


class Player:
    def __init__(self, identifier: str):
        self.identifier = identifier
        self._turn = False
        self.winner = False
        self.pecas = 40
        self.lista_peca_pos: Position[self.pecas]

    # def initialize(self, identifier: str):
    #     self.identifier = identifier

    def reset(self):
        pass

    def toggle_turn(self):
        pass

    def isPlayerTurn(self):
        return self._turn
