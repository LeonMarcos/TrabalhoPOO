####################### BANCO DE DADOS ######################

# Importa a função de conexão com o SQL de um módulo chamado Conex_SQL
from Conex_SQL import connection

# Cria um cursor usando a conexão estabelecida. O cursor é usado para executar comandos SQL e buscar resultados.
cursor = connection.cursor() # utiliza-se o cursor para apontar para as variáveis dentro do SQL

#############################################################

# Importa o módulo time para manipulação de tempo, mas não está sendo utilizado diretamente no código fornecido
import time
# Importa Type do módulo typing para suporte a anotações de tipo
from typing import Type

# Define a classe Item
class Item:
    
    # Construtor da classe Item
    def __init__(self) -> None:
        # Inicializa os atributos do item como None
        self.id: int = None
        self.nome: str = None
        self.descricao: str = None
        self.preco: float = None
        
########################################################################

    # Método para criar e adicionar um item ao banco de dados
    def cria_item(self, id: int, nome: str, descricao: str, preco: int) -> None:
        # Define os atributos do item com os valores fornecidos como parâmetros
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

        # Comando SQL para inserir um novo item na tabela Itens
        comando = """ INSERT INTO Itens(loja_id, nome, descricao, preco)
                      VALUES (?, ?, ?, ?)"""
        
        # Executa o comando SQL com os valores dos atributos do item
        cursor.execute(comando, self.id, self.nome, self.descricao, self.preco)
        # Confirma a transação no banco de dados
        cursor.commit()
