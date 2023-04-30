from tkinter import *
import os

# --------- importações do PyNetgames que serão usadas -----------

import logging
from typing import Dict, Optional
from uuid import UUID

from py_netgames_client.tkinter_client.PyNetgamesServerListener import PyNetgamesServerListener
from py_netgames_client.tkinter_client.PyNetgamesServerProxy import PyNetgamesServerProxy

# from tkinter_sample.ServerConnectionMenubar import ServerConnectionMenubar

# -------------------------------------------------------------------------------------


class PyAdventureInterface(PyNetgamesServerListener):

    # _tk: Tk
    # _server_proxy: PyNetgamesServerProxy
    # _menu_bar = ServerConnectionMenubar
    # _ongoing_match: bool
    # _match_id: UUID
    # _board: Optional[PyAdventureBoard]
    # _buttons: Dict[PyAdventureCoordinate, Button]
    # _logger: logging.Logger

    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.title("PyAdventure")
        # self.mainWindow.iconbitmap("img/icon.ico")
        self.mainWindow.resizable(False, False)
        self.mainWindow.geometry("1280x720")
        self.mainWindow["bg"] = "#DBE9F4"
        self.mainWindow.grid_columnconfigure(0, weight=1)
        self.mainWindow.grid_rowconfigure(0, weight=1)  # statusBoard
        self.mainWindow.grid_rowconfigure(1, weight=3)  # herosBoard
        self.mainWindow.grid_rowconfigure(
            2, weight=3)  # cardBoarda AND menuBoard

        self.statusBoard = Frame(self.mainWindow)
        self.statusBoard.grid(row=0, column=0, sticky="nsew")
        self.statusBoard.grid_columnconfigure(0, weight=1)
        self.statusBoard.grid_columnconfigure(1, weight=6)
        self.statusBoard.grid_columnconfigure(2, weight=1)
        self.statusBoard.grid_rowconfigure(0, weight=1)
        self.statusBoard.grid_rowconfigure(1, weight=1)

        self.lifePlayer1 = Label(
            self.statusBoard, text="Vida: X", font=60, pady=10)
        self.lifePlayer1.grid(row=0, column=0)
        self.manaPlayer1 = Label(
            self.statusBoard, text="Mana: X", font=60, padx=0, pady=10)
        self.manaPlayer1.grid(row=1, column=0)
        self.lifePlayer2 = Label(self.statusBoard, font=60, text="Vida: Y")
        self.lifePlayer2.grid(row=0, column=2)
        self.lifePlayer2 = Label(
            self.statusBoard, text="Mana: Y", font=60,  padx=0, pady=10)
        self.lifePlayer2.grid(row=1, column=2)
        self.roundCounter = Label(
            self.statusBoard, text="Round _", font=60, pady=10)
        self.roundCounter.grid(row=0, column=1)

        self.herosBoard = Frame(self.mainWindow)
        self.herosBoard.grid(row=1, column=0, sticky="nsew")
        self.herosBoard.grid_columnconfigure(0, weight=1)
        self.herosBoard.grid_columnconfigure(1, weight=1)
        self.herosBoard.grid_rowconfigure(2, weight=1)

        self.heroDruidaLeft = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/hero_druida_left.png"))
        self.heroGuerreiroLeft = PhotoImage(
            file=os.path.join(os.path.dirname(__file__), "./img/hero_guerreiro_left.png"))
        self.heroMagoLeft = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/hero_mago_left.png"))

        self.labelDruida = Label(self.herosBoard, image=self.heroDruidaLeft)
        # if heroPlayerLeft == "druida":
        self.labelDruida.grid(row=0, column=0)
        self.labelGuerreiro = Label(
            self.herosBoard, image=self.heroGuerreiroLeft)
        # if heroPlayerLeft == "guerreiro":
        self.labelGuerreiro.grid(row=0, column=0)
        self.labelMago = Label(self.herosBoard, image=self.heroMagoLeft)
        # if heroPlayerLeft == "mago":
        self.labelMago.grid(row=0, column=0)

        self.heroDruidaRight = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/hero_druida_right.png"))
        self.heroGuerreiroRight = PhotoImage(
            file=os.path.join(os.path.dirname(__file__), "./img/hero_guerreiro_right.png"))
        self.heroMagoRight = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/hero_mago_right.png"))

        self.labelDruida = Label(self.herosBoard, image=self.heroDruidaRight)
        # if heroPlayerRight == "druida":
        self.labelDruida.grid(row=0, column=1)
        self.labelGuerreiro = Label(
            self.herosBoard, image=self.heroGuerreiroRight)
        # if heroPlayerRight == "guerreiro":
        self.labelGuerreiro.grid(row=0, column=1, sticky="s")
        self.labelMago = Label(
            self.herosBoard, image=self.heroMagoRight)
        # if heroPlayerRight == "mago":
        self.labelMago.grid(row=0, column=1)

        self.barraTarefasFrame = Frame(
            self.mainWindow)
        self.barraTarefasFrame.grid(row=2, column=0, sticky="nsew")
        self.barraTarefasFrame.grid_columnconfigure(
            0, weight=7)  # coluna das cartas
        self.barraTarefasFrame.grid_columnconfigure(
            1, weight=2)  # coluna do menu
        self.barraTarefasFrame.grid_rowconfigure(0, weight=1)

        self.cardBoard = Frame(self.barraTarefasFrame, bg="#56899F", border=15)
        self.cardBoard.grid(row=0, column=0, sticky="nsew")
        self.cardBoard.grid_rowconfigure(0, weight=1)
        self.cardBoard.grid_rowconfigure(1, weight=10)

        self.menu = Frame(self.barraTarefasFrame, bg="#36696F")
        self.menu.grid(row=0, column=1, sticky="nsew")
        self.menu.grid_rowconfigure(0, weight=1)
        self.menu.grid_rowconfigure(1, weight=1)
        self.menu.grid_columnconfigure(0, weight=1)

        for i in range(4):
            self.cardBoard.grid_columnconfigure(i, weight=1)

            carta = Button(self.cardBoard, name=str(i), text="Carta {}".format(i+1),
                           padx=40, pady=80, command=self.remove_card)
            carta.grid(row=1, column=i)

            carta.bind('<Button-1>', self.remove_card)

        self.pular_vez = Button(self.menu, text="Passar vez", bg="#91DBBB", fg="black", font=("Arial", 14),
                                width=10, height=2, bd=5, relief="raised", activebackground="#254954", activeforeground="white", command=self.add_card)
        self.pular_vez.grid(row=0, column=0)

        self.card_description = Button(self.menu, text="Cartas", bg="#91DBBB", fg="black", font=("Arial", 14),
                                       width=10, height=2, bd=5, relief="raised", activebackground="#254954", activeforeground="white", command=self.see_cards)
        self.card_description.grid(row=1, column=0)

        self.add_listener()
        self.send_connect()

        self.mainWindow.mainloop()

    def remove_card(self, event=None):
        card = event.widget
        column = int(card.winfo_name())
        card.grid_remove()
        self.cardBoard.grid_columnconfigure(column, minsize=0)

    def add_card(self, event=None):
        new_column = self.cardBoard.grid_size()[0] + 1
        self.cardBoard.grid_columnconfigure(new_column, weight=1)
        new_card = Button(self.cardBoard, text="Carta", name=str(new_column),
                          padx=50, pady=80)
        new_card.grid(row=1, column=new_column)
        new_card.bind('<Button-1>', self.remove_card)

    def see_cards(self):
        popup = Toplevel(self.mainWindow)
        popup.title("Cartas PyAdventure")
        popup.geometry("200x100")
        popup_label = Label(popup, text="Aqui ficarão as descrições!")
        popup_label.pack()

    # -------------------------- PynetGames --------------------------
    def add_listener(self):
        self.server_proxy = PyNetgamesServerProxy
        self.server_proxy.add_listener(self)

    def send_connect(self):
        self.server_proxy.send_connect(
            address="wss://py-netgames-server.fly.dev")

    def receive_connection_sucess(self):
        print("====== conectado =======")
        self.send_match()

    def receive_error(self):
        pass

    def send_match(self):
        self.server_proxy.send_match(2)

    def receive_match(self, match):
        print("== partida iniciada ==")
        print("== ordem:", match.position)
        print("== match_id", match.match.id)

    def receive_disconnect(self):
        pass

    def receive_move(self):
        pass
