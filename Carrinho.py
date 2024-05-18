# import Cardapio


from typing import Type
from Item import Item

class Carrinho:
    # Atributos e construtor da classe Carrinho
    def __init__(self, nome:str) -> None:            
        self.nome = nome
        self.lista_de_itens = []
        self.total = 0
    
    #Método que recebe um item e o adiciona a lista de itens do carrinho
    def add_carrinho(self, item: Type[Item]) -> None:
        self.lista_de_itens.append(item)
        print("\nAdcionado com sucesso!")
        
    #Método que remove um item desejado (usando nome como critério) do carrinho
    def remove_carrinho(self) -> None:
        nome_item = input("\nDigite o nome do item a ser removido: ")
        item_encontrado = None
        for item in self.lista_de_itens:
            if item.nome == nome_item:
                item_encontrado = item
                break
        if item_encontrado:
            self.lista_de_itens.remove(item_encontrado)
            print(f"O item '{nome_item}' foi removido do carrinho.")
        else:
            print(f"O item '{nome_item}' não foi encontrado no carrinho.")
    
    #Método que calcula o valor total do carrinho e retorna o valor total
    def calcula_total(self) -> float:
        self.total = 0
        for item in self.lista_de_itens:
            self.total = self.total + item.preco
        
        return self.total
    
    #Método que exibe as informações do carrinho, iten, número de itens, descrição de cada iten e valor total
    def exibe_carrinho(self) -> None:
        contador = 0
        if not self.lista_de_itens:
            print("\nO carrinho está vazio.")
        else:
            print("\nO carrinho possui os seguintes itens: ")
            for item_carrinho in self.lista_de_itens:
                contador = contador+1
                print(contador,"-", f"Nome: {item_carrinho.nome}, Descrição: {item_carrinho.descricao}, Preço: {item_carrinho.preco:.2f} reais.")
        print("\nAo todo o carrinho possui", contador, "itens")
        print(f"O valor total é de: {self.calcula_total():.2f} reais ")

if __name__ == "__main__":
            nome = 'Leon'
            carrinho = Carrinho(nome)
            
            item = Item()
            item.cria_item()
            
            itemm = Item()
            itemm.cria_item()
            
            itemmm = Item()
            itemmm.cria_item()
            
            carrinho.add_carrinho(item)
            carrinho.add_carrinho(itemm)
            carrinho.add_carrinho(itemmm)
            carrinho.exibe_carrinho()
            carrinho.calcula_total()
            carrinho.remove_carrinho()
            carrinho.remove_carrinho()
            carrinho.exibe_carrinho()
