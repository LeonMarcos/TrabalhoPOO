# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:09:00 2024

@author: lmfel
"""

from Usuario import Usuario
from Cliente import Cliente
from Estabelecimento import Estabelecimento
from Sistema import Sistema
from typing import Type


if __name__ == "__main__":

    #Classes
    sistema = Sistema()
    cliente = Cliente()
    
    #Variáveis auxiliares
    conta_existe = None
    
    print("Seja bem vinde ao UFMGFood, o melhor aplicativo de delivery da UFMG!")
    print("\nDigite 1 para realizar login caso já possua uma conta existente.")
    print("Digite qualquer outra tecla para cadastrar um novo usuário caso não possua conta.")
    conta_existe = int(input(": "))
    
    if conta_existe == 1:
        
        while True:
            if sistema.verifica_login_cliente(cliente) == True:
                print("O login foi realizado com sucesso")
                break
            else:
                print("O login não foi realizado com sucesso. Por favor digite seus dados novamente.")
    
    else:
        print("Em construção")
    
    
 