####################### BANCO DE DADOS ######################

# Importa a função de conexão com o SQL de um módulo chamado Conex_SQL
from Conex_SQL import connection

# Cria um cursor usando a conexão estabelecida. O cursor é usado para executar comandos SQL e buscar resultados.
cursor = connection.cursor() # utiliza-se o cursor para apontar para as variáveis dentro do SQL

#############################################################

# Importa módulos e classes necessárias para a execução do código
import time
import datetime
from typing import List, Any
from Cliente import Cliente
from Estabelecimento import Estabelecimento
from Usuario import Usuario

# Define a classe Pedido
class Pedido:
    
    # Construtor da classe Pedido
    def __init__(self) -> None:
        # Inicializa os atributos do pedido como None
        self.id: int = None
        self.status: str = None
        self.total: float = None
        self.avaliacao: int = None

        # Obtém a data e hora atuais
        data_hora_atual = datetime.datetime.now()
        # Formata a data e a hora no formato desejado
        data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y às %H:%M:%S")
        
        # Define a data e horário que o pedido foi realizado
        self.data_horario_pedido = str(data_hora_formatada)
        
###########################################################################

    # Método para criar e adicionar um pedido ao banco de dados
    def cria_pedido(self, lista: List[Any]) -> None:
        # Inicializa a lista de itens do pedido
        self.lista = []
        # Adiciona os itens da lista fornecida à lista do pedido
        for p in lista:
            self.lista.append(p)
        
        print('finalizou')
        
        # Define o status do pedido como 'Pendente'
        self.status = 'Pendente'
        
        # Obtém o último ID de pedido da tabela Pedidos para definir o novo ID do pedido
        cursor.execute("SELECT MAX(id) FROM Pedidos")
        ultimo_id = cursor.fetchone()[0]
        # Incrementa o último ID para definir o ID do novo pedido
        self.id = ultimo_id + 1
        
        # Insere cada item do pedido no banco de dados
        for p in self.lista:
            comando = """ 
                INSERT INTO Pedidos(id, loja_id, cliente_id, id_item, quant_item, preco, subtotal, endereco, data_horario_pedido, status_pedido, nome_cliente, nome_loja, nome_item)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            # Executa o comando SQL com os valores dos atributos do item
            cursor.execute(comando, self.id, p.loja_id, p.cliente_id, p.item_id, p.quant_item, p.preco, p.subtotal, p.endereco, self.data_horario_pedido, self.status, p.nome_cliente, p.estab_nome, p.nome)
            # Confirma a transação no banco de dados
            cursor.commit()
    
    # Método para consultar pedidos finalizados de um estabelecimento
    def consulta_pedidos_finalizados(self, tabela: list, estabelecimento: list):
        # Define o status do pedido como 'Pendente'
        self.status = 'Pendente'

        # Consulta SQL para obter pedidos que não estão pendentes para o estabelecimento fornecido
        consulta = """
            SELECT DISTINCT id, status_pedido, nome_cliente, data_horario_pedido, avaliacao
            FROM Pedidos
            WHERE loja_id = ? AND status_pedido != ?
        """ # consulta o banco de dados
        
        # Executa a consulta SQL com o ID do estabelecimento e o status do pedido
        cursor.execute(consulta, estabelecimento.id, self.status)
        aux = cursor.fetchall()
        
        # Limpa a tabela antes de adicionar novos dados
        tabela.clear()
        
        # Adiciona os resultados da consulta à tabela
        for p in aux:
            tabela.append(p)
    
    # Método para consultar pedidos pendentes de um estabelecimento
    def consulta_pedidos_pendentes(self, tabela: list, estabelecimento: list) -> None:
        # Define o status do pedido como 'Pendente'
        self.status = 'Pendente'

        # Consulta SQL para obter pedidos que estão pendentes para o estabelecimento fornecido
        consulta = """
            SELECT DISTINCT id, status_pedido, nome_cliente, data_horario_pedido
            FROM Pedidos
            WHERE loja_id = ? AND status_pedido = ?
        """ # consulta o banco de dados
        
        # Executa a consulta SQL com o ID do estabelecimento e o status do pedido
        cursor.execute(consulta, estabelecimento.id, self.status)
        aux = cursor.fetchall()
        
        # Limpa a tabela antes de adicionar novos dados
        tabela.clear()
        
        # Adiciona os resultados da consulta à tabela
        for p in aux:
            tabela.append(p)
    
    # Método para buscar detalhes de um pedido específico
    def busca_pedido(self, pedido, itens_pedido) -> None:
        # Define o ID do pedido
        self.id = pedido.id
        
        # Consulta SQL para obter todos os detalhes de um pedido específico
        busca = """
            SELECT * FROM Pedidos
            WHERE id = ?
        """ # consulta o banco de dados
        
        # Executa a consulta SQL com o ID do pedido
        cursor.execute(busca, self.id)
        aux = cursor.fetchall()
        
        # Limpa a lista de itens do pedido antes de adicionar novos dados
        itens_pedido.clear()
        
        # Adiciona os resultados da consulta à lista de itens do pedido
        for p in aux:
            itens_pedido.append(p)
    
    # Método para consultar pedidos de um cliente específico
    def consulta_pedidos_cliente(self, tabela: list, cliente: list) -> None:
        # Consulta SQL para obter pedidos de um cliente específico
        consulta = """
            SELECT DISTINCT id, status_pedido, nome_loja, data_horario_pedido, avaliacao
            FROM Pedidos
            WHERE cliente_id = ?
        """ # consulta o banco de dados
        
        # Executa a consulta SQL com o ID do cliente
        cursor.execute(consulta, cliente.id)
        aux = cursor.fetchall()
        
        # Limpa a tabela antes de adicionar novos dados
        tabela.clear()
        
        # Adiciona os resultados da consulta à tabela
        for p in aux:
            tabela.append(p)
    
    # Método para consultar a avaliação de um pedido específico
    def consulta_avaliacao(self, id: int, busca_avaliacao: list) -> None:
        # Consulta SQL para obter a avaliação de um pedido específico
        consulta = """
            SELECT DISTINCT avaliacao
            FROM Pedidos
            WHERE id = ?
        """ # consulta o banco de dados
        
        # Executa a consulta SQL com o ID do pedido
        cursor.execute(consulta, id)
        aux = cursor.fetchall()
        
        # Limpa a lista de busca de avaliações antes de adicionar novos dados
        busca_avaliacao.clear()
        
        # Adiciona os resultados da consulta à lista de busca de avaliações
        for p in aux:
            busca_avaliacao.append(p)
            self.status = p # Atualiza o status do pedido com a avaliação obtida
