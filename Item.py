####################### BANCO DE DADOS ######################

from Conex_SQL import connection

cursor = connection.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################

import time
from Utilitarios import limpar_tela, limpar_texto
#from Estabelecimento import Estabelecimento

class Item:
    
    #Construtor       
    def __init__(self) -> None:
        
        self.nome = None
        self.descricao = None
        self.preco = None
        
    #Método que cria um item.
    def cria_item(self, estabelecimento) -> bool: #PROBLEMA DE COLOCAR O TIPO DA VARIÁVEL ESTABELECIMENTO
        
        while True:
            limpar_tela()
            print(f"-----------------  Cadastra Item - {estabelecimento.nome}  -----------------\n")
            
            consulta = "SELECT nome FROM Itens WHERE loja_id = ?"   #Consulta SQL
            cursor.execute(consulta, (estabelecimento.id,))   #Executa a consulta
            resultados = cursor.fetchall()   #Recupera os resultados
            nomes_dos_itens = [resultado[0] for resultado in resultados]   #Armazena os nomes na lista
            
            self.nome = input("\nNome do novo produto:\t")     
            novo_nome_limpo = limpar_texto(self.nome)
            nomes_dos_itens_limpo = [limpar_texto(nome) for nome in nomes_dos_itens]
            
            # Restrição de nome do produto já existente
            if novo_nome_limpo in nomes_dos_itens_limpo:
                print('\n| Nome já existente. Por favor, digite outro nome.')
                time.sleep(3)
                continue
            
            self.descricao = input("\nDescrição do novo produto:\t") 
            
            # Restrições de entrada
            try:
                preco_str = input("\nPreço do novo produto:\tR$")
                # Substitui ',' por '.' para permitir ambas as entradas
                preco_str = preco_str.replace(',', '.')
                self.preco = float(preco_str)

                # Restrições de entrada
                certeza = input("\n| Deseja cadastrar o produto com essas informações? (s/n):\t")
                certeza_limpo = limpar_texto(certeza)
                
                if (certeza_limpo != 's' and certeza_limpo != 'n'):
                    print("\n(Entrada Inválida!)")
                    time.sleep(2)
                    continue
                elif certeza_limpo == 'n':
                    return False
                elif certeza_limpo == 's':
                    self.loja_id = estabelecimento.id
                    return True
            except ValueError:
                print("\n(Valor Inválido!)")
                time.sleep(2)
                continue