from game.peca import Peca
from game.location import Location


class Player:
    def __init__(self, identifier: str):
        self.identifier = identifier
        self._turn = False
        self.winner = False
        self.pieces = []
        self.currentPiece = 0
        self.fillingBoard = False
        # self.lista_peca_pos: Position[self.pecas]

    def reset(self):
        pass

    def setTurn(self, turn: bool):
        self._turn = turn

    def isPlayerTurn(self):
        return self._turn

    def placePiece(self, location: Location):
        if self.currentPiece < 6:
            # minha_terrestre x
            self.pieces.append(Peca(0, location, self))
        elif self.currentPiece < 7:
            # prisioneiro x
            self.pieces.append(Peca(-1, location, self))
        elif self.currentPiece < 8:
            # general 10
            self.pieces.append(Peca(10, location, self))
        elif self.currentPiece < 9:
            # coronel 9
            self.pieces.append(Peca(9, location, self))
        elif self.currentPiece < 11:
            # major 8
            self.pieces.append(Peca(8, location, self))
        elif self.currentPiece < 14:
            # capitao 7
            self.pieces.append(Peca(7, location, self))
        elif self.currentPiece < 18:
            # tenente 6
            self.pieces.append(Peca(6, location, self))
        elif self.currentPiece < 22:
            # subtenente 5
            self.pieces.append(Peca(5, location, self))
        elif self.currentPiece < 26:
            # sargento 4
            self.pieces.append(Peca(4, location, self))
        elif self.currentPiece < 31:
            # cabo 3
            self.pieces.append(Peca(3, location, self))
        elif self.currentPiece < 39:
            # soldado 2
            self.pieces.append(Peca(2, location, self))
        else:
            # agente_secreto 1
            self.pieces.append(Peca(1, location, self))

        self.currentPiece += 1
