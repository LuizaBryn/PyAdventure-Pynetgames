from models import Jogador
from models import Carta

class Mesa(object):
	def __init__(self):
		self.__jogador1 : Jogador = Jogador()
		self.__jogador2 : Jogador = Jogador()
		self.__partida_em_andamento : bool = False
		self.__vez_jogar : bool = False
		self.__ultima_carta : Carta = None

	def start_match(self, aTurn : bool):
		pass

	def getPartidaAndamento(self) -> bool:
		pass

	def getVezJogador(self) -> bool:
		pass

	def reset(self):
		pass

	def set_partida_andamento(self, aStatus : bool):
		pass

	def mudarVez(self) -> Jogador:
		pass

	def getJogador(self) -> Jogador:
		pass

	def verificaMana(self) -> int:
		pass

	def usar_Carta(self, aCarta : Carta):
		pass

	def notificar(self, aMensgem : str):
		pass

	def descartarCarta(self, aCarta : Carta):
		pass

