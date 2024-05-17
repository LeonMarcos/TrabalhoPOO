# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:35:05 2024

@author: lmfel
"""

from Usuario import Usuario
from Cliente import Cliente
from Estabelecimento import Estabelecimento
from typing import Type

class Sistema:
    # Atributos e construtor da classe Sistema
    def __init__(self) -> None:
        self.__lista_de_clientes = []
        self.__lista_de_estabelecimentos = []
        
    # método que verifica se o cliente existe na lista de cliente
    def __verifica_login_cliente(self, cliente: Type[Cliente]) -> bool:
        cliente_login = cliente
        if cliente_login.get_email() == None and cliente_login.get_senha() == None:
           login_email = input("\nDigite seu e-mail: ")
           login_senha = input("Digite sua senha: ")
           for cliente_banco in self.__lista_de_clientes:
               if cliente_banco.get_email() == login_email and \
                   cliente_banco.get_senha() == login_senha:
                       return True    
        else:    
            for cliente_banco in self.__lista_de_clientes:
                if cliente_banco.get_email() == cliente_login.get_email() and \
                    cliente_banco.get_senha() == cliente_login.get_senha():
                        return True
        return False
    
    # método que retorna o cliente
    def login_cliente(self, cliente: Type[Cliente]) -> bool:
        cliente_classe = Cliente()
        login = None
        login = self.__verifica_login_cliente(cliente_classe)
        if login == True:
            print("\nO login foi efetuado com sucesso!")
        else:
            print("\nO login não foi efetuado com sucesso.")
        return login
        
    
    # método que cria um cadastro para cliente   
    def cria_cadastro_cliente(self, cliente: Type[Cliente]) -> None:
        cliente = cliente
        cliente_existente = None
        cliente_existente = self.__verifica_login_cliente(cliente)
        if cliente_existente == False:
            self.__lista_de_clientes.append(cliente)
            print("\nO cadastro foi realizado com sucesso!")
        else:
            print("\nO cliente já está cadastrado.")
            
    # método que verifica se o estabelecimento existe na lista de estabelecimento
    def __verifica_login_estabelecimento(self, estabelecimento: Type[Estabelecimento]) -> bool:
        estabelecimento_login = estabelecimento
        if estabelecimento_login.get_email() == None and estabelecimento_login.get_senha() == None:
           login_email = input("\nDigite seu e-mail: ")
           login_senha = input("Digite sua senha: ")
           for estabelecimento_banco in self.__lista_de_estabelecimentos:
               if estabelecimento_banco.get_email() == login_email and \
                   estabelecimento_banco.get_senha() == login_senha:
                       return True    
        else:    
            for estabelecimento_banco in self.__lista_de_estabelecimentos:
                if estabelecimento_banco.get_email() == estabelecimento_login.get_email() and \
                    estabelecimento_banco.get_senha() == estabelecimento_login.get_senha():
                        return True
        return False
    
    # método que retorna o estabelecimento
    def login_estabelecimento(self, estabelecimento: Type[Estabelecimento]) -> bool:
        estabelecimento_classe = Estabelecimento()
        login = None
        login = self.__verifica_login_estabelecimento(estabelecimento_classe)
        if login == True:
            print("\nO login foi efetuado com sucesso!")
        else:
            print("\nO login não foi efetuado com sucesso.")
        return login
        
    
    # método que cria um cadastro para estabelecimento   
    def cria_cadastro_estabelecimento(self, estabelecimento: Type[Estabelecimento]) -> None:
        estabelecimento = estabelecimento
        estabelecimento_existente = None
        estabelecimento_existente = self.__verifica_login_estabelecimento(estabelecimento)
        if estabelecimento_existente == False:
            self.__lista_de_estabelecimentos.append(estabelecimento)
            print("\nO cadastro foi realizado com sucesso!")
        else:
            print("\nO estabelecimento já está cadastrado.")
                    
    
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
        
        sistemaum.login_estabelecimento(estabelecimentoum)
        
        estabelecimentodois = Estabelecimento()
        sistemaum.login_estabelecimento(estabelecimentodois)
        estabelecimentodois.cria_Usuario()
        sistemaum.cria_cadastro_estabelecimento(estabelecimentodois)
        sistemaum.login_estabelecimento(estabelecimentodois)
        
        