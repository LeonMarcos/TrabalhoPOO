# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:04:34 2024

@author: lmfel
"""

from Usuario import Usuario
from Cliente import Cliente
from Item import Item
from typing import Type

class Estabelecimento(Usuario):
    
    def __init__(self):
        super().__init__()
        self.__horario_funcio = [None, None]  # Inicializando com None para indicar horários indefinidos
        self.__cardapio = []
        
    def define_horario(self) -> None:
        # Tratamento de exceção para o horário
        abertura = input("\nDigite o horário de abertura de seu estabelecimento: ")
        fechamento = input("Digite o horário de fechamento de seu estabelecimento: ")
        self.__horario_funcio[0] = abertura
        self.__horario_funcio[1] = fechamento
        
    def get_horario(self) -> list:
        return self.__horario_funcio
    
     
    def __verifica_item_cardapio(self, nome_item: str) -> bool:
        for item_cardapio in self.__cardapio:
            if item_cardapio.nome == nome_item:
                return True
        return False
    
    def cadastra_item(self) -> None:
        item = Item()
        item.cria_item()
        nome_item = item.nome
        if not self.__verifica_item_cardapio(nome_item):
            self.__cardapio.append(item)
            print("\nO item foi cadastrado com sucesso!")
        else:
            print("\nO item solicitado já está cadastrado.")
    
    def exibe_cardapio(self) -> None:
        if not self.__cardapio:
            print("\nO cardápio está vazio.")
        else:
            print("\nO cardápio possui os seguintes itens: ")
            for item_cardapio in self.__cardapio:
                print(f"Nome: {item_cardapio.nome}, Descrição: {item_cardapio.descricao}, Preço: {item_cardapio.preco:.2f} reais.")
        
    def remove_item_cardapio(self) -> None:
        nome_item = input("\nDigite o nome do item a ser removido: ")
        item_encontrado = None
        for item in self.__cardapio:
            if item.nome == nome_item:
                item_encontrado = item
                break
        if item_encontrado:
            self.__cardapio.remove(item_encontrado)
            print(f"O item '{nome_item}' foi removido com sucesso!")
        else:
            print(f"O item '{nome_item}' não foi encontrado no cardápio.")
            
    def escolhe_item(self) -> 'Item':
        nome_item = input("\nDigite o nome do item que deseja escolher: ")
        for item in self.__cardapio:
            if item.nome == nome_item:
                return item
        print(f"\nO item '{nome_item}' não foi encontrado no cardápio.")
        return None
    
if __name__ == "__main__":
    estabelecimentoum = Estabelecimento()
    estabelecimentoum.cria_Usuario()
    print("\n")
    print(estabelecimentoum.get_nome())
    print(estabelecimentoum.get_endereco())
    print(estabelecimentoum.get_telefone())
    print(estabelecimentoum.get_email())
    print(estabelecimentoum.get_cpf_cnpj())
    print(estabelecimentoum.get_senha())
    
    estabelecimentoum.define_horario()
    print(estabelecimentoum.get_horario())
    
    estabelecimentoum.exibe_cardapio()
    estabelecimentoum.cadastra_item()
    estabelecimentoum.cadastra_item()
    estabelecimentoum.cadastra_item()
    estabelecimentoum.exibe_cardapio()
    estabelecimentoum.remove_item_cardapio()
    estabelecimentoum.exibe_cardapio()
        
