from pyadventure.game_logic.models.Jogador import Jogador
from pyadventure.game_logic.models.Carta import Carta

class Mesa(object):
	def __init__(self):
		self.__jogador1 : Jogador = Jogador() # Jogador local
		self.__jogador2 : Jogador = Jogador() # Jogador remoto
		self.__partidaEmAndamento : bool = False

	@property
	def jogador1(self) -> Jogador:
		return self.__jogador1
	
	@property
	def jogador2(self) -> Jogador:
		return self.__jogador2
	
	@property
	def partidaEmAndamento(self) -> bool:
		return self.__partidaEmAndamento
	
	@partidaEmAndamento.setter
	def partidaEmAndamento(self, aPartidaEmAndamento : bool):
		self.__partidaEmAndamento = aPartidaEmAndamento

	def start_match(self, aTurn : bool, aEscolhaHeroi: str):
		self.reset()
		self.partida_em_andamento = True
		self.vez_jogar = aTurn
		if self.vez_jogar:
			self.jogador1.vez = True
		else:
			self.jogador2.vez = True

		self.jogador1.inicializar(aEscolhaHeroi)

	def statusJogadores(self):
		return {
			"jogador1": {
				"vida": self.jogador1.heroi.vitalidade,
				"mana": self.jogador1.heroi.mana
			},
			"jogador2": {
				"vida": self.jogador2.heroi.vitalidade,
				"mana": self.jogador2.heroi.mana
			}
		}

	def jogarCarta(self, aIndiceCarta : int):
		carta = self.obtemCarta(self.jogador1, aIndiceCarta)
		if self.jogador1.heroi.mana >= carta.custo:
			if carta.tipo == "barganhar" and len(self.jogador1.mao) > 6:
				return False
			self.resolverCartaLocal({"carta": carta.tipo, "custo": carta.custo})
			if  not self.partida_em_andamento:
				return {
					"tipo": "fimDeJogo",
				}
			self.jogador1.mao.remove(carta)
			return {
				"carta": carta.tipo,
				"custo": carta.custo,
				"tipo": "jogarCarta"
			}
		else:
			return False
		
	def passarVez(self):
		return {
			"tipo": "PassarVez"
		}
			
		
	def descartarCarta(self, aIndiceCarta : int):
		carta = self.obtemCarta(self.jogador1, aIndiceCarta)
		self.jogador1.mao.remove(carta)

	def obtemCarta(self, aJogador : Jogador, aIndiceCarta : int):
		return aJogador.mao[aIndiceCarta]
	
	def resolverCartaLocal(self, aJogada : dict):
		carta = aJogada["carta"]
		custo = aJogada["custo"]
		match carta:
			case "ataque_especial":
				self.jogador1.heroi.mana -= custo
				self.jogador2.heroi.vitalidade -= (7 + self.jogador1.heroi.ataque)
				self.avaliarVitoria()
			case "ataque":
				self.jogador1.heroi.mana -= custo
				self.jogador2.heroi.vitalidade -= (3 + self.jogador1.heroi.ataque)
				self.avaliarVitoria()
			case "meditar":
				self.jogador1.heroi.mana -= custo
				self.jogador1.heroi.mana += 8
			case "curar":
				self.jogador1.heroi.mana -= custo
				self.jogador1.heroi.vitalidade += 5
			case "barganhar":
				self.jogador1.heroi.mana -= custo
				self.jogador1.mao.append(self.jogador1.baralho.removerCarta())
				self.jogador1.mao.append(self.jogador1.baralho.removerCarta())
		

	def resolverCartaRemoto(self, aJogada : dict):
		carta = aJogada["carta"]
		custo = aJogada["custo"]
		match carta:
			case "ataque_especial":
				self.jogador2.heroi.mana -= custo
				self.jogador1.heroi.vitalidade -= (7 + self.jogador2.heroi.ataque)
			case "ataque":
				self.jogador2.heroi.mana -= custo
				self.jogador1.heroi.vitalidade -= (3 + self.jogador2.heroi.ataque)
			case "meditar":
				self.jogador2.heroi.mana -= custo
				self.jogador2.heroi.mana += 8
			case "curar":
				self.jogador2.heroi.mana -= custo
				self.jogador2.heroi.vitalidade += 5
			case "barganhar":
				self.jogador2.heroi.mana -= custo

	def comprarCarta(self):
		if len(self.jogador1.mao) < 7:
			self.jogador1.mao.append(self.jogador1.baralho.removerCarta())

	def avaliarVitoria(self):
		if self.jogador2.heroi.vitalidade <= 0:
			self.partida_em_andamento = False


	def reset(self):
		self.__jogador1.reset()
		self.__jogador2.reset() 
		self.__partidaEmAndamento = False

