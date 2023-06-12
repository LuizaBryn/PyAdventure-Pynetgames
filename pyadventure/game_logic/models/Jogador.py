from models import Mao
from models import Heroi
from models import Baralho
from models import Mesa

class Jogador(object):
	def __init__(self):
		self.__mao : Mao = None
		self.__heroi : Heroi = None
		self.__vez : bool = None

	def enable(self):
		pass

	def reset(self):
		pass

	def seuTurno(self) -> bool:
		pass

	def definirDruida(self):
		pass

	def definirMago(self):
		pass

	def definirGuerreiro(self):
		pass

	def getHeroi(self) -> Heroi:
		return self.__heroi

	def getMao(self) -> Mao:
		return self.__mao


