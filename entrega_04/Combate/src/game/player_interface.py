from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from dog.dog_player_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from game.tabuleiro import Tabuleiro
from game.player import Player
from game.location import Location
from game.position import Position


class PlayerInterface(DogPlayerInterface):
    def __init__(self, tabuleiro: Tabuleiro):
        self.main_window = Tk()  # instanciar Tk (que implementa a janela)
        self.turnMessage = StringVar(None)
        self.turnMessage.set("Partida não iniciada.")
        self.tabuleiro = tabuleiro
        self.tablePieces = [[StringVar(None) for x in range(10)] for y in range(10)]
        self.fill_main_window()  # preenchimento da janela
        self.player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        
        self.tabuleiro.setCurrentPlayer(Player(identifier=self.player_name))

        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(self.player_name, self)
        messagebox.showinfo(message=message)
        self.main_window.mainloop()  # abrir a janela
        #root.option_add('*tearOff', FALSE)
    
    def fill_main_window(self):
        # Título, ícone, dimensionamento e fundo da janela
        self.main_window.title("COMBATE")
        #self.main_window.iconbitmap("images/icon.ico")
        self.main_window.geometry("720x720")
        self.main_window.resizable(False, False)
        self.main_window["bg"]="dark olive green"
        # Criação de 2 frames e organização da janela em um grid de 2 linhas e 1 coluna,
        # sendo que table_frame ocupa a linha superior e message_frame, a inferior
        self.table_frame = Frame(self.main_window, padx=100, pady=25, bg="dark olive green")
        self.table_frame.grid(row=0 , column=0)
        self.message_frame = Frame(self.main_window, padx=0, pady=10, bg="dark olive green")
        self.message_frame.grid(row=1 , column=0)
        # Definição de 2 imagens para o preenchimento inicial
        self.an_image = PhotoImage(file="./image/gray_square.png") #pyimage1
        # Preenchimento de table_frame com 21 imagens iguais, organizadas em 3 linhas e 7 colunas
        self.board_view=[]
        for y in range(10):
            a_column = []  # column
            for x in range(10):
                aLabel = Label(self.table_frame, bd = 0, image=self.an_image)
                self.tabuleiro.positions[x][y] = Position(coord_x=x, coord_y=y)
                aLabel.grid(row=x, column=y)
                Label(self.table_frame, textvariable=self.tablePieces[x][y], bg="white").grid(row=x, column=y)
                aLabel.bind("<Button-1>", lambda event, a_line=x, a_column=y: self.click(event, a_line, a_column))
                a_column.append(aLabel)
            self.board_view.append(a_column)
        #preenchimento de message_frame com 1 imagem com logo (label) e 1 label com texto,
        # organizadas em 1 linha e 2 colunas
        #self.logo_label = Label(self.message_frame, bd = 0, image=self.logo)
        #self.logo_label.grid(row=0, column=0)
        #self.menubar.option_add('*tearOff', FALSE),
        self.message_label = Label(self.message_frame, bg="dark olive green", text='COMBATE', font="arial 30")
        self.turnMessageLabel = Label(self.message_frame, bg="dark olive green", textvariable=self.turnMessage, font="arial 20")
        self.message_label.grid(row=0, column=1)
        self.turnMessageLabel.grid(row=1, column=1)
        self.menubar = Menu(self.main_window)
        self.menubar.option_add('*tearOff', FALSE)
        self.main_window['menu'] = self.menubar
        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.menu_file.add_command(label='Iniciar jogo', command = self.start_match)
        self.menu_file.add_command(label='Restaurar estado inicial', command = self.reset_game)

    def start_match(self):
        start_status = self.dog_server_interface.start_match(2)
        message = start_status.get_message()
        messagebox.showinfo(message=message)
        if (len(start_status.players) > 1):
            self.tabuleiro.currentPlayer.setTurn(True)
            self.turnMessage.set("É o seu turno.")
    
    def reset_game(self):
        print('start_game')

    def toggleTurn(self):
        self.tabuleiro.toggleTurn()
        self.turnMessage.set("É o seu turno." if self.tabuleiro.currentPlayer.isPlayerTurn() else "Não é o seu turno.")
    
    def receive_start(self, start_status):
        message = start_status.get_message()
        messagebox.showinfo(message=message)
        self.turnMessage.set("Não é o seu turno.")

    def receive_move(self, a_move):
        match a_move["match_status"]:
            case "toggle_turn":
                self.toggleTurn()
            case "new_piece":
                self.tabuleiro.insertPiece(line=a_move["line"], column=a_move["column"])
                self.tablePieces[a_move["line"]][a_move["column"]].set(a_move["power"])
            case _:
                pass
        print("recebeu movimento" + str(a_move))

    def click(self, event, line, column):
        if (self.tabuleiro.currentPlayer.isPlayerTurn()):
            if (not self.tabuleiro.currentPlayer.filledBoard):
                if (self.tabuleiro.currentPiece < 40):
                    newPiecePower = self.tabuleiro.insertPiece(line=line, column=column)
                    self.tablePieces[line][column].set(newPiecePower)
                    self.dog_server_interface.send_move({"match_status": "new_piece", "line": 10 - line - 1, "column": column, "power": newPiecePower})
                else:
                    self.tabuleiro.currentPlayer.filledBoard = True
                    self.toggleTurn()
                    self.dog_server_interface.send_move({"match_status": "toggle_turn"})
                    print("TROCOU O TURNO")
            else:
                print("tabuleiro do jogador " + self.tabuleiro.currentPlayer.identifier + " já preenchido")
        else:
            print("não é o turno do jogador " + self.tabuleiro.currentPlayer.identifier)
        print('CLICK', line, column)
