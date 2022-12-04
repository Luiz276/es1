from position import Position


class Player:
    def __init__(self):
        self.identifier: str
        self.turn = False
        self.winner = False
        self.pecas = 40
        self.lista_peca_pos = Position[self.pecas]

    def initialize(self, symbol: int, identifier: str):
        pass

    def reset(self):
        pass

    def toggle_turn(self):
        pass
