####################### BANCO DE DADOS ######################

# Importa o módulo email que pode ser utilizado para manipulação de emails, embora não seja utilizado neste código
import email
# Importa a função de conexão com o SQL de um módulo chamado Conex_SQL
from Conex_SQL import connection

# Cria um cursor usando a conexão estabelecida. O cursor é usado para executar comandos SQL e buscar resultados.
cursor = connection.cursor() # utiliza-se o cursor para apontar para as variáveis dentro do SQL

#############################################################

# Importa o pacote Flet para construção de interfaces de usuário
import flet as ft
# Importa o módulo re para operações de expressões regulares
import re
# Importa o módulo time para manipulação de tempo
import time
# Importa a classe Usuario de um módulo específico
from Usuario import Usuario
# Importa a classe Item de um módulo específico
from Item import Item

# Cria uma instância da classe Item
item = Item()

# Define a classe Estabelecimento que herda de Usuario
class Estabelecimento(Usuario):
    # Constantes para validações usando expressões regulares (Regex)
    # Regex para garantir que o telefone tenha exatamente 11 dígitos
    padrao_telefone = r"^\d{11}$"
    # Regex para garantir que o nome só contenha letras e espaços, incluindo caracteres acentuados
    padrao_nome = r"^[a-zA-ZÀ-ÿ ]+$"
    # Regex para garantir que o CNPJ tenha exatamente 14 dígitos
    padrao_cnpj = r"^\d{14}$"

    # Construtor da classe Estabelecimento
    def __init__(self):
        # Chama o construtor da classe base (Usuario)
        super().__init__()
        # Inicializa os atributos privados do estabelecimento como None
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
    
    def get_id(self) -> str:
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

########################################################################

    # Método para alterar os dados do estabelecimento no banco de dados
    def alterar_dados(self, nome: str, endereco: str, telefone: int, email: str, cpf_cnpj: int, senha: str, id: int) -> None:

        # Comando SQL para atualizar os dados do estabelecimento na tabela Usuarios
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

    # Método para cancelar um pedido, atualizando seu status no banco de dados
    def cancelar_pedido(self, id: int) -> None:
        # Comando SQL para atualizar o status do pedido para 'Cancelado' na tabela Pedidos
        comando = """ UPDATE Pedidos
                        SET status_pedido = 'Cancelado'
                        WHERE id = ?;"""
        # Executa o comando SQL com o parâmetro fornecido
        cursor.execute(comando, id)
        # Confirma a transação no banco de dados
        cursor.commit()
        
    # Método para confirmar um pedido, atualizando seu status no banco de dados
    def confirmar_pedido(self, id: int) -> None:
        # Comando SQL para atualizar o status do pedido para 'Concluído' na tabela Pedidos
        comando = """ UPDATE Pedidos
                    SET status_pedido = 'Concluído'
                    WHERE id = ?;"""
        # Executa o comando SQL com o parâmetro fornecido
        cursor.execute(comando, id)
        # Confirma a transação no banco de dados
        cursor.commit()
    
    # Método para cadastrar um novo item usando a instância de Item criada
    def cadastrar_item(self, id: int, nome: str, descricao: str, preco: int) -> None:
        # Utiliza o método cria_item da classe Item para adicionar um novo item
        item.cria_item(id, nome, descricao, preco)

    # Método para alterar os dados de um item específico no banco de dados
    def alterar_item(self, nome: str, descricao: str, preco: int, id: int) -> None:
        # Comando SQL para atualizar os dados do item na tabela Itens
        comando = """
                        UPDATE Itens
                        SET         nome = ?, 
                                    descricao = ?, 
                                    preco = ?
                        WHERE item_id = ?
                        """
        # Executa o comando SQL com os parâmetros fornecidos
        cursor.execute(comando, nome, descricao, preco, id)
        # Confirma a transação no banco de dados
        cursor.commit()
    
    # Método para remover um item específico do banco de dados
    def remover_item(self, id: int) -> None:
        # Comando SQL para deletar o item da tabela Itens
        comando = """ DELETE FROM Itens
                                WHERE item_id = ? """
        # Executa o comando SQL com o parâmetro fornecido
        cursor.execute(comando, id)
        # Confirma a transação no banco de dados
        cursor.commit()
