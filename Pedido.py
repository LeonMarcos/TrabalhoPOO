# import Carrinho

from Carrinho import Carrinho
import random
import datetime

class Pedido:
        #Atributos e construtor
        def __init__(self, nome:str) -> None: #Cria um pedido com base no nome do cliente         
            self.nome = nome
            self.data_pedido = datetime.date.today()#Data em que o pedido foi realizado
            self.numero =''.join([str(random.randint(0, 9)) for _ in range(10)]) #Cria um número aleatório de 10 digitos para ser o número do pedido
            self.total = None
            
            
        def abre_pedido(self):
            carrinho = Carrinho(self.nome)#cria um objeto da classe carrinho
            
            
if __name__ == "__main__":
    nome = 'leon'
    pedido = Pedido(nome)
    
    print(pedido.numero)