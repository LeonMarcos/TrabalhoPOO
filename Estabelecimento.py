# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:04:34 2024

@author: lmfel
"""

from Usuario import Usuario
from Item import Item

class Estabelecimento(Usuario):
    # Atributos e construtor da classe Estabelecimento
    def __init__(self):
        super().__init__()
        self.__horario_funcio = [None, None]  # Inicializando com None para indicar horários indefinidos
        self.__cardapio = []
        
    #Método que define o horário de funcionamento do Estabelecimento
    def define_horario(self) -> None:
        # Tratamento de exceção para o horário
        abertura = input("\nDigite o horário de abertura de seu estabelecimento: ")
        fechamento = input("Digite o horário de fechamento de seu estabelecimento: ")
        self.__horario_funcio[0] = abertura
        self.__horario_funcio[1] = fechamento
    
    #Método que retorna o vetor de horário de funcionamento. O primeiro elemento é o horário de abertura e o segundo é o horário de fechamento.
    def get_horario(self) -> list:
        return self.__horario_funcio
    
    #Método que verifica se um item já existeno cardapio. Se o item existir, retorna True.
    def __verifica_item_cardapio(self, nome_item: str) -> bool:
        for item_cardapio in self.__cardapio:
            if item_cardapio.nome == nome_item:
                return True
        return False
    
    #Método que cadastra item no cardápio. O método só cadas um item no cadárpio caso ele seja novo.
    def cadastra_item(self) -> None:
        item = Item()
        item.cria_item() #Os itens só podem ser criados dentro dessa função.
        nome_item = item.nome
        if not self.__verifica_item_cardapio(nome_item):
            self.__cardapio.append(item)
            print("\nO item foi cadastrado com sucesso!")
        else:
            print("\nO item solicitado já está cadastrado.")
    
    #Método que exibe os itens cadastrados no cardápio.
    def exibe_cardapio(self) -> None:
        if not self.__cardapio:
            print("\nO cardápio está vazio.")
        else:
            print("\nO cardápio possui os seguintes itens: ")
            for item_cardapio in self.__cardapio:
                print(f"Nome: {item_cardapio.nome}, Descrição: {item_cardapio.descricao}, Preço: {item_cardapio.preco:.2f} reais.")
    
        #Método que remove um item desejado do cardápio com base no nome.
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
    
    #método que retorna um item escolhido do cardápio
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
        
