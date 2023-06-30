class Carta():
	def __init__(self, aTipo : str, aCusto : int, aDescricao : str):
		self.__custo : int = aCusto
		self.__descricao : str = aDescricao
		self.__tipo : str = aTipo

	@property
	def custo(self) -> int:
		return self.__custo
	
	@custo.setter
	def custo(self, aCusto : int):
		self.__custo = aCusto

	@property
	def descricao(self) -> str:
		return self.__descricao
	
	@descricao.setter
	def descricao(self, aDescricao : str):
		self.__descricao = aDescricao

	@property
	def tipo(self) -> str:
		return self.__tipo
	
	@tipo.setter
	def tipo(self, aTipo : str):
		self.__tipo = aTipo
	
	def selecionarCarta(self):
		pass

