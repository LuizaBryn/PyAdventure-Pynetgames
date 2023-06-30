from pyadventure.game_logic.models.Heroi import Heroi
from pyadventure.game_logic.models.Mago import Mago
from pyadventure.game_logic.models.Druida import Druida
from pyadventure.game_logic.models.Guerreiro import Guerreiro
from pyadventure.game_logic.models.Baralho import Baralho

class Jogador():
	def __init__(self):
		self.__mao : list = []
		self.__heroi : Heroi = None
		self.__vez : bool = False
		self.__baralho : Baralho = None
		self.__herois : dict = {
			"druida": Druida,
			"mago": Mago,
			"guerreiro": Guerreiro
		}

	@property
	def heroi(self) -> Heroi:
		return self.__heroi
	
	@heroi.setter
	def heroi(self, aHeroi: Heroi):
		self.__heroi = aHeroi

	@property
	def mao(self) -> list:
		return self.__mao
	
	@property
	def vez(self) -> bool:
		return self.__vez
	
	@vez.setter
	def vez(self, aVez: bool):
		self.__vez = aVez
	
	@property
	def baralho(self) -> Baralho:
		return self.__baralho
	
	@property
	def herois(self) -> dict:
		return self.__herois
	
	def reset(self):
		self.__mao.clear()
		self.__heroi = None
		self.__vez = False
		self.__baralho = None


	def inicializar(self, escolha_heroi: str):
		self.__baralho = Baralho()

		self.heroi = self.herois[escolha_heroi]()

		self.baralho.reiniciarBaralho()

		self.receberCartasIniciais()

	def receberCartasIniciais(self):
		for _ in range(4):
			self.mao.append(self.baralho.removerCarta())