
class Item:
       
    def __init__(self):
        
        self.nome = None
        self.descricao = None
        self.preco = None
        
    def cria_item(self) -> None:
        self.nome = input("\nPor favor informe o nome do item: ")
        self.descricao = input("Por favor informe a descrição do item: ")
        while True:
            try:
                self.preco = float(input("Digite o valor do produto: "))
                break
            except ValueError:
                print("O valor do produto é inválido. Por favor digite novamente.")
    
    