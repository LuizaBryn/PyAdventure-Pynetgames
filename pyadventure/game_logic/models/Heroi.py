from models import Jogador

class Heroi(object):
	def __init__(self):
		self.__ataque : int = 0
		self.__vitalidade : int = 60
		self.__mana : int = 10

	@property
	def getAtaque(self) -> int:
		return self.__ataque
	
	@property
	def getVitalidade(self) -> int:
		return self.__vitalidade
	
	@property
	def getMana(self) -> int:
		return self.__mana

	def addMana(self, aMana : int):
		pass

	def removeMana(self, aMana : int):
		pass

	

