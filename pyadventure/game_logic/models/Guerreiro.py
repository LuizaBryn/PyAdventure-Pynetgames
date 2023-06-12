from models import Heroi

class Guerreiro(Heroi):
	def __init__(self):
		self.__ataque : int = 2

	@property
	def getAtaque(self) -> int:
		return self.__ataque
