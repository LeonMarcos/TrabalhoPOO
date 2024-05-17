# import Cardapio

from Usuario import Usuario
from Cliente import Cliente
from Estabelecimento import Estabelecimento
from Item import Item
from typing import Type

class Carrinho:
    
    def __init__(self, cliente: Type[Cliente]):            
        self.nome = cliente.get_nome()
        self.lista_de_itens = []
        self.total = 0
                
    def add_carrinho()