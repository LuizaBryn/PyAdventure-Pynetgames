from pyadventure.game_logic.models.Heroi import Heroi

class Mago(Heroi):
	def __init__(self):
		super().__init__()
		self.__mana : int = 30

	@property
	def mana(self) -> int:
		return self.__mana
	
	@mana.setter
	def mana(self, aMana : int):
		self.__mana = aMana
	