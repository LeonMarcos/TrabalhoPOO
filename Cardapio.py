# import Item

class Cardapio:
    
    def __init__(self):
        self.itens = []
        
    def add_cardapio(self,Item):
        
        item = Item
        self.itens.append(item)
       
    def exibe_itens(self):
        
        print('\n ----------------- CARDÁPIO -----------------\n')
        print('Cód | Produto | Valor (R$)')
        print('----------------------------\n')
        
        for p in self.itens:
            print(f"{p.cod}  | {p.nome} |  R${p.preco:0.2f}")
        
        print('\n----------------------------------------------\n')