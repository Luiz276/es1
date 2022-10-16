from tkinter import *

class PlayerInterface:
    def __init__(self):
        self.main_window = Tk() # instanciar Tk (que implementa a janela)
        self.fill_main_window() # preenchimento da janela
        self.main_window.mainloop() # abrir a janela
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
        self.an_image = PhotoImage(file="image/gray_square.png") #pyimage1
        # Preenchimento de table_frame com 21 imagens iguais, organizadas em 3 linhas e 7 colunas
        self.board_view=[]
        for y in range(10):
            a_column = [] # column
            for x in range(10):
                aLabel = Label(self.table_frame, bd = 0, image=self.an_image)
                aLabel.grid(row=x , column=y)
                aLabel.bind("<Button-1>", lambda event, a_line=x, a_column=y: self.click(event, a_line, a_column))
                a_column.append(aLabel)
            self.board_view.append(a_column)
        #preenchimento de message_frame com 1 imagem com logo (label) e 1 label com texto,
        # organizadas em 1 linha e 2 colunas
        #self.logo_label = Label(self.message_frame, bd = 0, image=self.logo)
        #self.logo_label.grid(row=0, column=0)
        #self.menubar.option_add('*tearOff', FALSE),
        self.message_label = Label(self.message_frame, bg="dark olive green", text=' COMBATE', font="arial 30")
        self.message_label.grid(row=0, column=1)
        self.menubar = Menu(self.main_window)
        self.menubar.option_add('*tearOff', FALSE)
        self.main_window['menu'] = self.menubar
        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.menu_file.add_command(label='Iniciar jogo', command = self.start_match)
        self.menu_file.add_command(label='restaurar estado inicial', command = self.start_game)

    def start_match(self):
        print('start_match')
    
    def start_game(self):
        print('start_game')
    
    def click(self, event, line, column):
        print('CLICK', line, column)