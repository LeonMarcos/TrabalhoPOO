# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:35:05 2024

@author: lmfel
"""
#############################################################
import pyodbc 

dados_conexao = ( 
    "Driver={SQL Server};" #nome padrão quando se utiliza o SQL
    "Server=localhost\SQLEXPRESS;" #nome do seu servidor igual mostrado no SQL
    "Database=UFMGFood;" #nome do projeto criado
)
conexao = pyodbc.connect(dados_conexao)
#print ('Conexão bem sucedida')

cursor = conexao.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################

from Cliente import Cliente
from Estabelecimento import Estabelecimento
from typing import Type
import time

class Sistema:
    # Atributos e construtor da classe Sistema
    def __init__(self) -> None:
        self.__lista_de_clientes = []
        self.__lista_de_estabelecimentos = []
        self.__numeros_estabelecimentos = []
        
    # método que verifica se o cliente existe na lista de cliente
    def __verifica_login_cliente(self, cliente: Type[Cliente]) -> bool:
        cliente_login = cliente
        consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados
        cursor.execute(consulta) 
        tabela = cursor.fetchall()
        self.__lista_de_clientes  = []
        for busca in tabela:
            self.__lista_de_clientes.append(busca)
        
        if cliente_login.get_email() == None and cliente_login.get_senha() == None:
           login_email = input("\nDigite seu e-mail: ")
           login_senha = input("Digite sua senha: ")
           for cliente_banco in self.__lista_de_clientes:
               if cliente_banco.email == login_email and \
                   cliente_banco.senha == login_senha:
                       return True
                           
        else:         
            for cliente_banco in self.__lista_de_clientes :
                if cliente_banco.email == cliente_login._email:
                    print('Email já cadastrado por outro usuário!')
                    time.sleep(3)
                    print('\033[H\033[2J') 
                    return True 
                
                if cliente_banco.cpf_cnpj == cliente_login._cpf_cnpj: #alterei para email OU cpf/cnpj iguais
                    print('CPF já cadastrado por outro usuário!')
                    time.sleep(3)
                    print('\033[H\033[2J') 
                    return True
                     
        return False
        
    
    # método que retorna o cliente
    def login_cliente(self, cliente: Type[Cliente]) -> bool:
        
        print('\033[H\033[2J')
        cliente_classe = Cliente()       
        print(f"-------------- Login {type(cliente_classe).__name__}  --------------\n")
        login = None 
        login = self.__verifica_login_cliente(cliente_classe)
        print('\n---------------------------------------')
        
        if login == True:
            print("\n|O login foi efetuado com sucesso!")
            time.sleep(3)
            print('\033[H\033[2J') 
        else:
            login = False
            print("\n|O login não é válido.")
            time.sleep(3)
            print('\033[H\033[2J') 
            
        return login
        
    
    # método que cria um cadastro para cliente   
    def cria_cadastro_cliente(self, cliente: Type[Cliente]) -> None:
        cliente = cliente
        cliente_existente = None
        cliente_existente = self.__verifica_login_cliente(cliente)
        if cliente_existente == False:
            comando = """ INSERT INTO Usuarios(nome, endereco, telefone, email, cpf_cnpj, senha)
            VALUES
              (?, ?, ?, ?, ?, ?)"""
            cursor.execute(comando, cliente._nome, cliente._endereco, cliente._telefone, cliente._email, cliente._cpf_cnpj, cliente._senha )
            cursor.commit()
            consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados
            cursor.execute(consulta) 
            tabela = cursor.fetchall()
            self.__lista_de_clientes  = []
            for busca in tabela:
             self.__lista_de_clientes .append(busca)

            print("\n|O cadastro foi realizado com sucesso!")
            time.sleep(3)
            print('\033[H\033[2J') 

        else:
            #cliente já cadastrado - Resposta ao usuário na função verifica_login
            pass
            
    # método que verifica se o estabelecimento existe na lista de estabelecimento
    def __verifica_login_estabelecimento(self, estabelecimento: Type[Estabelecimento]) -> bool:
        estabelecimento_login = estabelecimento
        consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados
        cursor.execute(consulta) 
        tabela = cursor.fetchall()
        self.__lista_de_estabelecimentos  = []
        for busca in tabela:
            self.__lista_de_estabelecimentos.append(busca)
        if estabelecimento_login.get_email() == None and estabelecimento_login.get_senha() == None:
           login_email = input("\nDigite seu e-mail: ")
           login_senha = input("Digite sua senha: ")
           for estabelecimento_banco in self.__lista_de_estabelecimentos:
               if estabelecimento_banco.email == login_email and \
                   estabelecimento_banco.senha == login_senha:
                       return True    
        else:    
            for estabelecimento_banco in self.__lista_de_estabelecimentos:
                if estabelecimento_banco.email == estabelecimento_login._email:
                     print('Email já cadastrado por outro usuário!')
                     time.sleep(3)
                     print('\033[H\033[2J') 
                     return True 
                if estabelecimento_banco.cpf_cnpj == estabelecimento_login._cpf_cnpj: #alterei para email ou cpf/cnpj iguais
                    print('CNPJ já cadastrado por outro usuário!')
                    time.sleep(3)
                    print('\033[H\033[2J') 
                    return True
        return False
    
    # método que retorna o estabelecimento
    def login_estabelecimento(self, estabelecimento: Type[Estabelecimento]) -> bool:
        print('\033[H\033[2J')
        print("\n-------------- Login Estabelecimento  --------------\n")
        estabelecimento_classe = Estabelecimento()
        login = None
        login = self.__verifica_login_estabelecimento(estabelecimento_classe)
        print('\n---------------------------------------')
        if login == True:
            print("\n|O login foi efetuado com sucesso!")
            time.sleep(3)
            print('\033[H\033[2J') 
        else:
            print("\n|O login não é válido.")
            time.sleep(3)
            print('\033[H\033[2J')
            
            
        return login
        
    
    # método que cria um cadastro para estabelecimento   
    def cria_cadastro_estabelecimento(self, estabelecimento: Type[Estabelecimento]) -> None:
        estabelecimento = estabelecimento
        estabelecimento_existente = None
        estabelecimento_existente = self.__verifica_login_estabelecimento(estabelecimento)
        if estabelecimento_existente == False:
            comando = """ INSERT INTO Usuarios(nome, endereco, telefone, email, cpf_cnpj, senha)
            VALUES
              (?, ?, ?, ?, ?, ?)"""
            cursor.execute(comando, estabelecimento._nome, estabelecimento._endereco, estabelecimento._telefone, estabelecimento._email, estabelecimento._cpf_cnpj, estabelecimento._senha )
            cursor.commit()
            consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados
            cursor.execute(consulta) 
            tabela = cursor.fetchall()
            self.__lista_de_estabelecimentos  = []
            for busca in tabela:
                self.__lista_de_estabelecimentos.append(busca)
            print("\n|O cadastro foi realizado com sucesso!")
            time.sleep(3)
            print('\033[H\033[2J') 
        else:
            #estabelecimento já cadastrado - Resposta ao usuário na função verifica_login
            pass
            
    # Método que exibe uma lista de estabelecimentos cadastrados e associa cada estabelecimento a um número inteiro diferente
    def exibe_estabelecimentos(self) ->"Estabelecimento":
        numero = 0
        if not self.__lista_de_estabelecimentos:
            print("\nNão existem estabelecimento cadastradas no aplicativo.")
        else:
            print("\nLista de estabelecimentos cadastrados em nosso aplicativo: ")
            for estabelecimento in self.__lista_de_estabelecimentos:
                numero = numero +1
                print(numero,"-", f"Nome: {estabelecimento.get_nome(),}")
                self.__numeros_estabelecimentos.append(numero)
        
            
if __name__ == "__main__":
    
        sistemaum = Sistema()    
        estabelecimentoum = Estabelecimento()
        
        estabelecimentoum.cria_Usuario()
        print("\n")
        print(estabelecimentoum.get_nome())
        print(estabelecimentoum.get_endereco())
        print(estabelecimentoum.get_telefone())
        print(estabelecimentoum.get_email())
        print(estabelecimentoum.get_cpf_cnpj())
        print(estabelecimentoum.get_senha())
        
        sistemaum.cria_cadastro_estabelecimento(estabelecimentoum) 
        
        estabelecimentodois = Estabelecimento()
        estabelecimentodois.cria_Usuario()
        sistemaum.cria_cadastro_estabelecimento(estabelecimentodois)
        
        sistemaum.exibe_estabelecimentos()
        