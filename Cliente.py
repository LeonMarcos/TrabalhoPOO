####################### BANCO DE DADOS ######################

# Importa um módulo específico do pacote lib2to3, provavelmente usado para alguma operação de transformação de código
from lib2to3.fixes.fix_idioms import TYPE
# Importa a função de conexão com o SQL de um módulo chamado Conex_SQL
from Conex_SQL import connection

# Cria um cursor usando a conexão estabelecida. O cursor é usado para executar comandos SQL e buscar resultados.
cursor = connection.cursor() # utiliza-se o cursor para apontar para as variáveis dentro do SQL

#############################################################

# Importa o pacote Flet para a construção de interfaces de usuário
import flet as ft
# Importa o módulo re para operações de expressões regulares
import re
# Importa o módulo time para manipulação de tempo
import time
# Importa a classe Usuario de um módulo específico
from Usuario import Usuario
# Importa flet_runtime, provavelmente para operações em tempo de execução com Flet
from flet_runtime import *
# Importa a função Type do módulo typing para tipagem estática
from typing import Type

# Define a classe Cliente que herda de Usuario
class Cliente(Usuario):
    
    # Construtor da classe Cliente
    def __init__(self):
        # Chama o construtor da classe base (Usuario)
        super().__init__()
        # Inicializa os atributos privados do cliente como None
        self.__nome: str = None
        self.__endereco: str = None
        self.__telefone: int = None
        self.__email: str = None
        self.__cpf_cnpj: int = None
        self.__senha: str = None
        self.__id: int = None
        # Define o tipo como o nome da classe, útil para identificar o tipo de usuário
        self.tipo = self.__class__.__name__

    # Métodos getters para acessar os atributos privados

    def get_nome(self) -> str:
        return self.__nome

    def get_endereco(self) -> str:
        return self.__endereco

    def get_telefone(self) -> int:
        return self.__telefone

    def get_email(self) -> str:
        return self.__email

    def get_cpf_cnpj(self) -> int:
        return self.__cpf_cnpj

    def get_senha(self) -> str:
        return self.__senha
    
    def get_id(self) -> int:
        return self.__id

    # Métodos setters para modificar os atributos privados

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def set_endereco(self, endereco: str) -> None:
        self.__endereco = endereco

    def set_telefone(self, telefone: int) -> None:
        self.__telefone = telefone

    def set_email(self, email: str) -> None:
        self.__email = email

    def set_cpf_cnpj(self, cpf_cnpj: int) -> None:
        self.__cpf_cnpj = cpf_cnpj

    def set_senha(self, senha: str) -> None:
        self.__senha = senha

    def set_id(self, id: int) -> None:
        self.__id = id

##################################################################

    # Método para alterar os dados do cliente no banco de dados
    def alterar_dados(self, nome: str, endereco: str, telefone: int, email: str, cpf_cnpj: int, senha: str, id: int) -> None:

        # Comando SQL para atualizar os dados do cliente na tabela Usuarios
        comando = """ UPDATE Usuarios
                        SET  nome = ?,
                            endereco = ?,
                            telefone = ?,
                            email = ?,
                            cpf_cnpj = ?,
                            senha = ?
                        WHERE id = ? """

        # Executa o comando SQL com os parâmetros fornecidos
        cursor.execute(comando, nome, endereco, telefone, email, cpf_cnpj, senha, id)
        # Confirma a transação no banco de dados
        cursor.commit()

    # Método para avaliar um pedido específico, atualizando a avaliação no banco de dados
    def avaliar_pedido(self, avaliacao: int, id: int) -> None:
                
        # Comando SQL para atualizar a avaliação do pedido na tabela Pedidos
        comando = """ 
                    UPDATE Pedidos
                    SET avaliacao = ?
                    WHERE id = ?
                  """
        
        # Executa o comando SQL com os parâmetros fornecidos
        cursor.execute(comando, avaliacao, id)
        # Confirma a transação no banco de dados
        cursor.commit()
