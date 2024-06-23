####################### BANCO DE DADOS ######################

# Importa a conexão com o banco de dados do módulo Conex_SQL
from Conex_SQL import connection

# Cria um cursor para executar comandos SQL
cursor = connection.cursor()

#############################################################

# Importações de módulos e classes necessárias
import flet as ft
from Carrinho import Carrinho
from Usuario import Usuario
from Cliente import Cliente
from Estabelecimento import Estabelecimento
from typing import Type
import time

# Variável global para armazenar dados do usuário logado
dados_usuario = None

# Definição da classe Sistema
class Sistema:
    
    # Construtor da classe Sistema
    def __init__(self) -> None:
        # Listas para armazenar usuários e estabelecimentos
        self.__lista_de_usuarios = []
        self.__lista_de_estabelecimentos = []

########################################################################               

    # Método para buscar dados de pedidos finalizados de um pedido específico
    def busca_dados_finalizados(self, pedido: list, info: list):
        # Consulta SQL para buscar informações de pedidos finalizados
        informacoes = """ 
            SELECT DISTINCT id, status_pedido, nome_cliente, data_horario_pedido, avaliacao
            FROM Pedidos
            WHERE id = ?
        """ 
        cursor.execute(informacoes, pedido.id)
        aux = cursor.fetchall()
        info.clear()  # Limpa a lista de informações antes de adicionar novos resultados
        for p in aux:
            info.append(p)

    # Método para buscar dados de pedidos pendentes de um pedido específico
    def busca_dados_pendentes(self, pedido: list, info: list):
        # Consulta SQL para buscar informações de pedidos pendentes
        informacoes = """ 
            SELECT DISTINCT id, status_pedido, nome_cliente, data_horario_pedido
            FROM Pedidos
            WHERE id = ?
        """ 
        cursor.execute(informacoes, pedido.id)
        aux = cursor.fetchall()
        info.clear()  # Limpa a lista de informações antes de adicionar novos resultados
        for p in aux:
            info.append(p)

    # Método para buscar dados de um usuário por sua classe
    def busca_usuario_classe(self, classe: list, dados: list):
        # Consulta SQL para buscar informações de usuário por classe
        busca = """ 
            SELECT * FROM Usuarios
            WHERE id = ?;
        """ 
        cursor.execute(busca, classe.id)
        aux = cursor.fetchall()
        dados.clear()  # Limpa a lista de dados antes de adicionar novos resultados
        for p in aux:
            dados.append(p)
    
    # Método para buscar dados de um usuário por ID
    def busca_usuario_id(self, id: int, dados: list):
        # Consulta SQL para buscar informações de usuário por ID
        busca = """ 
            SELECT * FROM Usuarios
            WHERE id = ?;
        """ 
        cursor.execute(busca, id)
        aux = cursor.fetchall()
        dados.clear()  # Limpa a lista de dados antes de adicionar novos resultados
        for p in aux:
            dados.append(p)

    # Método para buscar dados de pedidos de um pedido específico
    def busca_dados_pedidos(self, pedido: list, info: list):
        # Consulta SQL para buscar informações de pedidos
        informacoes = """ 
            SELECT DISTINCT id, status_pedido, nome_loja, data_horario_pedido
            FROM Pedidos
            WHERE id = ?
        """ 
        cursor.execute(informacoes, pedido.id)
        aux = cursor.fetchall()
        info.clear()  # Limpa a lista de informações antes de adicionar novos resultados
        for p in aux:
            info.append(p)

    # Método para atualizar a interface de avaliação com base nas informações do pedido
    def atualizar_valor_avaliacao(self, info: list, estrelas: list):
        for p in info:
            print(p)
            # Se o pedido não estiver concluído, oculta as estrelas de avaliação
            if p.status_pedido != 'Concluído':
                for estrela in estrelas:
                    estrela.visible = False
            # Se o pedido estiver concluído e houver uma avaliação, seleciona as estrelas correspondentes
            if p.status_pedido == 'Concluído' and p.avaliacao is not None:
                for i, estrela in enumerate(estrelas, start=1):
                    estrela.selected = i <= p.avaliacao
    
    # Método para consultar todos os usuários no banco de dados
    def consulta_usuario(self, lista: list):
        # Consulta SQL para buscar todos os usuários
        consulta = """ 
            SELECT * FROM Usuarios;
        """ 
        cursor.execute(consulta)
        aux = cursor.fetchall()
        lista.clear()  # Limpa a lista antes de adicionar novos resultados
        for p in aux:
            lista.append(p)

    # Método para consultar um usuário pelo ID no início do sistema
    def consulta_usuario_inicio_id(self, classe: list, dados: list):
        # Consulta SQL para buscar informações de um usuário pelo ID
        procura = """ 
            SELECT * FROM Usuarios
            WHERE id = ?;
        """ 
        cursor.execute(procura, classe.id)
        aux = cursor.fetchall()
        dados.clear()  # Limpa a lista de dados antes de adicionar novos resultados
        for p in aux:
            dados.append(p)
            classe = dados
    
    # Método para cadastrar um novo usuário no sistema
    def cadastro(self, page: Type[ft.Page], nome: str, endereco: str, cpf_cnpj: int, telefone: int, email: str, senha: str, tipo_usuario: str, lista_de_usuarios: list, email_cadastro: Type[ft.TextField], cpf_cnpj_cadastro: Type[ft.TextField], nome_cadastro: Type[ft.TextField], senha_cadastro: Type[ft.TextField], endereco_cadastro: Type[ft.TextField], telefone_cadastro: Type[ft.TextField], login_email: str, login_senha: str, cad_msg: Type[ft.Banner]):
        print(telefone)
        cpf_cnpj = int(cpf_cnpj)
        telefone = int(telefone)
        global ok
        ok = True
        
        # Validações dos dados do cadastro
        if email not in lista_de_usuarios:
            email_cadastro.error_text = None
            email_cadastro.error_style = None

        if len(str(cpf_cnpj)) == 11 and cpf_cnpj_cadastro.label == 'CPF' and cpf_cnpj_cadastro not in lista_de_usuarios:
            cpf_cnpj_cadastro.error_text = None
            cpf_cnpj_cadastro.error_style = None

        if len(str(cpf_cnpj)) == 14 and cpf_cnpj_cadastro.label == 'CNPJ' and cpf_cnpj_cadastro not in lista_de_usuarios:
            cpf_cnpj_cadastro.error_text = None
            cpf_cnpj_cadastro.error_style = None
        
        if len(nome.split()) >= 2 and cpf_cnpj_cadastro.label == 'CPF':
            nome_cadastro.error_text = None
            nome_cadastro.error_style = None

        if len(nome.split()) >= 1 and cpf_cnpj_cadastro.label == 'CNPJ':
            nome_cadastro.error_text = None
            nome_cadastro.error_style = None
        
        if '@' in email and '.' in email:
            email_cadastro.error_text = None
            email_cadastro.error_style = None

        if len(senha) >= 6 or len(senha) <= 20:
            senha_cadastro.error_text = None
            senha_cadastro.error_style = None

        if len(endereco) >= 10:
            endereco_cadastro.error_text = None
            endereco_cadastro.error_style = None

        if len(str(telefone)) == 11:
            telefone_cadastro.error_text = None
            telefone_cadastro.error_style = None
        
        # Validações de existência dos dados no banco de dados
        for usuario_banco in lista_de_usuarios:
            if usuario_banco.email == email:
                ok = False
                print('| Email já cadastrado por outro usuário!')
                email_cadastro.error_text = 'Email já cadastrado!'
                email_cadastro.error_style = ft.TextStyle(color='#ff3230', size=15)

            if len(str(cpf_cnpj)) != 11 and cpf_cnpj_cadastro.label == 'CPF':
                ok = False
                cpf_cnpj_cadastro.error_text = 'CPF deve conter 11 dígitos!'
                cpf_cnpj_cadastro.error_style = ft.TextStyle(color='#ff3230', size=15)

            if len(str(cpf_cnpj)) != 14 and cpf_cnpj_cadastro.label == 'CNPJ':
                ok = False
                cpf_cnpj_cadastro.error_text = 'CNPJ deve conter 14 dígitos!'
                cpf_cnpj_cadastro.error_style = ft.TextStyle(color='#ff3230', size=15)

            if len(nome.split()) < 2 and cpf_cnpj_cadastro.label == 'CPF':
                ok = False
                nome_cadastro.error_text = 'Digite Nome e Sobrenome!'
                nome_cadastro.error_style = ft.TextStyle(color='#ff3230', size=15)
            
            if len(nome.split()) < 1 and cpf_cnpj_cadastro.label == 'CNPJ':
                ok = False
                nome_cadastro.error_text = 'Digite um nome!'
                nome_cadastro.error_style = ft.TextStyle(color='#ff3230', size=15)
            
            if '@' not in email or '.' not in email:
                ok = False
                email_cadastro.error_text = 'Digite um email válido!'
                email_cadastro.error_style = ft.TextStyle(color='#ff3230', size=15)

            if len(senha) < 6 or len(senha) > 20:
                ok = False
                senha_cadastro.error_text = 'Senha deve ter entre 6-20 caracteres!'
                senha_cadastro.error_style = ft.TextStyle(color='#ff3230', size=15)
            
            if len(endereco) < 10:
                ok = False
                endereco_cadastro.error_text = 'Endereço deve ter pelo menos 10 caracteres!'
                endereco_cadastro.error_style = ft.TextStyle(color='#ff3230', size=15)

            if len(str(telefone)) != 11:
                ok = False
                telefone_cadastro.error_text = 'Telefone deve conter 11 dígitos!'
                telefone_cadastro.error_style = ft.TextStyle(color='#ff3230', size=15)
                
            if usuario_banco.cpf_cnpj == cpf_cnpj:
                ok = False
                if cpf_cnpj_cadastro.label == 'CPF':
                    cpf_cnpj_cadastro.error_text = 'CPF já cadastrado!'
                    cpf_cnpj_cadastro.error_style = ft.TextStyle(color='#ff3230', size=15)
                    print('| CPF já cadastrado por outro usuário!')
                    
                if cpf_cnpj_cadastro.label == 'CNPJ':
                    cpf_cnpj_cadastro.error_text = 'CNPJ já cadastrado!'
                    cpf_cnpj_cadastro.error_style = ft.TextStyle(color='#ff3230')
                    print('| CNPJ já cadastrado por outro usuário!')
      
        # Se todas as validações passarem, realiza o cadastro no banco de dados
        if ok:
            self.commit_cadastro(cpf_cnpj_cadastro, email_cadastro, telefone_cadastro, nome_cadastro, senha_cadastro, endereco_cadastro, login_email, login_senha, nome, endereco, telefone, email, cpf_cnpj, senha, tipo_usuario)
            page.dialog.open = False
            page.update()
            cad_msg(page)
            page.update()

        page.update()
    
    # Método para realizar o cadastro efetivo no banco de dados
    def commit_cadastro(self, cpf_cnpj_cadastro: Type[ft.TextField], email_cadastro: Type[ft.TextField], telefone_cadastro: Type[ft.TextField], nome_cadastro: Type[ft.TextField], senha_cadastro: Type[ft.TextField], endereco_cadastro: Type[ft.TextField], login_email: str, login_senha: str, nome: str, endereco: str, telefone: str, email: str, cpf_cnpj: str, senha: str, tipo_usuario: str):
        # Limpa erros e valores de campos de entrada
        entradas = [cpf_cnpj_cadastro, email_cadastro, telefone_cadastro, nome_cadastro, senha_cadastro, endereco_cadastro, login_email, login_senha]
        for entrada in entradas:
            entrada.error_text = None
            entrada.error_style = None
            entrada.value = None
        
        # Comando SQL para inserir um novo usuário no banco de dados
        comando = """ 
            INSERT INTO Usuarios(nome, endereco, telefone, email, cpf_cnpj, senha, tipo)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(comando, nome, endereco, telefone, email, cpf_cnpj, senha, tipo_usuario)
        cursor.commit()

    # Método para realizar o login de um usuário
    def login(page, email, senha, lista_de_usuarios, login_email, login_senha, salva_dados_usuario):
        for usuario_banco in lista_de_usuarios:
            global ok
            if usuario_banco.email != email:
                login_email.error_text = 'Email não cadastrado!'
                login_email.error_style = ft.TextStyle(color='#ff3230', size=15)
                login_senha.error_text = None
                login_senha.error_style = None
            
            if usuario_banco.senha != senha:
                ok = False
                login_senha.error_text = 'Senha incorreta!'
                login_senha.error_style = ft.TextStyle(color='#ff3230', size=15)
            
            if usuario_banco.email == email and usuario_banco.senha == senha:
                ok = True
                print('chegou')
                salva_dados_usuario(usuario_banco)
                print('passou')
                                            
                if usuario_banco.tipo == 'Cliente':
                    page.go('/inicio')
                    
                if usuario_banco.tipo == 'Estabelecimento':
                    page.go('/pendentes')

                if ok:
                    entradas = [login_email, login_senha]
                    for entrada in entradas:
                        entrada.error_text = None
                        entrada.error_style = None

        for p in lista_de_usuarios:
            if p.email == email:
                print('foi')
                login_email.error_text = None
                login_email.error_style = None

        page.update()
