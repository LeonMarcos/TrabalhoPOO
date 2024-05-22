# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:09:00 2024

@author: lmfel
"""
import time
from click import pause
from Usuario import Usuario
from Cliente import Cliente
from Estabelecimento import Estabelecimento
from Sistema import Sistema
from typing import Type


if __name__ == "__main__":

    #Classes
    sistema1 = Sistema()
    cliente1 = Cliente()
    estabelecimento1 = Estabelecimento()
    
    def menu_inicial():

        #Variáveis auxiliares
        conta_existe = None
        opcao = None
        
        while True:
            print('\033[H\033[2J')
            print("-----------------  UFMGFood  -----------------\n")
            print("\n| O melhor aplicativo de delivery da UFMG!\n")
            print('1 - Login')
            print('2 - Cadastrar')
            print('9 - Sair')
            
            conta_existe = input("\n\nDigite a opção desejada:\t")
            
            if conta_existe == '1':
                
                login = sistema1.login_cliente(cliente1)
                
                if login == True:
                        menu_app()
                        break

            if conta_existe == '2':

                opcao = None
                while opcao != '9':
                    print('\033[H\033[2J')
                    print('--------------  Cadastro   --------------\n')
                    print('\n1 - Cadastrar como cliente')
                    print('2 - Cadastrar como estabelecimento')
                    print('9 - Voltar')
                    opcao = input("\n\nDigite a opção desejada:\t")
                    
                    if opcao == '1':
                        cliente1.cria_Usuario()
                        sistema1.cria_cadastro_cliente(cliente1)
                        print('\033[H\033[2J')
                        break

                    if opcao == '2':
                        estabelecimento1.cria_Usuario()
                        sistema1.cria_cadastro_estabelecimento(estabelecimento1)  
                        break

                    if opcao == '9':
                        print('\033[H\033[2J')
                        break
                    
            if conta_existe == '9':
                break

    def menu_app():
        print('entrou no menu')

    menu_inicial()
        