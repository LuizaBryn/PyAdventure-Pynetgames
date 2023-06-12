from models import Mao
from models import Baralho
from models import Mesa

class Carta(object):
	def selecionarCarta(self):
		pass

	def __init__(self):
		self.__custo : int = None
		self.__descricao : str = None
		self.__dano : int = None
		self.__tipo : str = None
