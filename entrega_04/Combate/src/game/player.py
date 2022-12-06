


class Player:
    def __init__(self, identifier: str):
        self.identifier = identifier
        self._turn = False
        self.winner = False
        self.filledBoard = False
        # self.lista_peca_pos: Position[self.pecas]

    def reset(self):
        pass

    def setTurn(self, turn: bool):
        self._turn = turn

    def isPlayerTurn(self):
        return self._turn

    
