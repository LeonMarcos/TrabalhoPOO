####################### BANCO DE DADOS ######################

from Conex_SQL import connection

cursor = connection.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################

import time
from Carrinho import Carrinho
from Usuario import Usuario
from Cliente import Cliente
from Estabelecimento import Estabelecimento
from typing import Type
from Utilitarios import limpar_tela

dados_usuario = None

class Sistema:
    # Atributos e construtor da classe Sistema
    def __init__(self) -> None:
        self.__lista_de_usuarios = []
        self.__lista_de_estabelecimentos = []

    def salva_dados_usuario(self, usuario:Type[Usuario]) -> None:
        self.dados_usuario = usuario
         
    def retorna_dados_usuario(self) -> Usuario:
         return self.dados_usuario
           
    # método que verifica se o usuário existe na lista de usuários
    def __verifica_login_usuario(self, usuario:Type[Usuario]) -> bool:
        usuario_login = usuario
        consulta = """ SELECT * FROM Usuarios WHERE tipo = ?; """ #consulta o banco de dados
        cursor.execute(consulta, usuario.tipo) 
        tabela = cursor.fetchall()
        self.__lista_de_usuarios  = []
        for busca in tabela:
            self.__lista_de_usuarios.append(busca)
        
        if usuario_login.get_email() == None and usuario_login.get_senha() == None:
           login_email = input("\nDigite seu e-mail:\t")
           login_senha = input("Digite sua senha:\t")
           
           for usuario_banco in self.__lista_de_usuarios:
               if usuario_banco.email == login_email and \
                   usuario_banco.senha == login_senha:
                        self.salva_dados_usuario(usuario_banco) #tem que retornar os dados do cliente tbm e não só se o login foi aprovado
                        return True
                           
        else:         
            for usuario_banco in self.__lista_de_usuarios :
                    
                if usuario_banco.email == usuario_login._email:
                    print('| Email já cadastrado por outro usuário!')
                    time.sleep(3)
                    limpar_tela()
                    return True 
                
                if usuario_banco.cpf_cnpj == usuario_login._cpf_cnpj: #alterei para email OU cpf/cnpj iguais
                    print('| CPF já cadastrado por outro usuário!')
                    time.sleep(3)
                    limpar_tela()
                    return True
                     
        return False
    
    # método que retorna o usuário
    def login_usuario(self, usuario:Type[Usuario]) -> bool:
        
        limpar_tela()
        print("---------------- Login ----------------\n")
        login = None 
        login = self.__verifica_login_usuario(usuario)
        print('\n---------------------------------------')
        
        if login == True:
            print("\n| O login foi efetuado com sucesso!")
            time.sleep(3)
            limpar_tela()
        else:
            login = False
            print("\n| O login não é válido.")
            time.sleep(3)
            limpar_tela()

        return login        
    
    # método que cria um cadastro para cliente   
    def cria_cadastro_cliente(self, cliente: Type[Cliente]) -> None:
 
        comando = """ INSERT INTO Usuarios(nome, endereco, telefone, email, cpf_cnpj, senha, tipo)
        VALUES
          (?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(comando, cliente._nome, cliente._endereco, cliente._telefone, cliente._email, cliente._cpf_cnpj, cliente._senha, cliente.tipo )
        cursor.commit()
        consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados
        cursor.execute(consulta) 
        tabela = cursor.fetchall()
        self.__lista_de_clientes  = []
        for busca in tabela:
         self.__lista_de_clientes .append(busca)

        print("\n| O cadastro foi realizado com sucesso!")
        time.sleep(3)
        limpar_tela() 
            
    
    # método que cria um cadastro para estabelecimento   
    def cria_cadastro_estabelecimento(self, estabelecimento: Type[Estabelecimento]) -> None:

        comando = """ INSERT INTO Usuarios(nome, endereco, telefone, email, cpf_cnpj, senha, tipo)
        VALUES
          (?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(comando, estabelecimento._nome, estabelecimento._endereco, estabelecimento._telefone, estabelecimento._email, estabelecimento._cpf_cnpj, estabelecimento._senha, estabelecimento.tipo )
        cursor.commit()
        consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados
        cursor.execute(consulta) 
        tabela = cursor.fetchall()
        self.__lista_de_estabelecimentos  = []
        for busca in tabela:
            self.__lista_de_estabelecimentos.append(busca)
        print("\n|O cadastro foi realizado com sucesso!")
        time.sleep(3)
        limpar_tela()
        
            
    # Método que exibe uma lista de estabelecimentos cadastrados e associa cada estabelecimento a um número inteiro diferente
    def exibe_estabelecimentos(self, cliente:Type[Cliente]) ->bool:
        carrinho_aux = Carrinho()
        
        consulta = """ SELECT * FROM Usuarios
                        WHERE tipo = 'Estabelecimento';
           """ #consulta o banco de dados
        cursor.execute(consulta) 
        tabela = cursor.fetchall()
        self.__lista_de_estabelecimentos  = []
        
        for busca in tabela:
            self.__lista_de_estabelecimentos.append(busca)

        if not self.__lista_de_estabelecimentos:
            print("\n| Não existem estabelecimentos cadastrados no aplicativo.")
            limpar_tela()
        else:
            while True:
                lista_numeros = []
                limpar_tela()
                print("\n-----------------  Lista de Estabelecimentos  -----------------\n\n")
                numero = 0
                
                for estab in self.__lista_de_estabelecimentos:
                    numero = numero + 1
                    print(estab.id,"–", estab.nome)
                    lista_numeros.append(estab.id)
                    print("-"*50)
                print("\n0 – Voltar.") 
                
                navegar = 0
                try:
                    navegar = int(input('\n\nDigite a opção desejada:\t'))
                except ValueError:
                    print("\n(Entrada Inválida!)")
                    time.sleep(2)
                    continue
                
                if (navegar == 0 or navegar in lista_numeros):
                    for proc in self.__lista_de_estabelecimentos:
                        if proc.id == navegar:
                                limpar_tela()
                                car = carrinho_aux.menu(proc, cliente)
                                if car == False: # nessa condição o carrinho não está finalizado e mantém o menu lista de estabelecimentos aberto
                                    pass
                                if car == True: # quando finalizar o carrinho, será possível voltar ao menu inicial
                                    return False

                    if navegar == 0:
                        return False
                else:
                    print("\n(Entrada Inválida!)")
                    time.sleep(2)