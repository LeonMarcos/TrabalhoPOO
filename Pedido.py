# import Carrinho

class Pedido:
        
    
        def __init__(self):
            
            # self.num = cliente.n_pedido
            #print(cliente.n_pedido) printar para testar se o n° bate com o n° do carrinho
            pass
        
        def exibe(self, Carrinho):
            
            self.lista = Carrinho.lista
            Carrinho.limpar()
            
            
            print('\n---------------- PEDIDO ----------------\n')
            total = 0
            for p in self.lista:
                
                subtotal = p.quant * p.preco
                print(f"| {p.nome} - R${p.preco:0.2f} x {p.quant} - R${subtotal:0.2f}")
                
                total += subtotal
            print('\n------------------------------------')    
            print(f"\nValor total do pedido: R${total:0.2f}")
            
  
        def avaliar(self):
         
          opcao = input('\nDeseja avaliar o pedido?\t (s/n)\t')
          if opcao == 's':
              nota = input('\nAvalie seu pedido com uma nota entre 0 e 10:\n')
              print(f'\nObrigado por contribuir com sua avaliação de nota {nota}!')
              self.nota = nota
          else:
              print('\nObrigado pela compra!')