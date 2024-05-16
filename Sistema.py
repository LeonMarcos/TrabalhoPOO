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
        
    def verifica_login_cliente(self, cliente: Type[Cliente]) -> bool:
        cliente_login = cliente
        if cliente_login.get_email() == None and cliente_login.get_senha() == None:
           login_email = input("Digite seu e-mail: ")
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
    
    # método que cria um cadastro para cliente   
    def cria_cadastro_cliente(self, cliente: Type[Cliente]) -> None:
        cliente = cliente
        cliente_existente = None
        cliente_existente = self.verifica_login_cliente(cliente)
        if cliente_existente == False:
            self.__lista_de_clientes.append(cliente)
            print("O cadastro foi realizado com sucesso")
        else:
            print("O cliente já está cadastrado")
            
'''def main():
    
        sistemaum = Sistema()    
        clienteum = Cliente()
        clienteum.cria_Usuario()
        print("\n")
        print(clienteum.get_nome())
        print(clienteum.get_endereco())
        print(clienteum.get_telefone())
        print(clienteum.get_email())
        print(clienteum.get_cpf_cnpj())
        print(clienteum.get_senha())
        sistemaum.cria_cadastro_cliente(clienteum)
        
        sistemaum.cria_cadastro_cliente(clienteum)
        
        clientedois = Cliente()
        clientedois = clienteum
        sistemaum.cria_cadastro_cliente(clientedois)
        
        clientetres = Cliente()
        sistemaum.cria_cadastro_cliente(clientetres)
        
        
        
main()'''