from pyadventure.game_logic.models.Heroi import Heroi

class Guerreiro(Heroi):
	def __init__(self):
		super().__init__()
		self.__ataque : int = 2

	@property
	def ataque(self) -> int:
		return self.__ataque
