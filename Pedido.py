####################### BANCO DE DADOS ######################

import time
from Conex_SQL import connection


cursor = connection.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################

import random
import datetime

class Pedido:
        #Atributos e construtor
        def __init__(self:str) -> None: #Cria um pedido com base no nome do cliente         
            #self.nome = nome
            self.data_pedido = datetime.date.today()#Data em que o pedido foi realizado
            #self.numero =''.join([str(random.randint(0, 9)) for _ in range(4)]) #Cria um número aleatório de 4 digitos para ser o número do pedido
            self.total = None
            


        def cria_pedido(self, lista, estabelecimento, cliente):
            #car_aux = Carrinho()
            estabelecimento = estabelecimento
            cliente = cliente
            self.lista = lista
            #self.status = 'Pendente'
            cursor.execute("SELECT MAX(id) FROM Pedidos")
            ultimo_id = cursor.fetchone()[0]
            self.id = ultimo_id + 1
            
            for p in self.lista:
                comando = """ INSERT INTO Pedidos(id, loja_id, cliente_id, id_item, quant_item, preco, subtotal, endereco, data_pedido, status_pedido, nome_cliente, nome_loja, nome_item)
                VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                cursor.execute(comando, self.id, estabelecimento.id, cliente.id, p.item_id, p.quant, p.preco, p.subtotal, cliente.endereco, 'hoje', 'Pendente', cliente.nome, estabelecimento.nome, p.nome)
                cursor.commit()

            self.historico_pedidos_cliente(cliente)
        
        def exibe_pedido(self,pedido,usuario):
            while True:
                usuario = usuario
                pedido = pedido
                consulta = """ SELECT * FROM Pedidos
                                WHERE id = ? """ #consulta o banco de dados
                cursor.execute(consulta, pedido.id) 
                tabela = cursor.fetchall()
                self.lista_pedido = []
                for busca in tabela:
                    self.lista_pedido.append(busca)

                print('\033[H\033[2J')
                print(f"\n\n","-"*30, "Detalhes do Pedido","-"*30,"\n")
                if usuario.tipo == 'Estabelecimento':
                    print(f"| {pedido.nome_cliente}")
                if usuario.tipo == 'Cliente':
                    print(f"| {pedido.nome_loja}")
                print(f"| #{pedido.id}".ljust(15), f"| Pedido {pedido.status_pedido}".ljust(20),f"| {pedido.data_pedido}\n")
                print("-"*60,"\n")
                
                self.total = 0
                for p in self.lista_pedido:
                    self.avaliacao = p.avaliacao
                    self.endereco = p.endereco
                    #p.subtotal = p.quant_item * p.preco
                    print(f"| {p.nome_item}".ljust(20), f"R${p.preco:0.2f}".ljust(15),f"x {p.quant_item}".ljust(10), f"R${p.subtotal:0.2f}")
                    
                    self.total += p.subtotal 
                    
                print("\n","-"*60)    
                print(f"\n| Valor total do pedido: R${self.total:0.2f}")
                print(f"\n| Endereço de entrega: {self.endereco}") #### DESCOBRIR O PQ NÃO FUNCIONA COM pedido.endereco
                if usuario.tipo == 'Cliente' and self.avaliacao == None and pedido.status_pedido == 'Concluído':
                    
                    quer_avaliar = input('\nDeseja avaliar o seu pedido?\t(s/n)\n')
                    if quer_avaliar == 's':
                        self.avaliacao = input('Avalie o seu pedido com uma nota de 1 a 5:\n')
                        print(f"Você avaliou este pedido com nota {self.avaliacao}. Seu feedback é muito importante pra gente!")
                        comando = """ UPDATE Pedidos
                                                SET avaliacao = ?
                                                WHERE id = ?"""
                        cursor.execute(comando,self.avaliacao,pedido.id)
                        time.sleep(3)
                        return True
                    if quer_avaliar == 'n':
                        print('| Seu feedback é importante, considere avaliar o seu pedido mais tarde!')
                        time.sleep(3)
                if self.avaliacao:
                        print(f"\n| Avaliação: {self.avaliacao}")
                
                

                if usuario.tipo == 'Estabelecimento' and pedido.status_pedido == 'Pendente':
                        print("\n1 - Confirmar Pedido")
                        print("2 - Cancelar Pedido")
                        print("0 - Voltar")
                        
                        confirma = input(f"\nDigite a opção desejada:\t")
                        if confirma == '1':
                            certeza = input("Tem certeza que deseja confirmar o pedido? \t(s/n)\n")
                            if certeza == 's':
                                comando = """ UPDATE Pedidos
                                                SET status_pedido = 'Concluído'
                                                WHERE id = ?;"""
                                cursor.execute(comando,pedido.id)
                                cursor.commit()
                                return True
                        
                        cursor.execute(comando)
                        if confirma == '2':
                            certeza = input("Tem certeza que deseja cancelar o pedido? \t(s/n)\n")
                            if certeza == 's':
                                comando = """ UPDATE Pedidos
                                                SET status_pedido = 'Concluído'
                                                WHERE id = ?;"""
                                cursor.execute(comando,pedido.id)
                                cursor.commit()
                                return True
                        
                        if confirma == '0':
                            return False
                        
                        pass
                else:
                    input('\n\nPrecione qualquer tecla para voltar\n')
                    return False

        def historico_pedidos_cliente(self,cliente):
            while True:
                cliente = cliente
                consulta = """ SELECT DISTINCT id, status_pedido, nome_loja, data_pedido
                                FROM Pedidos
                                WHERE cliente_id = ?; """ #consulta o banco de dados
                cursor.execute(consulta, cliente.id) 
                tabela = cursor.fetchall()
                self.historico = []
                for busca in tabela:
                    self.historico.append(busca)
                
                print('\033[H\033[2J')
                print("-"*30, f"Pedidos - {cliente.nome}", "-"*30)

                if not self.historico:
                    print(f'\n| Você ainda não realizou nenhum pedido!')
                    print('\n',"-"*50)
                    input('')
                    return False

                for p in self.historico:
                    print(f"\n{p.data_pedido} ")
                    print(f"{p.id} | Pedido {p.status_pedido} – {p.nome_loja}")
                    print('\n',"-"*50)
                print("0 - Voltar")

                
                nav = int(input("\nDigite o número do pedido que deseja visualizar: \t"))
                
                for p in self.historico:
                    if nav == p.id:
                        self.exibe_pedido(p,cliente)
                if nav == 0:
                    return False
                
        def historico_pedidos_estabelecimento(self,estabelecimento,status):
            while True:
                status = status
                estabelecimento = estabelecimento
                if status == 'Pendente':
                    consulta = """ SELECT DISTINCT id, status_pedido, nome_cliente, data_pedido
                                    FROM Pedidos
                                    WHERE loja_id = ? AND status_pedido = 'Pendente'; """ #consulta o banco de dados

                if status == 'Concluído':
                    consulta = """ SELECT DISTINCT id, status_pedido, nome_cliente, data_pedido
                                    FROM Pedidos
                                    WHERE loja_id = ? AND status_pedido = 'Concluído'; """ #consulta o banco de dados
                    
                cursor.execute(consulta, estabelecimento.id) 
                tabela = cursor.fetchall()
                self.historico = []
                for busca in tabela:
                    self.historico.append(busca)
                
                print('\033[H\033[2J')
                print("-"*30, f"Pedidos - {estabelecimento.nome}", "-"*30)

                if not self.historico:
                    print(f'\n| No momento não existem pedidos {status}s!')
                    print('\n',"-"*50)
                    input('')
                    return False
                    

                for p in self.historico:
                    print(f"\n| {p.data_pedido} ")
                    print(f"{p.id} | Pedido {p.status_pedido} – {p.nome_cliente}")
                    print('\n',"-"*50)
                print("\n0 - Voltar")

                nav = int(input("\nDigite o número do pedido que deseja visualizar: \t"))
                
                for p in self.historico:
                    if nav == p.id:
                        self.exibe_pedido(p,estabelecimento)
                if nav == 0:
                    return False

            
if __name__ == "__main__":
    nome = 'leon'
    pedido = Pedido(nome)
    
    print(pedido.numero)