

####################### BANCO DE DADOS ######################

from Conex_SQL import connection


cursor = connection.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################

from Usuario import Usuario
from Item import Item
import time
from Utilitarios import limpar_tela

class Estabelecimento(Usuario):
    # Atributos e construtor da classe Estabelecimento
    def __init__(self):
        super().__init__()
        self.__horario_funcio = [None, None]  # Inicializando com None para indicar horários indefinidos
        self.__cardapio = []
        
    #Método que define o horário de funcionamento do Estabelecimento
    def define_horario(self) -> None:
        # Tratamento de exceção para o horário
        abertura = input("\nDigite o horário de abertura de seu estabelecimento: ")
        fechamento = input("Digite o horário de fechamento de seu estabelecimento: ")
        self.__horario_funcio[0] = abertura
        self.__horario_funcio[1] = fechamento
    
    #Método que retorna o vetor de horário de funcionamento. O primeiro elemento é o horário de abertura e o segundo é o horário de fechamento.
    def get_horario(self) -> list:
        return self.__horario_funcio
    
    #Método que verifica se um item já existeno cardapio. Se o item existir, retorna True.
    def __verifica_item_cardapio(self, nome_item,estabelecimento: str) -> bool:
        estabelecimento = estabelecimento
        nome_item = nome_item
        consulta = """ SELECT * FROM Itens WHERE loja_id = ?; """ #consulta o banco de dados
        cursor.execute(consulta,estabelecimento.id) 
        tabela = cursor.fetchall()
        self.__cardapio = []
        for busca in tabela:
            self.__cardapio.append(busca)
        
        for procura in self.__cardapio:
            if procura.nome == nome_item:
                return True
        
        return False
    
    #Método que cadastra item no cardápio. O método só cadas um item no cadárpio caso ele seja novo.
    def cadastra_item(self,estabelecimento) -> None:
        estabelecimento = estabelecimento
        item = Item()
        item.cria_item(estabelecimento) #Os itens só podem ser criados dentro dessa função.
        nome_item = item.nome
        if not self.__verifica_item_cardapio(nome_item,estabelecimento):
            comando = """ INSERT INTO Itens(nome, descricao, preco, loja_id)
            VALUES
              (?, ?, ?, ?)"""
            cursor.execute(comando, item.nome, item.descricao, item.preco, item.loja_id )
            cursor.commit()
            
            print("\nItem cadastrado com sucesso!")
            time.sleep(2)
        else:
            print("\nEste item já possui cadastrado.")
            time.sleep(2)
    
    #Método que exibe os itens cadastrados no cardápio.
    def exibe_cardapio(self, estabelecimento) -> None:
        estabelecimento = estabelecimento
        while True:
            limpar_tela()
            print('*'*31," "*8,f"Cardápio - {estabelecimento.nome}"," "*8,'*'*31,"\n\n")
            consulta = """ SELECT * FROM Itens WHERE loja_id = ?; """ #consulta o banco de dados
            cursor.execute(consulta,estabelecimento.id) 
            tabela = cursor.fetchall()
            self.__cardapio = []
            for busca in tabela:
                self.__cardapio.append(busca)
            if not self.__cardapio:
                print("| O cardápio está vazio.")
                input('\nPressione ENTER para voltar')
                return False
                
            
            numero = 0
            print("N° |           Nome            |            Descrição            |            Preço  ")
            for item_cardapio in self.__cardapio:
                    # sys.stdout.flush()
                    print("-"*100)
                    numero = numero +1
                    # Lista de caracteres a serem impressos
                    print(numero, f"   {item_cardapio.nome}".ljust(30), f"{item_cardapio.descricao}".ljust(33), f"R${item_cardapio.preco:.2f}")
            print("-"*100)
            break
        
    
    #Método que remove um item desejado do cardápio com base no nome.
    def remove_item_cardapio(self) -> None:
        nome_item = input("\nDigite o nome do item a ser removido: ")
        item_encontrado = None
        for item in self.__cardapio:
            if item.nome == nome_item:
                item_encontrado = item
                break
        if item_encontrado:
            self.__cardapio.remove(item_encontrado)
            print(f"O item '{nome_item}' foi removido com sucesso!")
        else:
            print(f"O item '{nome_item}' não foi encontrado no cardápio.")
    
    #método que retorna um item escolhido do cardápio
    def escolhe_item(self) -> 'Item':
        nome_item = input("\nDigite o nome do item que deseja escolher: ")
        for item in self.__cardapio:
            if item.nome == nome_item:
                return item
        print(f"\nO item '{nome_item}' não foi encontrado no cardápio.")
        return None
    
if __name__ == "__main__":
    estabelecimentoum = Estabelecimento()
    estabelecimentoum.cria_Usuario()
    print("\n")
    print(estabelecimentoum.get_nome())
    print(estabelecimentoum.get_endereco())
    print(estabelecimentoum.get_telefone())
    print(estabelecimentoum.get_email())
    print(estabelecimentoum.get_cpf_cnpj())
    print(estabelecimentoum.get_senha())
    
    estabelecimentoum.define_horario()
    print(estabelecimentoum.get_horario())
    
    estabelecimentoum.exibe_cardapio()
    estabelecimentoum.cadastra_item()
    estabelecimentoum.cadastra_item()
    estabelecimentoum.cadastra_item()
    estabelecimentoum.exibe_cardapio()
    estabelecimentoum.remove_item_cardapio()
    estabelecimentoum.exibe_cardapio()
        
