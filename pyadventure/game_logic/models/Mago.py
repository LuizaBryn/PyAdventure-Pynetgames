from models import Heroi

class Mago(Heroi):
	def __init__(self):
		self._mana : int = 25

	@property
	def getMana(self) -> int:
		return self._mana
	