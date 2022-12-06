from game.position import Position
from game.player import Player
from game.peca import Peca
from game.location import Location

'''
# Tabuleiro match_status
#1 - Sem partida (estado inicial)
#2 - Partida finalizada (jogo com vencedor - sem jogo empatado)
#3 - Seu turno, partida em andamento e sem movimento ocorrendo
#4 - Seu turno, partida em andamento e com movimento ocorrendo
#5 - Não é seu turno
#6 - Partida abandonada pelo oponente
'''


class Tabuleiro:

    def __init__(self):
        self.positions = [[0 for x in range(10)] for y in range(10)]
        self.currentPlayer: Player
        self.match_status = 1
        self.currentPiece = 0

    def setCurrentPlayer(self, player: Player):
        self.currentPlayer = player

    def toggleTurn(self):
        self.currentPlayer.setTurn(not self.currentPlayer.isPlayerTurn())

    def insertPiece(self, line: int, column: int):
        currentPower = 0
        if self.currentPiece < 6:
            # minha_terrestre x
            currentPower = 0
            self.positions[line][column].setOccupant(Peca(0, Location(line = line, column = column), self.currentPlayer))
        elif self.currentPiece < 7:
            # prisioneiro x
            currentPower = -1
            self.positions[line][column].setOccupant(Peca(-1, Location(line = line, column = column), self.currentPlayer))
        elif self.currentPiece < 8:
            # general 10
            currentPower = 10
            self.positions[line][column].setOccupant(Peca(10, Location(line = line, column = column), self.currentPlayer))
        elif self.currentPiece < 9:
            # coronel 9
            currentPower = 9
            self.positions[line][column].setOccupant(Peca(9, Location(line = line, column = column), self.currentPlayer))
        elif self.currentPiece < 11:
            # major 8
            currentPower = 8
            self.positions[line][column].setOccupant(Peca(8, Location(line = line, column = column), self.currentPlayer))
        elif self.currentPiece < 14:
            # capitao 7
            currentPower = 7
            self.positions[line][column].setOccupant(Peca(7, Location(line = line, column = column), self.currentPlayer))
        elif self.currentPiece < 18:
            # tenente 6
            currentPower = 6
            self.positions[line][column].setOccupant(Peca(6, Location(line = line, column = column), self.currentPlayer))
        elif self.currentPiece < 22:
            # subtenente 5
            currentPower = 5
            self.positions[line][column].setOccupant(Peca(5, Location(line = line, column = column), self.currentPlayer))
        elif self.currentPiece < 26:
            # sargento 4
            currentPower = 4
            self.positions[line][column].setOccupant(Peca(4, Location(line = line, column = column), self.currentPlayer))
        elif self.currentPiece < 31:
            # cabo 3
            currentPower = 3
            self.positions[line][column].setOccupant(Peca(3, Location(line = line, column = column), self.currentPlayer))
        elif self.currentPiece < 39:
            # soldado 2
            currentPower = 2
            self.positions[line][column].setOccupant(Peca(2, Location(line = line, column = column), self.currentPlayer))
        else:
            # agente_secreto 1
            currentPower = 1
            self.positions[line][column].setOccupant(Peca(1, Location(line = line, column = column), self.currentPlayer))

        self.currentPiece += 1
        
        return currentPower

    def setWinner(self):
        pass