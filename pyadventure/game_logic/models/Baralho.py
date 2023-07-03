import random
from collections import deque
from pyadventure.game_logic.models.Carta import Carta

class Baralho(object):
	def __init__(self):
		self.__cartas : Carta = deque()

	@property
	def cartas(self) -> Carta:
		return self.__cartas

	def criarBaralho(self) -> None:
		tipos = {
			"ataque_especial": (7, 5, "Adiciona 7 de dano ao ataque"),
			"ataque": (16, 2, "Adiciona 3 de dano ao ataque"),
			"meditar": (11, 0, "Recupera 8 de mana"),
			"curar": (7, 3, "Recupera 5 de vida"),
			"barganhar": (9, 2, "Compre duas cartas")
		}

		for tipo, (quantidade, custo, descricao) in tipos.items():
			for _ in range(quantidade):
				carta = Carta(tipo, custo, descricao)
				self.cartas.append(carta)

		self.embaralhar()

	def embaralhar(self) -> None:
		random.shuffle(self.__cartas)

	def removerCarta(self) -> Carta:
		return self.cartas.pop()

	def reiniciarBaralho(self) -> None:
		self.cartas.clear()
		self.criarBaralho()

