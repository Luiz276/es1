from position import Position
from player import Player

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
        self.positions: Position[10][10]
        self.local_player: Player
        self.remote_player: Player
        self.match_status = 1
