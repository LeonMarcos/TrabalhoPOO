####################### BANCO DE DADOS ######################

from Conex_SQL import connection

cursor = connection.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################

import time
import datetime
from typing import List, Any
from Cliente import Cliente
from Estabelecimento import Estabelecimento
from Utilitarios import limpar_tela
from Usuario import Usuario

class Pedido:
        
        def __init__(self) -> None: #Construtor
        
            data_hora_atual = datetime.datetime.now() #Obtém a data e a hora atuais
            data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y às %H:%M:%S") #Formata a data e a hora no formato desejado
            
            self.data_horario_pedido = str(data_hora_formatada) #Data e horário que o pedido foi realizado
            self.total = None

        def cria_pedido(self, lista:List[Any], cliente:Cliente) -> None:
            
            self.lista = lista
            self.status = 'Pendente'
            cursor.execute("SELECT MAX(id) FROM Pedidos")
            ultimo_id = cursor.fetchone()[0]
            self.id = ultimo_id + 1
            
            for p in self.lista:
                comando = """ INSERT INTO Pedidos(id, loja_id, cliente_id, id_item, quant_item, preco, subtotal, endereco, data_horario_pedido, status_pedido, nome_cliente, nome_loja, nome_item)
                VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                cursor.execute(comando, self.id, p.estab_id, p.cliente_id, p.item_id, p.quant, p.preco, p.subtotal, p.endereco, self.data_horario_pedido, self.status, p.cliente_nome, p.estab_nome, p.nome)
                cursor.commit()

            self.historico_pedidos_cliente(cliente)
        
        def exibe_pedido(self, id_pedido:int, usuario:Usuario) -> None:
            
            while True:
                consulta = """ SELECT * FROM Pedidos
                                WHERE id = ? """ #consulta o banco de dados
                cursor.execute(consulta, id_pedido)
                tabela = cursor.fetchall()
                self.lista_pedido = []
                for busca in tabela:
                    self.lista_pedido.append(busca)
                
                for p in self.historico:
                    if id_pedido == p.id:
                        pedido=p

                limpar_tela()
                print("\n\n","-"*30, "Detalhes do Pedido","-"*30,"\n")
                
                if usuario.tipo == 'Estabelecimento':
                    print(f"| {pedido.nome_cliente}")
                if usuario.tipo == 'Cliente':
                    print(f"| {pedido.nome_loja}")
                    
                print(f"| #{pedido.id}".ljust(15), f"| Pedido {pedido.status_pedido}".ljust(20),f"| Data/Horário: {pedido.data_horario_pedido}\n")
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
                    
                    a=1
                    while a:
                        quer_avaliar = input('\nDeseja avaliar o seu pedido? (s/n):\t')
                        if (quer_avaliar != 's' and quer_avaliar != 'n'):
                            print("\n(Entrada Inválida!)")
                            continue                   
                    
                        elif quer_avaliar == 's':
                            b=1
                            while b:
                                try:
                                    self.avaliacao = int(input('\nAvalie o seu pedido com uma nota de 1 a 5:\t'))
                                except ValueError:
                                    print("\n(Entrada Inválida!)")
                                    continue
                                
                                if (self.avaliacao < 1 or self.avaliacao > 5):
                                    print("\n(Entrada Inválida!)")
                                    continue                                    
                                
                                print(f"\nVocê avaliou este pedido com nota {self.avaliacao}. Seu feedback é muito importante pra gente!")
                                comando = """ UPDATE Pedidos
                                                        SET avaliacao = ?
                                                        WHERE id = ?"""
                                cursor.execute(comando,self.avaliacao,pedido.id)
                                cursor.commit()
                                time.sleep(3)
                                a=0
                                return True
                        elif quer_avaliar == 'n':
                            print('\n| Seu feedback é importante, considere avaliar o seu pedido mais tarde!')
                            time.sleep(3)
                            a=0
                            return True
                if self.avaliacao:
                        print(f"\n| Avaliação: {self.avaliacao}")
                
                if usuario.tipo == 'Estabelecimento' and pedido.status_pedido == 'Pendente':
                        print("\n1 - Confirmar Pedido.")
                        print("2 - Cancelar Pedido.")
                        print("0 - Voltar.")
                        
                        c=1
                        while c:
                            confirma = input("\nDigite a opção desejada:\t")
                            if (confirma != '0' and confirma != '1' and confirma != '2'):
                                print("\n(Entrada Inválida!)")
                                continue
                            
                            elif confirma == '1':
                                d=1
                                while d:
                                    certeza = input("\nTem certeza que deseja confirmar o pedido? (s/n):\t")
                                    if (certeza != 's' and certeza != 'n'):
                                        print("\n(Entrada Inválida!)")
                                        continue
                                    elif certeza == 's':
                                        self.status = 'Concluído'
                                        comando = """ UPDATE Pedidos
                                                        SET status_pedido = ?
                                                        WHERE id = ?;"""
                                        cursor.execute(comando,self.status,pedido.id)
                                        cursor.commit()
                                        d=0
                                        c=0
                                        limpar_tela()
                                        print('\n| Pedido confirmado!')
                                        time.sleep(2.5)
                                        return True
                                    elif certeza == 'n':
                                        d=0
                        
                            elif confirma == '2':
                                e=1
                                while e:
                                    certeza = input("\nTem certeza que deseja cancelar o pedido? (s/n):\t")
                                    if (certeza != 's' and certeza != 'n'):
                                        print("\n(Entrada Inválida!)")
                                        continue
                                    elif certeza == 's':
                                        self.status = 'Cancelado'                          
                                        comando = """ UPDATE Pedidos
                                                        SET status_pedido = ?
                                                        WHERE id = ?;"""
                                        cursor.execute(comando,self.status,pedido.id)
                                        cursor.commit()
                                        c=0
                                        e=0
                                        limpar_tela()
                                        print('\n| Pedido cancelado!')
                                        time.sleep(2.5)
                                        return True
                                    elif certeza == 'n':
                                        e=0
                            
                            elif confirma == '0':
                                c=0
                                return False
                            
                            pass
                else:
                    input('\n\nPressione ENTER para voltar.\t')
                    return False

        def historico_pedidos_cliente(self, cliente:Cliente) -> None:
            
            while True:
                consulta = """ SELECT DISTINCT id, status_pedido, nome_loja, data_horario_pedido
                                FROM Pedidos
                                WHERE cliente_id = ?; """ #consulta o banco de dados
                cursor.execute(consulta, cliente.id) 
                tabela = cursor.fetchall()
                self.historico = []
                for busca in tabela:
                    self.historico.append(busca)
                
                limpar_tela()
                print("-"*30, f"Pedidos - {cliente.nome}", "-"*30)

                if not self.historico:
                    print('\n| Você ainda não realizou nenhum pedido!')
                    print('\n',"-"*50)
                    input('\n\nPressione ENTER para voltar.\t')
                    return False

                for p in self.historico:
                    data_formatada = p.data_horario_pedido[:10]
                    print(f"\nData: {data_formatada} ")
                    print(f"{p.id} | Pedido {p.status_pedido} – {p.nome_loja}")
                    print('\n',"-"*50)
                print("\n0 - Voltar.")
                
                a = 1    
                while a:
                    try:
                        nav = int(input("\nDigite o número do pedido que deseja visualizar ou '0' para voltar: \t"))
                    except ValueError:
                        print("\n(Entrada Inválida!)")
                        continue
                        
                    if nav == 0:
                        a=0
                        return False
                    
                    else:
                        for p in self.historico:
                            if nav == p.id:
                                self.exibe_pedido(nav,cliente)
                                a=0
                    print("\n(Entrada Inválida!)")
                
        def historico_pedidos_estabelecimento(self, estabelecimento:Estabelecimento, status:str) -> None:
            
            while True:
                if status == 'Pendente':
                    consulta = """ SELECT DISTINCT id, status_pedido, nome_cliente, data_horario_pedido
                                    FROM Pedidos
                                    WHERE loja_id = ? AND status_pedido = 'Pendente'; """ #consulta o banco de dados

                if status == 'Finalizado':
                    consulta = """ SELECT DISTINCT id, status_pedido, nome_cliente, data_horario_pedido
                                    FROM Pedidos
                                    WHERE loja_id = ? AND status_pedido != 'Pendente'; """ #consulta o banco de dados
                    
                cursor.execute(consulta, estabelecimento.id) 
                tabela = cursor.fetchall()
                self.historico = []
                for busca in tabela:
                    self.historico.append(busca)
                
                limpar_tela()
                print("-"*30, f"Pedidos - {estabelecimento.nome}", "-"*30)

                if not self.historico:
                    print(f'\n| No momento não existem pedidos {status}s!')
                    print('\n',"-"*50)
                    input('\n\nPressione ENTER para voltar.\t')
                    return False

                for p in self.historico:
                    data_formatada = p.data_horario_pedido[:10]
                    print(f"\nData: {data_formatada} ")
                    print(f"{p.id} | Pedido {p.status_pedido} – {p.nome_cliente}")
                    print('\n',"-"*50)
                print("\n0 - Voltar.")
                
                a = 1    
                while a:
                    try:
                        nav = int(input("\nDigite o número do pedido que deseja visualizar ou '0' para voltar: \t"))
                    except ValueError:
                        print("\n(Entrada Inválida!)")
                        continue
                        
                    if nav == 0:
                        a=0
                        return False
                    
                    else:
                        for p in self.historico:
                            if nav == p.id:
                                self.exibe_pedido(nav,estabelecimento)
                                a=0
                    print("\n(Entrada Inválida!)")

#Main de teste:
'''if __name__ == "__main__":
    nome = 'leon'
    pedido = Pedido(nome)
    
    print(pedido.numero)'''