# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:18:22 2024

"""

from Usuario import Usuario
from Pedido import Pedido
from typing import Type

class Cliente(Usuario):
    #Atributos de Cliente
    def __init__(self):
        super().__init__()
        self.__cartao = None
        
    #Método responsável por cadastrar um número de cartao
    def cria_cartao(self) -> None:
        #Tratamento de exceção para o cartao
        while True:
            try:
                self.__cartao = int(input("Digite o número do cartao: "))
                break
            except:
                print("Número do cartao inválido. Por favor digite novamente")
    #Método que cria um objeto da classe Pedido e realiza um pedido (INCOMPLETO)
    def realiza_pedido(self):
        pedido = Pedido(self.get_nome())
        
    
if __name__ == "__main__":
    
        clienteum = Cliente()
        clienteum.cria_Usuario()
        print("\n")
        print(clienteum.get_nome())
        print(clienteum.get_endereco())
        print(clienteum.get_telefone())
        print(clienteum.get_email())
        print(clienteum.get_cpf_cnpj())
        print(clienteum.get_senha())
        

