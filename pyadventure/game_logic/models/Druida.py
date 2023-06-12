from models import Heroi

class Druida(Heroi):
	def __init__(self):
		self.__vitalidade : int = 70

	@property
	def getVitalidade(self) -> int:
		return self.__vitalidade