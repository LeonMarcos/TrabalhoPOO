####################### BANCO DE DADOS ######################

from Conex_SQL import connection

cursor = connection.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################

import re
import time
from Utilitarios import limpar_tela, limpar_texto
from Usuario import Usuario
from Item import Item

class Estabelecimento(Usuario):
    # Constantes
    # Regex para garantir que o telefone tenha exatamente 11 dígitos
    padrao_telefone = r"^\d{11}$"
    # Regex para garantir que o nome só contenha letras e espaços
    padrao_nome = r"^[a-zA-ZÀ-ÿ ]+$"
    # Regex para garantir que o cnpj tenha exatamente 14 dígitos
    padrao_cnpj = r"^\d{14}$"

    # Atributos e construtor da classe Estabelecimento
    def __init__(self):
        super().__init__()
        self._nome = None
        self._endereco = None
        self._telefone = None
        self._email = None
        self._cpf_cnpj = None
        self._senha = None
        self.tipo = self.__class__.__name__
        self.__cardapio = []

    def get_nome(self) -> str:
        return self._nome

    def get_endereco(self) -> str:
        return self._endereco

    def get_telefone(self) -> int:
        return self._telefone

    def get_email(self) -> str:
        return self._email

    def get_cpf_cnpj(self) -> int:
        return self._cpf_cnpj

    def get_senha(self) -> str:
        return self._senha

    def cria_Usuario(self) -> None:
        limpar_tela()
        print(f"\n---------  Cadastrar {self.__class__.__name__}  ---------\n")

        # Tratamento de exceção para o nome
        while True:
            try:
                nome = str(input("\nNome: "))
                if len(nome.split()) >= 1 and re.fullmatch(self.padrao_nome, nome):
                    self._nome = nome
                    break
                else:
                    print(
                        "Nome de estabelecimento inválido. Por favor, digite um nome contendo apenas letras e espaços.")
            except:
                print("Nome inválido. Por favor, digite novamente.")

        # Tratamento de exceção para o endereço
        while True:
            try:
                self._endereco = str(input("Endereço: "))
                break
            except:
                print("Endereço inválido. Por favor, digite novamente.")

        # Tratamento de exceção para o telefone
        while True:
            try:
                telefone = input("Telefone (11 dígitos com DDD): ")
                if re.fullmatch(self.padrao_telefone, telefone):
                    self._telefone = int(telefone)
                    break
                else:
                    print(
                        "Número de telefone inválido. Por favor, digite um número com 11 dígitos (DDD + número).")
            except:
                print("Número de telefone inválido. Por favor, digite novamente.")

        # Tratamento de exceção para o email
        while True:
            try:
                self._email = str(input("E-mail: "))
                if "@" in self._email:
                    break
                else:
                    print("E-mail inválido. O e-mail deve conter '@'.")
            except:
                print("E-mail inválido. Por favor, digite novamente.")

        # Tratamento de exceção para o cnpj
        while True:
            try:
                if self.tipo == 'Estabelecimento':
                    cnpj = re.sub(r'\D', '', input(
                        "CNPJ (10 dígitos somente números. O 0001 será adicionado automaticamente.): "))
                    if len(cnpj) == 10 and cnpj.isdigit():
                        # Insere '0001' entre o 8º e o 9º dígito
                        cnpj = cnpj[:8] + '0001' + cnpj[8:]
                        self._cpf_cnpj = int(cnpj)
                        break
                    else:
                        print("Número de CNPJ inválido. Por favor, digite novamente.")
            except:
                print("Número de CNPJ inválido. Por favor, digite novamente.")

        # Tratamento de exceção para a senha
        while True:
            try:
                senha = input("Digite sua senha: ")
                if len(senha) >= 6:
                    self._senha = senha
                    break
                else:
                    print(
                        "A senha deve ter pelo menos 6 dígitos. Por favor, digite novamente.")
            except:
                print("Senha inválida. Por favor, digite novamente.")

        # self.tipo = self.__class__.__name__
        limpar_tela()

    # Método para atualizar usuário
    def atualiza_Usuario(self) -> None:
        limpar_tela()
        print(f"\n---------  Atualizar {self.__class__.__name__}  ---------\n")
        atributos = {
            "1": "Nome",
            "2": "Endereço",
            "3": "Telefone",
            "4": "E-mail",
            "5": "CNPJ",
            "6": "Senha"
        }
        while True:
            print("\nEscolha o atributo a ser atualizado:")
            for key, value in atributos.items():
                print(f"{key}. {value}")
            escolha = input("\nDigite o número do atributo (ou '0' para sair):\t")
            if escolha == '0':
                break
            elif escolha in atributos:
                atributo = atributos[escolha]
                if atributo == "Nome":
                    while True:
                        try:
                            nome = str(input("\nNovo Nome: "))
                            if len(nome.split()) >= 1 and re.fullmatch(self.padrao_nome, nome):
                                self._nome = nome
                                break
                            else:
                                print(
                                    "Nome de estabelecimento inválido. Por favor, digite um nome contendo apenas letras e espaços.")
                        except:
                            print("Nome inválido. Por favor, digite novamente.")
                elif atributo == "Endereço":
                    while True:
                        try:
                            self._endereco = str(input("Novo Endereço: "))
                            break
                        except:
                            print("Endereço inválido. Por favor, digite novamente.")
                elif atributo == "Telefone":
                    while True:
                        try:
                            telefone = input(
                                "Novo Telefone (11 dígitos com DDD): ")
                            if re.fullmatch(self.padrao_telefone, telefone):
                                self._telefone = int(telefone)
                                break
                            else:
                                print(
                                    "Número de telefone inválido. Por favor, digite um número com 11 dígitos (DDD + número).")
                        except:
                            print(
                                "Número de telefone inválido. Por favor, digite novamente.")
                elif atributo == "E-mail":
                    while True:
                        try:
                            self._email = str(input("Novo E-mail: "))
                            if "@" in self._email:
                                break
                            else:
                                print("E-mail inválido. O e-mail deve conter '@'.")
                        except:
                            print("E-mail inválido. Por favor, digite novamente.")
                elif atributo == "CNPJ":
                    while True:
                        try:
                            cnpj = re.sub(r'\D', '', input(
                                "Novo CNPJ (10 dígitos somente números. O 0001 será adicionado automaticamente.): "))
                            if len(cnpj) == 10 and cnpj.isdigit():
                                cnpj = cnpj[:8] + '0001' + cnpj[8:]
                                self._cpf_cnpj = int(cnpj)
                                break
                            else:
                                print(
                                    "Número de CNPJ inválido. Por favor, digite novamente.")
                        except:
                            print(
                                "Número de CNPJ inválido. Por favor, digite novamente.")
                elif atributo == "Senha":
                    while True:
                        try:
                            senha = input("Nova Senha: ")
                            if len(senha) >= 6:
                                self._senha = senha
                                break
                            else:
                                print(
                                    "A senha deve ter pelo menos 6 dígitos. Por favor, digite novamente.")
                        except:
                            print("Senha inválida. Por favor, digite novamente.")
            else:
                print("Escolha inválida. Por favor, tente novamente.")

    

    # Método que exibe os itens cadastrados no cardápio.
    def exibe_cardapio(self, estabelecimento) -> None:
        estabelecimento = estabelecimento
        while True:
            limpar_tela()
            print('*'*31, " "*8,
                  f"Cardápio - {estabelecimento.nome}", " "*8, '*'*31, "\n\n")
            consulta = """ SELECT * FROM Itens WHERE loja_id = ?; """  # consulta o banco de dados
            cursor.execute(consulta, estabelecimento.id)
            tabela = cursor.fetchall()
            self.__cardapio = []
            for busca in tabela:
                self.__cardapio.append(busca)
            if not self.__cardapio:
                print("| O cardápio está vazio.")
                input('\nPressione ENTER para voltar')
                return False

            numero = 0
            print(
                "N° |           Nome            |            Descrição            |            Preço  ")
            for item_cardapio in self.__cardapio:
                # sys.stdout.flush()
                print("-"*100)
                numero = numero + 1
                # Lista de caracteres a serem impressos
                print(numero, f"   {item_cardapio.nome}".ljust(30), f"{item_cardapio.descricao}".ljust(33), f"R${item_cardapio.preco:.2f}")
            print("-"*100)
            break
        
    # Método que cadastra item no cardápio.
    def cadastra_item(self, estabelecimento) -> None:
        
        item = Item()
        # Os itens só podem ser criados dentro dessa função.
        retorno = item.cria_item(estabelecimento)
        if retorno == False:
            return
        comando = """ INSERT INTO Itens(nome, descricao, preco, loja_id)
        VALUES
          (?, ?, ?, ?)"""
        cursor.execute(comando, item.nome, item.descricao,
                       item.preco, item.loja_id)
        cursor.commit()

        print("\n| Produto cadastrado com sucesso!")
        time.sleep(2.5) 

    # Método que remove um item desejado do cardápio com base no nome.
    def remove_item_cardapio(self) -> None:
            
        nome_item = input("\nDigite o nome do item a ser removido:\t")
        nome_limpo = limpar_texto(nome_item)
        
        # Buscar item no cardápio
        item_encontrado = None
        for item in self.__cardapio:
            if limpar_texto(item.nome) == nome_limpo:
                item_encontrado = item
                break
            
        if item_encontrado:
            # Restrições de entrada
            certeza = input(f"\nTem certeza que deseja remover '{item_encontrado.nome}' do cardápio? (s/n):\t")
            certeza_limpo = limpar_texto(certeza)
            if (certeza_limpo != 's' and certeza_limpo != 'n'):
                print("\n(Entrada Inválida!)")
                time.sleep(2)
                return
            elif certeza_limpo == 's':
                # Consulta SQL para deletar o item com o nome e loja especificados
                consulta = "DELETE FROM Itens WHERE nome = ? AND loja_id = ?"
                # Executa a consulta
                cursor.execute(consulta, (item_encontrado.nome, item_encontrado.loja_id))
                # Deleta o item no banco de dados
                cursor.commit()

                print(f"\n| '{item_encontrado.nome}' foi removido com sucesso!")
                time.sleep(3)
                return
            elif certeza_limpo == 'n':
                return  
        else:
            print('\n(Nome Inválido!)')
            time.sleep(2)
            return
            
    def altera_item_cardapio(self) -> None:
        
        nome_item = input("\nDigite o nome do item a ser alterado:\t")
        nome_limpo = limpar_texto(nome_item)
        
        item_encontrado = None
        for item in self.__cardapio:
            if limpar_texto(item.nome) == nome_limpo:
                item_encontrado = item
                break
            
        if item_encontrado:
            a=1
            while a:
                limpar_tela()
                print('\n\n------------- Altera Item -------------')
                print('\n\n1 - Nome: {item_encontrado.nome}')
                print('2 - Descrição: {item_encontrado.descricao}')
                print('3 - Preço: {item_encontrado.preco}')
                
                escolha = input('\nQual atributo deseja modificar? (1, 2 ou 3):\t')
                escolha_limpo = limpar_texto(escolha)
                
                if (escolha_limpo != '1' or escolha_limpo != '2' or escolha_limpo != '3'):
                    print("\n(Entrada Inválida!)")
                    time.sleep(2)
                    continue
                
                if escolha_limpo == '1':
                    
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
                
                elif escolha_limpo == '2':
                    nova_descricao = input("\nDescrição do novo produto:\t")
                
                elif escolha_limpo == '3':
                    try:
                        preco_str = input("\nPreço do novo produto:\tR$")
                        # Substitui ',' por '.' para permitir ambas as entradas
                        preco_str = preco_str.replace(',', '.')
                        preco = float(preco_str)
                    except ValueError:
                        print("\n(Valor Inválido!)")
                        time.sleep(2)
                        continue
                    
                
                else:
                    print("\n(Entrada Inválida!)")
                    time.sleep(2)
                    continue
                    
                
                
                      
                
                
                
            # Restrições de entrada
            certeza = input(f"\nTem certeza que deseja remover '{item_encontrado.nome}' do cardápio? (s/n):\t")
            certeza_limpo = limpar_texto(certeza)
            if (certeza_limpo != 's' and certeza_limpo != 'n'):
                print("\n(Entrada Inválida!)")
                time.sleep(2)
                return
            elif certeza_limpo == 's':
                # Consulta SQL para deletar o item com o nome e loja especificados
                consulta = "DELETE FROM Itens WHERE nome = ? AND loja_id = ?"
                # Executa a consulta
                cursor.execute(consulta, (item_encontrado.nome, item_encontrado.loja_id))
                # Deleta o item no banco de dados
                cursor.commit()

                print(f"\n| '{item_encontrado.nome}' foi removido com sucesso!")
                time.sleep(3)
                return
            elif certeza_limpo == 'n':
                return  
        else:
            print('\n(Nome Inválido!)')
            time.sleep(2)
            return

#Main de teste:
'''if __name__ == "__main__":
    estabelecimentoum = Estabelecimento()
    estabelecimentoum.cria_Usuario()
    print("\n")
    print(estabelecimentoum.get_nome())
    print(estabelecimentoum.get_endereco())
    print(estabelecimentoum.get_telefone())
    print(estabelecimentoum.get_email())
    print(estabelecimentoum.get_cpf_cnpj())
    print(estabelecimentoum.get_senha())

    estabelecimentoum.exibe_cardapio(estabelecimentoum)
    estabelecimentoum.cadastra_item(estabelecimentoum)
    estabelecimentoum.cadastra_item(estabelecimentoum)
    estabelecimentoum.cadastra_item(estabelecimentoum)
    estabelecimentoum.exibe_cardapio(estabelecimentoum)
    estabelecimentoum.remove_item_cardapio()
    estabelecimentoum.exibe_cardapio(estabelecimentoum)'''