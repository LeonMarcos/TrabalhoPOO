

class Item:
       
    def __init__(self):
        # Atributos e construtor da classe Item
        self.nome = None
        self.descricao = None
        self.preco = None
        
    #Método que cria um item.
    def cria_item(self,estabelecimento) -> None:
        estabelecimento = estabelecimento
        print('\033[H\033[2J')
        print(f"-----------------  Cadastra Item -{estabelecimento.nome}  -----------------\n")
        self.nome = input("\nNome do novo item: ")
        self.descricao = input("Descrição do novo item: ")
        while True:
            try:
                self.preco = float(input("Valor do produto: R$"))
                break
            except ValueError:
                print("O valor do produto é inválido. Por favor digite novamente.")
        self.loja_id = estabelecimento.id

    