# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from abc import ABC, abstractmethod
import math
import re


class Usuario:
    #Constantes
    padrao_telefone = r"\d{11,}$"
    # Atributos e construtor da classe Usuario
    def __init__(self) -> None:
        self._nome = None
        self._endereco = None
        self._telefone = None
        self._email = None
        self._cpf_cnpj = None
        self._senha = None
        self._saldo = None
        
    # método get nome responsável por retornar o nome do usuario    
    def get_nome(self) -> str:
        return self._nome
        
    # método get endereco responsável por retornar o endereco do usuario    
    def get_endereco(self) -> str:
        return  self._endereco
    
    # método get telefone responsável por retornar o telefone do usuario    
    def get_telefone(self) -> int:
        return  self._telefone
    
    # método get email responsável por retornar o email do usuario    
    def get_email(self) -> str:
        return  self._email
        
    # método get cpf_cnpj responsável por retornar o cpf_cnpj do usuario    
    def get_cpf_cnpj(self) -> int:
        return  self._cpf_cnpj
    
    # método get senha responsável por retornar a senha do usuario
    def get_senha(self) -> str:
        return  self._senha

    # método get saldo responsável por retornar o saldo do usuario
    def atualiza_saldo(self, saldo) -> None:
        self._saldo = saldo
    
    # método get saldo responsável por retornar o saldo do usuario
    def get_saldo(self) -> float:
        return  self._saldo
    
    # método abstrato responsavel por criar o Usuario
    def cria_Usuario(self) -> None:
        
        #Tratamento de exceção para o nome
        while True:
            try:
                self._nome = str(input("Digite seu nome: "))
                break
            except:
                print("Nome inválido. Por favor digite novamente")
                
        #Tratamento de exceção para o endereco
        while True:
            try:
                self._endereco = str(input("Digite seu endereco: "))
                break
            except:
                print("Endereço inválido. Por favor digite novamente")
                
        #Tratamento de exceção para o telefone
        while True:
            try:
                self._telefone = int(input("Digite seu telefone: "))
                break
            except:
                print("Número de telefone inválido. Por favor digite novamente")
        
        #Tratamento de exceção para o email
        while True:
            try:
                self._email = str(input("Digite seu email: "))
                break
            except:
                print("E-mail inválido. Por favor digite novamente")
        
        #Tratamento de exceção para o cpf_cnpj
        while True:
            try:
                self._cpf_cnpj = int(input("Digite seu cpf_cnpj: "))
                break
            except:
                print("Número de cpf_cnpj inválido. Por favor digite novamente")
        
        #Tratamento de exceção para o senha
        while True:
            try:
                self._senha = str(input("Digite seu senha: "))
                break
            except:
                print("Senha inválida. Por favor digite novamente")
        
        

"""def main():
    usuarioum = Usuario()
    usuarioum.cria_Usuario()
    print("\n")
    print(usuarioum.get_nome())
    print(usuarioum.get_endereco())
    print(usuarioum.get_telefone())
    print(usuarioum.get_email())
    print(usuarioum.get_cpf_cnpj())
    print(usuarioum.get_senha())
    
main()"""