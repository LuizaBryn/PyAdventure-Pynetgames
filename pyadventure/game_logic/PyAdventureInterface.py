from tkinter import *
import os
from tkinter import simpledialog
from tkinter import messagebox

from pyadventure.game_logic.models.Mesa import Mesa

# --------- importações do PyNetgames que serão usadas -----------

from py_netgames_client.tkinter_client.PyNetgamesServerListener import PyNetgamesServerListener
from py_netgames_client.tkinter_client.PyNetgamesServerProxy import PyNetgamesServerProxy

# from tkinter_sample.ServerConnectionMenubar import ServerConnectionMenubar

# -------------------------------------------------------------------------------------


class PyAdventureInterface(PyNetgamesServerListener):

    # _tk: Tk
    # _server_proxy: PyNetgamesServerProxy
    # _menu_bar = ServerConnectionMenubar
    # _ongoing_match: bool
    # _board: Optional[PyAdventureBoard]
    # _buttons: Dict[PyAdventureCoordinate, Button]
    # _logger: logging.Logger

    def __init__(self):
        self.janela = Tk()
        self.janela.title("PyAdventure")
        # self.janela.iconbitmap("img/icon.ico")
        self.janela.resizable(False, False)
        self.janela.geometry("1280x720")
        self.janela["bg"] = "#DBE9F4"
        self.janela.grid_columnconfigure(0, weight=1)
        self.janela.grid_rowconfigure(0, weight=1)  # frameStatus
        self.janela.grid_rowconfigure(1, weight=3)  # frameHerois
        self.janela.grid_rowconfigure(
            2, weight=3)  # frameCartasa AND menuBoard

        self.frameStatus = Frame(self.janela)
        self.frameStatus.grid(row=0, column=0, sticky="nsew")
        self.frameStatus.grid_columnconfigure(0, weight=1)
        self.frameStatus.grid_columnconfigure(1, weight=6)
        self.frameStatus.grid_columnconfigure(2, weight=1)
        self.frameStatus.grid_rowconfigure(0, weight=1)
        self.frameStatus.grid_rowconfigure(1, weight=1)

        self.vidaJogador1 = Label(self.frameStatus, text="Vida: X", font=60, pady=10)
        self.vidaJogador1.grid(row=0, column=0)

        self.manaJogador1 = Label(self.frameStatus, text="Mana: X", font=60, padx=0, pady=10)
        self.manaJogador1.grid(row=1, column=0)

        self.vidaJogador2 = Label(self.frameStatus, font=60, text="Vida: Y")
        self.vidaJogador2.grid(row=0, column=2)
        
        self.manaJogador2 = Label(self.frameStatus, text="Mana: Y", font=60,  padx=0, pady=10)
        self.manaJogador2.grid(row=1, column=2)

        self.frameHerois = Frame(self.janela)
        self.frameHerois.grid(row=1, column=0, sticky="nsew")
        self.frameHerois.grid_columnconfigure(0, weight=1)
        self.frameHerois.grid_columnconfigure(1, weight=1)
        self.frameHerois.grid_rowconfigure(2, weight=1)

        self.druidaMini = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/hero_druida_mini.png"))
        self.guerreiroMini = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/hero_guerreiro_mini.png"))
        self.magoMini = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/hero_mago_mini.png"))
        

        self.druidaEsquerdo = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/hero_druida_left.png"))
        self.guerreiroEsquerdo = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/hero_guerreiro_left.png"))
        self.magoEsquerdo = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/hero_mago_left.png"))
        
        self.druidaDireito = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/hero_druida_right.png"))
        self.guerreiroDireito = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/hero_guerreiro_right.png"))
        self.magoDireito = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/hero_mago_right.png"))
        
        self.cartaAtaque = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/ataque.png"))
        self.cartaAtaqueEspecial = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/ataque_especial.png"))
        self.cartaCurar = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/curar.png"))
        self.cartaBarganhar = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/barganhar.png"))
        self.cartaMeditar = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), "./img/meditar.png"))

        self.frameBarraTarefas = Frame(
            self.janela)
        self.frameBarraTarefas.grid(row=2, column=0, sticky="nsew")
        self.frameBarraTarefas.grid_columnconfigure(
            0, weight=7)  # coluna das cartas
        self.frameBarraTarefas.grid_columnconfigure(
            1, weight=2)  # coluna do menu
        self.frameBarraTarefas.grid_rowconfigure(0, weight=1)

        self.frameCartas = Frame(self.frameBarraTarefas, border=15)
        self.frameCartas.grid(row=0, column=0, sticky="nsew")
        self.frameCartas.grid_rowconfigure(0, weight=1)
        self.frameCartas.grid_rowconfigure(1, weight=10)

        self.menu = Frame(self.frameBarraTarefas, bg="#36696F")
        self.menu.grid(row=0, column=1, sticky="nsew")
        self.menu.grid_rowconfigure(0, weight=1)
        self.menu.grid_rowconfigure(1, weight=1)
        self.menu.grid_columnconfigure(0, weight=1)

        self.labels = []

        self.pularVez = Button(self.menu, text="Passar vez", bg="#91DBBB", fg="black", font=("Arial", 14),
                                width=10, height=2, bd=5, relief="raised", activebackground="#254954", 
                                activeforeground="white").grid(row=0, column=0)


        self.mesa = Mesa()
        self.__match_id = None
        self.__turnoLocal = False

        self.add_listener()
        self.send_connect()

        self.janela.mainloop()

    @property
    def match_id(self):
        return self.__match_id
    
    @match_id.setter
    def match_id(self, match_id: str):
        self.__match_id = match_id

    @property
    def turnoLocal(self):
        return self.__turnoLocal
    
    @turnoLocal.setter
    def turnoLocal(self, turnoLocal: bool):
        self.__turnoLocal = turnoLocal

    def selecionarCarta(self, indice: int):
        jogada = None
        if self.turnoLocal:
            escolha = self.mostrarAcoes(indice)
            if escolha == "jogar":
                jogada = self.mesa.jogarCarta(indice)
                self.atualizarInterface()
                if jogada is not None:
                    self.server_proxy.send_move(self.match_id, jogada)
                    self.turnoLocal = False
                else:
                    messagebox.showerror("Erro", "Você não tem mana suficiente para jogar essa carta ou sua mão esta cheia!")
            elif escolha == "descartar":
                self.mesa.descartarCarta(indice)
                self.atualizarInterface()

            
        else:
            messagebox.showerror("Erro", "Não é sua vez de jogar!")


    def carregarCarta(self, tipo: str):
        switcher = {
            "ataque": self.cartaAtaque,
            "ataque_especial": self.cartaAtaqueEspecial,
            "curar": self.cartaCurar,
            "barganhar": self.cartaBarganhar,
            "meditar": self.cartaMeditar
        }
        return switcher.get(tipo)

    def criarLabelsCartas(self):
        if self.labels is not None:
            for label in self.labels:
                label.destroy()
        self.labels = []

        for i in range(0,7):
            self.labels.append(Label(self.frameCartas))
            self.labels[i].grid(row=0, column=i, padx=10)

    def atualizarMao(self, mao: list):
        self.criarLabelsCartas()
        for i in range(len(mao)):
            self.labels[i].config(image=self.carregarCarta(mao[i].tipo), width=130, height=200)
            self.labels[i].bind("<Button-1>", lambda event, indice=i: self.selecionarCarta(indice))

    def atualizarStatus(self, status: dict):
        self.vidaJogador1.config(text=f"Vida: {status['jogador1']['vida']}")
        self.manaJogador1.config(text=f"Mana: {status['jogador1']['mana']}")
        self.vidaJogador2.config(text=f"Vida: {status['jogador2']['vida']}")
        self.manaJogador2.config(text=f"Mana: {status['jogador2']['mana']}")

    def atualizarInterface(self):
        self.atualizarMao(self.mesa.jogador1.mao)
        self.atualizarStatus(self.mesa.statusJogadores())

    def atualizarInterfaceHerois(self, heroi: str):
        if heroi == "druida":
            imagemHeroi = self.druidaDireito
        elif heroi == "guerreiro":
            imagemHeroi = self.guerreiroDireito
        elif heroi == "mago":
            imagemHeroi = self.magoDireito

        labelHeroi = Label(self.frameHerois, image=imagemHeroi)
        labelHeroi.grid(row=0, column=1)

    def escolheHeroi(self):
        modal = Toplevel(self.janela)
        modal.title("Escolha um herói")

        # Cria as variáveis para armazenar a escolha do herói
        self.heroiSelecionado = StringVar()

        # Cria os botões de rádio para cada herói
        frameHeroi = Frame(modal)
        frameHeroi.pack()

        opcoesHerois = ["druida", "guerreiro", "mago"]
        imagensHerois = [self.druidaMini, self.guerreiroMini, self.magoMini]

        for i in range(len(opcoesHerois)):
            # Define a imagem do herói
            imagemHeroi = imagensHerois[i]

            # Cria o botão de rádio com a imagem do herói
            botaoHeroi = Radiobutton(frameHeroi, image=imagemHeroi, variable=self.heroiSelecionado,
                                      value=opcoesHerois[i], indicatoron=0, width=100, height=100)
            botaoHeroi.pack(side=LEFT, padx=10)

        # Adiciona um botão OK para confirmar a escolha
        botaoOK = Button(modal, text="OK", command=modal.destroy)
        botaoOK.pack(pady=10)

        # Aguarda a seleção do herói
        modal.wait_window(modal)

        # Carrega a imagem do herói escolhido
        heroiEscolhido = self.heroiSelecionado.get()
        imagemHeroi = None

        if heroiEscolhido == "druida":
            imagemHeroi = self.druidaEsquerdo
        elif heroiEscolhido == "guerreiro":
            imagemHeroi = self.guerreiroEsquerdo
        elif heroiEscolhido == "mago":
            imagemHeroi = self.magoEsquerdo

        # Exibe a imagem do herói escolhido
        if imagemHeroi is not None:
            labelHeroi = Label(self.frameHerois, image=imagemHeroi)
            labelHeroi.grid(row=0, column=0)

        return heroiEscolhido

    def mostrarAcoes(self, indice: int):
        # Create a new window
        janelaAcoes = Toplevel(self.janela)
        janelaAcoes.title("Ações")

        escolha = StringVar()

        # Get the card from the player's hand based on the card index
        carta = self.mesa.jogador1.mao[indice]

        # Create a label to display the carta information
        labelCarta = Label(janelaAcoes, text=f"carta: {carta.tipo}")
        labelCarta.pack()

        # Create buttons for the available actions
        def setEscolhaJogar():
            escolha.set("jogar")
            janelaAcoes.destroy()

        def setEscolhaDescartar():
            escolha.set("descartar")
            janelaAcoes.destroy()

        botaoJogar = Button(janelaAcoes, text="Play", command=setEscolhaJogar)
        botaoJogar.pack()

        botaoDescartar = Button(janelaAcoes, text="Descarta", command=setEscolhaDescartar)
        botaoDescartar.pack()

        janelaAcoes.wait_window(janelaAcoes)

        return escolha.get()


    # -------------------------- PynetGames --------------------------
    def add_listener(self):
        self.server_proxy = PyNetgamesServerProxy()
        self.server_proxy.add_listener(self)

    def send_connect(self):
        self.server_proxy.send_connect(
            address="wss://py-netgames-server.fly.dev")
    
    def send_match(self):
        self.server_proxy.send_match(2)

    def receive_connection_success(self):
        print("====== conectado =======")
        self.send_match()

    def receive_error(self):
        pass

    def receive_match(self, match):
        print("== partida iniciada ==")
        print("== ordem:", match.position)
        print("== match_id", match.match_id)
        self.match_id = match.match_id
        vez = match.position
        if vez == 1:
            self.turnoLocal = True

        escolhaHeroi = self.escolheHeroi()
        self.mesa.start_match(vez, escolhaHeroi)

        jogada = {
            "tipo": "Heroi",
            "heroi": escolhaHeroi
        }

        self.server_proxy.send_move(self.match_id, jogada)


    def receive_disconnect(self):
        pass

    def receive_move(self, jogada):
        tipoJogada = jogada.payload["tipo"]

        if tipoJogada == "jogarCarta":
            self.mesa.resolverCartaRemoto(jogada.payload)
            self.turnoLocal = True
        elif tipoJogada == "PassarVez":
            pass
        elif tipoJogada == "Heroi":
            self.mesa.jogador2.heroi = self.mesa.jogador2.herois[jogada.payload["heroi"]]()
            self.atualizarInterfaceHerois(jogada.payload["heroi"])
        
        self.atualizarInterface()

