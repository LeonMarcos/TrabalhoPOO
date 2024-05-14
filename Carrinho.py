# import Cardapio

class Carrinho:
    
    def __init__(self):            
        self.lista = []
                
    def menu(self):      
        print('\n1 - Adicionar Item')
        print('2 - Remover Item')
        print('3 - Exibir Carrinho')
        print('4 - Limpar Carrinho')
        print('5 - Sair')  
  
    def add_itens(self,Cardapio):
        # encontrado = False
        # for codigo in self.itens:
            
        #     if codigo.cod == produto.cod:
        #         codigo.quant += produto.quant
        #         encontrado = True
        #         print(codigo.quant)
        #         print(produto.quant)
                
        
        # if not encontrado:
        # self.itens.append(Cardapio.itens)
            
            
            

        cod = int(input('\nDigite o código do produto a ser adicionado:\t'))
        qtd = int(input('\nDigite a quantidade de produtos a ser adicionado:\t'))
        
        # for busca in Cardapio.itens:
        #     if cod == busca.cod:
        #         busca.quant = qtd
        #         self.lista.append(busca)                
        #         return self.lista
        encontrado = False
        for busca in Cardapio.itens:    #busca o código no cardápio
            if cod == busca.cod:
                    for codigo in self.lista:   #busca o código no carrinho para não repetir o produto na lista, aumenta apenas a quantidade
                        
                        if cod == codigo.cod:
                            codigo.quant += qtd
                            encontrado = True
                            
                    if not encontrado:          #se não tiver o código no carrinho, agora ele tem condição de inserir todos os dados
                        busca.quant = qtd
                        self.lista.append(busca)                
                        return self.lista
                                 
        
    def exibe_car(self):
        # print(f"\nNúmero do pedido: {self.numero}")
        # print(f"Data do pedido: {self.data}")
        # print('\n-------------------------------')
        # print('\nItens do pedido:')
        print('\n\n------------- CARRINHO -------------\n')
        
        
        total = 0
        for p in self.lista:
            
            subtotal = p.quant * p.preco
            print(f"| {p.nome} - R${p.preco:0.2f} x {p.quant} - R${subtotal:0.2f}")
            
            total += subtotal
        print('\n------------------------------------')    
        print(f"\nValor total do pedido: R${total:0.2f}")
        
    def limpar(self):
        self.lista = []