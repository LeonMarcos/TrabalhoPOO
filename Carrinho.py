
####################### BANCO DE DADOS ######################

from Conex_SQL import connection



cursor = connection.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################
from types import SimpleNamespace
from Item import Item
from Estabelecimento import Estabelecimento
from Pedido import Pedido
import time

class Carrinho:
    # Atributos e construtor da classe Carrinho
    def __init__(self) -> None:            
        self.lista_carrinho = []
        self.cardapio = []
        self.total = 0
    

    def menu(self, estabelecimento,cliente):
        cliente = cliente
        while True:
            print('\033[H\033[2J')
            estab_aux = Estabelecimento()
            estabelecimento = estabelecimento
            estab_aux.exibe_cardapio(estabelecimento)
            self.convert_lista(estabelecimento)
            
            print('\n1 - Adicionar Item ao Carrinho')
            print('2 - Remover Item do Carrinho')
            print('3 - Exibir Carrinho')
            print('4 - Limpar Carrinho')
            print('5 - Sair') 
            
            opcao = None
            opcao = input('\nDigite a opção desejada:\t')

            if opcao == '1':
                self.add_carrinho()
            
            if opcao == '2':
                self.remove_carrinho()

            if opcao == '3':
                confirma = False
                confirma = self.exibe_carrinho(estabelecimento, cliente)
                if not confirma:
                     return True

            if opcao == '4':
                 self.limpar()

            if opcao == '5':
                 break
        

    def convert_lista(self,estabelecimento):
        estabelecimento = estabelecimento
        consulta = """ SELECT * FROM Itens WHERE loja_id = ?; """ #consulta o banco de dados
        cursor.execute(consulta,estabelecimento.id) 
        tabela = cursor.fetchall()
        aux = [] #tabela auxiliar para receber os dados do tipo pyodbc.Row
        for busca in tabela:
            aux.append(busca)
        self.cardapio = [] #converte 
        for row in aux:
            # Cria um dicionário com os nomes das colunas e valores da linha
            row_dict = {column[0]: value for column, value in zip(cursor.description, row)}
            
            # Cria um SimpleNamespace a partir do dicionário
            row_namespace = SimpleNamespace(**row_dict)
            
            # Adiciona o objeto SimpleNamespace à lista custom_rows
            self.cardapio.append(row_namespace)
        
         
    
    #Método que recebe um item e o adiciona a lista de itens do carrinho
    def add_carrinho(self) -> None:
        nome = input('\nDigite o nome do produto a ser adicionado:\t')
        qtd = int(input('\nDigite a quantidade de produtos a ser adicionado:\t'))
                
        encontrado = False
        for busca in self.cardapio:    #busca o código no cardápio
            if nome == busca.nome:
                    for procura in self.lista_carrinho:   #busca o código no carrinho para não repetir o produto na lista, aumenta apenas a quantidade
                        
                        if nome == procura.nome:
                            procura.quant += qtd
                            encontrado = True
                            
                    if not encontrado:          #se não tiver o código no carrinho, agora ele tem condição de inserir todos os dados
                        busca.quant = qtd
                        self.lista_carrinho.append(busca)                
                        return self.convert_lista
        
    #Método que remove um item desejado (usando nome como critério) do carrinho
    def remove_carrinho(self) -> None:
        nome_item = input("\nDigite o nome do item a ser removido: ")
        item_encontrado = None
        for item in self.lista_carrinho:
            if item.nome == nome_item:
                item_encontrado = item
                break
        if item_encontrado:
            self.lista_carrinho.remove(item_encontrado)
            print(f"O item '{nome_item}' foi removido do carrinho.")
        else:
            print(f"O item '{nome_item}' não foi encontrado no carrinho.")
    
    def limpar(self):
            self.lista_carrinho = []

    #Método que calcula o valor total do carrinho e retorna o valor total
    # def calcula_total(self) -> float:
    #     self.total = 0
    #     for item in self.lista_carrinho:
    #         self.total = self.total + item.preco
        
    #     return self.total
    
    #Método que exibe as informações do carrinho, iten, número de itens, descrição de cada iten e valor total
    def exibe_carrinho(self, estabelecimento, cliente) -> bool:
        estabelecimento = estabelecimento
        cliente = cliente
        print('\033[H\033[2J')
        print('\n\n------------- CARRINHO -------------\n')
        
        
        self.total = 0
        for p in self.lista_carrinho:
             
            p.subtotal = p.quant * p.preco
            print(f"| {p.nome} - R${p.preco:0.2f} x {p.quant} - R${p.subtotal:0.2f}")
            
            self.total += p.subtotal
        print('\n------------------------------------')    
        print(f"\n| Valor total do carrinho: R${self.total:0.2f}")

        finalizar = input('\nDeseja finalizar o seu pedido?\t (s/n)\t')
        if finalizar == 's':
                print('\033[H\033[2J')
                print('\n| Pedido enviado!')
                time.sleep(2.5)
                self.finalizar_carrinho(estabelecimento, cliente)
                return True
                
                #Deve ser criado um novo número do pedido
                #print(cliente.n_pedido) printar o número antes e depois p/ verificar soma
                # cliente.n_pedido = cliente.n_pedido + 1
                #print(cliente.n_pedido)
                #função de limpar lista do carrinho
                # pedido1.exibe(carrinho)
                # pedido1.avaliar()
                
                
        elif 'n':
                print('\033[H\033[2J')
                print("\n| Você pode revisar seu pedido!")
                time.sleep(2)
                return True

    def finalizar_carrinho(self, estabelecimento, cliente):
         estabelecimento = estabelecimento
         cliente = cliente
         pedido_aux = Pedido()
         pedido_aux.cria_pedido(self.lista_carrinho, estabelecimento, cliente)

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
