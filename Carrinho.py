
####################### BANCO DE DADOS ######################

from inspect import _void
from Conex_SQL import connection



cursor = connection.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################
from types import SimpleNamespace
from Item import Item
from Estabelecimento import Estabelecimento
from Pedido import Pedido
import time
import os

class Carrinho:
    # Atributos e construtor da classe Carrinho
    def __init__(self) -> None:            
        self.lista_carrinho = []
        self.cardapio = []
        self.total = 0
    

    def menu(self, estabelecimento,cliente):
        cliente = cliente
        veri = None
        while True:
            os.system('cls')
            estab_aux = Estabelecimento()
            estabelecimento = estabelecimento
            veri = estab_aux.exibe_cardapio(estabelecimento)
            if veri == False:
                 return False
            self.convert_lista(estabelecimento)
            
            
            print('\n1 - Adicionar Item ao Carrinho')
            print('2 - Remover Item do Carrinho')
            print('3 - Exibir Carrinho')
            print('4 - Limpar Carrinho')
            print('0 - Voltar') 
            
            opcao = None
            opcao = input('\nDigite a opção desejada:\t')

            if opcao == '1':
                self.add_carrinho(estabelecimento)
            
            if opcao == '2':
                self.remove_carrinho()

            if opcao == '3':
                os.system('cls')
                confirma = False
                confirma = self.exibe_carrinho(estabelecimento, cliente)
                if confirma == True:
                    return True
                if confirma == False:
                    pass

            if opcao == '4':
                 self.limpar()

            if opcao == '0':
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
    def add_carrinho(self,estabelecimento) -> None:
        nome = input('\nDigite o nome do produto a ser adicionado:\t')
        qtd = int(input('\nDigite a quantidade de produtos a ser adicionado:\t'))
                
        encontrado = False
        ok = True
        for busca in self.cardapio:    #busca o código no cardápio
            if nome == busca.nome:
                    for procura in self.lista_carrinho:   #busca o código no carrinho para não repetir o produto na lista, aumenta apenas a quantidade
                        
                        if procura.loja_id != busca.loja_id:
                             os.system('cls')
                             print('| Você não pode selecionar itens de lojas diferentes')
                             time.sleep(2)
                             ok = False
                             break

                        if nome == procura.nome and ok == True:
                            procura.quant += qtd
                            encontrado = True
                    
                    
                            
                    if not encontrado and ok == True:          #se não tiver o código no carrinho, agora ele tem condição de inserir todos os dados
                        busca.estab_car = estabelecimento.nome
                        busca.quant = qtd
                        self.lista_carrinho.append(busca)                
                        return self.convert_lista
        
    #Método que remove um item desejado (usando nome como critério) do carrinho
    def remove_carrinho(self) -> None:
        if not self.lista_carrinho:
             print('\n| O carrinho está vazio!')
             time.sleep(3)
        if self.lista_carrinho:
            nome_item = input("\nDigite o nome do item a ser removido: ")
            item_encontrado = None
            for item in self.lista_carrinho:
                if item.nome == nome_item:
                    item_encontrado = item
                    break
            if item_encontrado:
                self.lista_carrinho.remove(item_encontrado)
                print(f"\n| O item '{nome_item}' foi removido do carrinho.")
                time.sleep(3)
            else:
                print(f"\n| O item '{nome_item}' não foi encontrado no carrinho.")
                time.sleep(3)
    def limpar(self):
        if not self.lista_carrinho:
             print('\n| O carrinho está vazio!')
             time.sleep(3)
        if self.lista_carrinho:
            print('\n| Retirando os itens do carrinho...')
            time.sleep(3)
            self.lista_carrinho = []
    
    #Método que exibe as informações do carrinho, iten, número de itens, descrição de cada iten e valor total
    def exibe_carrinho(self, estabelecimento, cliente) -> bool:
        estabelecimento = estabelecimento
        cliente = cliente
        os.system('cls')
        print('\n\n------------- CARRINHO -------------')
        for p in self.lista_carrinho:
             estab_car = p.estab_car
        
        if not self.lista_carrinho:
             print('\n| Vazio!\n')
             print('-'*36,'\n')
             input('\nPressione ENTER para voltar.\t')
             return False

        
        if self.lista_carrinho:
            print(f"| {estab_car}")
            print('-'*36,'\n')
            self.total = 0
            for p in self.lista_carrinho:
                p.estab_id = estabelecimento.id
                p.cliente_id = cliente.id
                p.endereco = cliente.endereco
                p.cliente_nome = cliente.nome
                p.estab_nome = estabelecimento.nome

                p.subtotal = p.quant * p.preco
                print(f"| {p.nome} - R${p.preco:0.2f} x {p.quant} - R${p.subtotal:0.2f}")
                
                self.total += p.subtotal
            print('\n------------------------------------')    
            print(f"\n| Valor total do carrinho: R${self.total:0.2f}")
            if estab_car != estabelecimento.nome:
                input('\nPressione ENTER para voltar.\t')
            if estab_car == estabelecimento.nome:
                finalizar = input('\nDeseja finalizar o seu pedido?\t (s/n)\t')
                if finalizar == 's':
                        os.system('cls')
                        print('\n| Pedido enviado!')
                        time.sleep(2.5)
                        self.finalizar_carrinho(cliente)
                        return True
                        
                elif 'n':
                        os.system('cls')
                        print("\n| Você pode revisar seu pedido!")
                        time.sleep(2)
                        return False

    def finalizar_carrinho(self,cliente):
        #  estabelecimento = estabelecimento
         cliente = cliente
         pedido_aux = Pedido()
         pedido_aux.cria_pedido(self.lista_carrinho,cliente)

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
