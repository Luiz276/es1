from game.player_interface import *
from game.tabuleiro import Tabuleiro


def main():
    tabuleiro = Tabuleiro()
    player_interface = PlayerInterface(tabuleiro=tabuleiro)


if __name__ == "__main__":
    main()
