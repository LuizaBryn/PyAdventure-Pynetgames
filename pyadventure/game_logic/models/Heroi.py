class Heroi():
	def __init__(self):
		self.__ataque : int = 0
		self.__vitalidade : int = 50
		self.__mana : int = 20

	@property
	def ataque(self) -> int:
		return self.__ataque
	
	@property
	def vitalidade(self) -> int:
		return self.__vitalidade
	
	@vitalidade.setter
	def vitalidade(self, aVitalidade : int):
		self.__vitalidade = aVitalidade
	
	@property
	def mana(self) -> int:
		return self.__mana
	
	@mana.setter
	def mana(self, aMana : int):
		self.__mana = aMana

	