####################### BANCO DE DADOS ######################

from Conex_SQL import connection

cursor = connection.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################

import time
from types import SimpleNamespace
from Estabelecimento import Estabelecimento
from Pedido import Pedido
from Utilitarios import limpar_tela, limpar_texto
from Cliente import Cliente

class Carrinho:
    
    #Construtor
    def __init__(self) -> None:
         
        self.lista_carrinho = []
        self.cardapio = []
        self.total = 0

    def menu(self, estabelecimento:Estabelecimento, cliente:Cliente) -> bool:
        
        veri = None
        while True:
            limpar_tela()
            estab_aux = Estabelecimento()
            veri = estab_aux.exibe_cardapio(estabelecimento)
            if veri == False:
                 return False
            self.convert_lista(estabelecimento)
            
            print('\n1 - Adicionar Item ao Carrinho.')
            print('2 - Remover Item do Carrinho.')
            print('3 - Exibir Carrinho.')
            print('4 - Limpar Carrinho.')
            print('0 - Voltar.') 
            
            # Restrições para valores de entrada
            a=1
            while a:
                opcao = None
                opcao = input('\nDigite a opção desejada:\t')
                opcao_limpa = limpar_texto(opcao)
                if (opcao_limpa != '0' and opcao_limpa != '1' and opcao_limpa != '2' and opcao_limpa != '3' and opcao_limpa != '4'):
                    print("\n(Entrada Inválida!)")
                    time.sleep(2)
                    break
    
                elif opcao_limpa == '1':
                    self.add_carrinho(estabelecimento)
                    a=0
                
                elif opcao_limpa == '2':
                    self.remove_carrinho()
                    a=0
    
                elif opcao_limpa == '3':
                    a=0
                    limpar_tela()
                    confirma = False
                    confirma = self.exibe_carrinho(cliente)
                    if confirma == True:
                        return True
                    if confirma == False:
                        pass
    
                elif opcao_limpa == '4':
                    self.limpar()
                    a=0
    
                elif opcao_limpa == '0':
                    a=0
                    return False
            
    def convert_lista(self, estabelecimento:Estabelecimento) -> None:
        
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
    def add_carrinho(self, estabelecimento:Estabelecimento) -> None:
        
        # Restrições de entrada para o nome do produto que esteja no cardápio
        nome_encontrado = 0
        nome = input('\nDigite o nome do produto a ser adicionado:\t')
        nome_limpo = limpar_texto(nome)
        
        for busca in self.cardapio:    #busca o código no cardápio
            if nome_limpo == limpar_texto(busca.nome):
                nome_encontrado = 1
        if nome_encontrado == 0:
            print('\n(Nome Inválido!)')
            time.sleep(2)
            return
            
        # Restrições de entrada para a quantidade do produto
        try:
            qtd = int(input('\nDigite a quantidade do produto a ser adicionado:\t'))
        except ValueError:
            print('\n(Valor Inválido!)')
            time.sleep(2)
            return
        if qtd <= 0:
            print('\n(Valor Inválido!)')
            time.sleep(2)
            return
            
        encontrado = False
        ok = True
        for busca in self.cardapio:   #busca o código no cardápio
            if nome_limpo == limpar_texto(busca.nome):
                    for procura in self.lista_carrinho:   #busca o código no carrinho para não repetir o produto na lista, aumenta apenas a quantidade
                        
                        if procura.loja_id != busca.loja_id:
                             limpar_tela()
                             print('\n| Você não pode selecionar itens de lojas diferentes!')
                             time.sleep(4)
                             ok = False
                             break

                        if nome_limpo == limpar_texto(procura.nome) and ok == True:
                            procura.quant += qtd
                            encontrado = True
                            print('\n| Adicionado ao carrinho.')
                            time.sleep(2.5)
                                  
                    if not encontrado and ok == True:   #se não tiver o código no carrinho, agora ele tem condição de inserir todos os dados
                        busca.estab_car = estabelecimento.nome
                        busca.quant = qtd
                        self.lista_carrinho.append(busca)  
                        print('\n| Adicionado ao carrinho.')
                        time.sleep(2.5)
                        return self.convert_lista
        
    #Método que remove um item desejado (usando nome como critério) do carrinho
    def remove_carrinho(self) -> None:
        
        if not self.lista_carrinho:
             print('\n| O carrinho está vazio!')
             time.sleep(3)
             
        if self.lista_carrinho:
            consulta = "SELECT nome FROM Itens"   #Consulta SQL
            cursor.execute(consulta)   #Executa a consulta
            resultados = cursor.fetchall()   #Recupera os resultados
            nomes_dos_itens = [resultado[0] for resultado in resultados]   #Armazena os nomes na lista
            
            # Restrições de entrada para que o nome do item esteja no sql
            nome_encontrado = 0
            nome = input("\nDigite o nome do produto a ser removido:\t")
            nome_limpo = limpar_texto(nome)
            
            nomes_dos_itens_limpo = [limpar_texto(nome) for nome in nomes_dos_itens]
            
            if nome_limpo in nomes_dos_itens_limpo:
                nome_encontrado = 1
            elif nome_encontrado == 0:
                print('\n(Nome Inválido!)')
                time.sleep(2)
                return
            
            # Verificação se o nome do produto está no carrinho
            item_encontrado = None
            for item in self.lista_carrinho:
                if limpar_texto(item.nome) == nome_limpo:
                    item_encontrado = item
                    break
            if item_encontrado:
                # Restrições de entrada dos valores para quantidades a serem removidas
                try:
                    qtd = int(input('\nDigite a quantidade do produto a ser removido:\t'))
                except ValueError:
                    print('\n(Valor Inválido!)')
                    time.sleep(2)
                    return
                
                if (qtd == 0 or qtd < 0 or (item_encontrado.quant - qtd) < 0):
                    print('\n(Valor Inválido!)')
                    time.sleep(2)
                    return
                
                elif (item_encontrado.quant - qtd) == 0:
                    self.lista_carrinho.remove(item_encontrado)
                    print(f"\n| O item '{item.nome}' foi removido do carrinho.")
                    time.sleep(2.5)
                
                elif (item_encontrado.quant - qtd) > 0:
                    item_encontrado.quant -= qtd
                    print(f"\n| {qtd} '{item.nome}' removido do carrinho.")
                    time.sleep(2.5)
                    
            else:
                print("\n| O item não foi encontrado no carrinho.")
                time.sleep(3)
                
    def limpar(self) -> None:
        
        if not self.lista_carrinho:
            print('\n| O carrinho está vazio!')
            time.sleep(3)
        if self.lista_carrinho:
            print('\n| Retirando os itens do carrinho...')
            time.sleep(3)
            self.lista_carrinho = []
    
    #Método que exibe as informações do carrinho, iten, número de itens, descrição de cada iten e valor total
    def exibe_carrinho(self, cliente:Cliente) -> bool:
        
        a = 1
        while a:
            limpar_tela()
            print('\n\n------------- CARRINHO -------------')
            for p in self.lista_carrinho:
                 estab_car = p.estab_car
            
            if not self.lista_carrinho:
                 print('\n| Vazio.\n')
                 print('-'*36)
                 input('\n\nPressione ENTER para voltar.\t')
                 return False
            
            if self.lista_carrinho:
                print(f"| {estab_car}")
                print('-'*36,'\n')
                self.total = 0
                for p in self.lista_carrinho:
                    p.estab_id = p.loja_id
                    p.cliente_id = cliente.id
                    p.endereco = cliente.endereco
                    p.cliente_nome = cliente.nome
                    p.estab_nome = p.estab_car
    
                    p.subtotal = p.quant * p.preco
                    print(f"| {p.nome} - R${p.preco:0.2f} x {p.quant} - R${p.subtotal:0.2f}")
                    
                    self.total += p.subtotal
                print('\n------------------------------------')    
                print(f"\n| Valor total do carrinho: R${self.total:0.2f}")
                
                # Restrições da entrada
                finalizar = input('\n\nDeseja finalizar o seu pedido? (s/n):\t')
                finalizar_limpo = limpar_texto(finalizar)
                if finalizar_limpo == 's':
                        limpar_tela()
                        print('\n| Pedido enviado!')
                        time.sleep(3)
                        self.finalizar_carrinho(cliente)
                        return True
                elif finalizar_limpo == 'n':
                        limpar_tela()
                        print("\n| Você pode revisar seu pedido!")
                        time.sleep(3)
                        return False
                else:
                    print('\n(Entrada Inválida!)')
                    time.sleep(2)
                    
    def finalizar_carrinho(self, cliente:Cliente) -> None:
        
        pedido_aux = Pedido()
        pedido_aux.cria_pedido(self.lista_carrinho, cliente)

#Main de teste:
'''if __name__ == "__main__":
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
            carrinho.exibe_carrinho()'''