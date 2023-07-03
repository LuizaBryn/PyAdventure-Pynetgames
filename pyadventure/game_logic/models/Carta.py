class Carta():
	def __init__(self, aTipo : str, aCusto : int, aDescricao : str):
		self.__custo : int = aCusto
		self.__descricao : str = aDescricao
		self.__tipo : str = aTipo

	@property
	def custo(self) -> int:
		return self.__custo

	@property
	def descricao(self) -> str:
		return self.__descricao

	@property
	def tipo(self) -> str:
		return self.__tipo

