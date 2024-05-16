# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:18:22 2024

"""

from Usuario import Usuario

class Cliente(Usuario):
    
    def __init__(self):
        super().__init__()
        self.__cartao = None
        
        
    def cria_cartao(self) -> None:
        #Tratamento de exceção para o cartao
        while True:
            try:
                self.__cartao = int(input("Digite o número do cartao: "))
                break
            except:
                print("Número do cartao inválido. Por favor digite novamente")
    
'''def main():
    
        clienteum = Cliente()
        clienteum.cria_Usuario()
        print("\n")
        print(clienteum.get_nome())
        print(clienteum.get_endereco())
        print(clienteum.get_telefone())
        print(clienteum.get_email())
        print(clienteum.get_cpf_cnpj())
        print(clienteum.get_senha())
        
main()'''
