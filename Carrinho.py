####################### BANCO DE DADOS ######################

# Importa a função de conexão com o SQL de um módulo chamado Conex_SQL
from Conex_SQL import connection

# Cria um cursor usando a conexão estabelecida. O cursor é usado para executar comandos SQL e buscar resultados.
cursor = connection.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################

# Importações necessárias para o funcionamento da classe Carrinho e manipulação de tempo e tipos
import time
from types import SimpleNamespace
from Estabelecimento import Estabelecimento # Importa a classe Estabelecimento de um módulo específico
from Pedido import Pedido # Importa a classe Pedido de um módulo específico
from Cliente import Cliente # Importa a classe Cliente de um módulo específico
from typing import Type # Importa a função Type do módulo typing para tipagem estática
from Item import Item # Importa a classe Item de um módulo específico
from Estabelecimento import Estabelecimento # Importa novamente a classe Estabelecimento (essa linha parece redundante)

# Define a classe Carrinho que vai representar um carrinho de compras
class Carrinho:
    
    # Construtor da classe Carrinho
    def __init__(self) -> None:
        # Inicializa a lista do carrinho vazia
        self.lista_carrinho: list = []
        # Inicializa o total com zero
        self.total: float = 0

########################################################################

    # Método para adicionar itens ao carrinho
    def adicionar_item(self, lista: list) -> list:
        # Atualiza a lista interna do carrinho com a lista fornecida como argumento
        self.lista_carrinho = lista
        # Incrementa a quantidade de cada item na lista do carrinho
        for p in self.lista_carrinho:
            p.quant_item += 1 # Supõe que os itens têm um atributo 'quant_item' que armazena a quantidade
        # Retorna a lista atualizada do carrinho
        return self.lista_carrinho
    
    # Método para remover um item específico do carrinho, usando o nome do item como critério
    def remove_item(self, lista: list, item: Type[Item]) -> list:
        # Atualiza a lista interna do carrinho com a lista fornecida como argumento
        self.lista_carrinho = lista
        # Remove o item especificado da lista do carrinho
        self.lista_carrinho.remove(item)
        # Retorna a lista atualizada do carrinho
        return self.lista_carrinho

    # Método para limpar o carrinho, removendo todos os itens
    def limpar_carrinho(self, lista: list) -> list:
        # Atualiza a lista interna do carrinho com a lista fornecida como argumento
        self.lista_carrinho = lista
        # Limpa todos os itens do carrinho
        self.lista_carrinho.clear()
        # Retorna a lista limpa do carrinho
        return self.lista_carrinho
