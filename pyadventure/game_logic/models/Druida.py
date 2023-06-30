from pyadventure.game_logic.models.Heroi import Heroi

class Druida(Heroi):
	def __init__(self):
		super().__init__()
		self.__vitalidade : int = 60

	@property
	def vitalidade(self) -> int:
		return self.__vitalidade
	
	@vitalidade.setter
	def vitalidade(self, aVitalidade : int):
		self.__vitalidade = aVitalidade