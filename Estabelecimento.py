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
        
        consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados
        cursor.execute(consulta) 
        tabela = cursor.fetchall()
        lista_usuarios  = []
        for busca in tabela:
            lista_usuarios.append(busca)
            
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
        
        cursor.execute("SELECT MAX(id) FROM Usuarios")
        ultimo_id = cursor.fetchone()[0]
        self.id = ultimo_id + 1

        limpar_tela()

    # Método para atualizar usuário
    def atualiza_Usuario(self, numero:int) -> None:
        
        consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados
        cursor.execute(consulta) 
        tabela = cursor.fetchall()
        lista_usuarios  = []
        for busca in tabela:
            lista_usuarios.append(busca)
        
        consulta = """ SELECT * FROM Usuarios WHERE tipo = ?; """ #consulta o banco de dados
        cursor.execute(consulta, self.__class__.__name__) 
        tabela = cursor.fetchall()
        lista_estabelecimentos  = []
        for busca in tabela:
            lista_estabelecimentos.append(busca)        
        
        atributos = {
            "1": "Nome",
            "2": "Endereço",
            "3": "Telefone",
            "4": "E-mail",
            "5": "CNPJ",
            "6": "Senha"
        }
        
        while True:
            limpar_tela()
            print(f"\n--------------  Atualizar {self.__class__.__name__}  --------------\n")
            print("\nEscolha o atributo a ser atualizado:\n")
            for key, value in atributos.items():
                print(f"{key}. {value}")
            print("\n0 - Voltar.")
            
            escolha = input("\nDigite o número do atributo (ou '0' para voltar):\t")
            escolha_limpo = limpar_texto(escolha)
            
            if escolha_limpo == '0':
                break
            elif escolha_limpo in atributos:
                atributo = atributos[escolha_limpo]
                n_alterado = False
                
                if atributo == "Nome":
                    nome_escolha = 'Nome'
                    titulo = 'nome'
                    
                    nome = str(input("\n- Novo Nome:\t"))
                    if len(nome.split()) >= 1 and re.fullmatch(self.padrao_nome, nome):
                        self._nome = nome
                        update = self._nome
                        
                        for estabelecimento_banco in lista_estabelecimentos:
                            
                            if limpar_texto(estabelecimento_banco.nome) == limpar_texto(self._nome):
                                print('\n| Nome já cadastrado.')
                                time.sleep(3)
                                n_alterado = True
                                continue
                    else:
                        print("\nNome inválido. Por favor, digite um nome contendo apenas letras e espaços.")
                        time.sleep(4)
                        continue
                        
                elif atributo == "Endereço":
                    nome_escolha = "Endereço"
                    titulo = 'endereco'
                    
                    self._endereco = str(input("\n- Novo Endereço:\t"))
                    update = self._endereco
                    
                    for estabelecimento_banco in lista_estabelecimentos:
                        
                        if limpar_texto(estabelecimento_banco.endereco) == limpar_texto(self._endereco): #alterei para email ou cpf/cnpj iguais
                            print('\n| Endereço já cadastrado.')
                            time.sleep(3)
                            n_alterado = True
                            continue
                            
                elif atributo == "Telefone":
                    nome_escolha = 'Telefone'
                    titulo = 'telefone'
                    
                    telefone = input("\n- Novo Telefone (11 dígitos com DDD):\t")
                    if re.fullmatch(self.padrao_telefone, telefone):
                        self._telefone = int(telefone)
                        update = self._telefone
                        
                        for estabelecimento_banco in lista_usuarios:
                            if estabelecimento_banco.telefone == self._telefone: #alterei para email ou cpf/cnpj iguais
                                print('\n| Telefone já cadastrado.')
                                time.sleep(3)
                                n_alterado = True
                                continue
                            
                    else:
                        print("\nNúmero de telefone inválido. Por favor, digite um número com 11 dígitos (DDD + número).")
                        time.sleep(4)
                        continue
                            
                elif atributo == "E-mail":
                    nome_escolha = 'E-mail'
                    titulo = 'email'
                    
                    self._email = str(input("\n- Novo E-mail:\t"))
                    if "@" in self._email:
                        update = self._email
                        
                        for estabelecimento_banco in lista_usuarios:
                            
                            if limpar_texto(estabelecimento_banco.email) == limpar_texto(self._email):
                                 print('\n| E-mail já cadastrado.')
                                 time.sleep(3)
                                 n_alterado = True
                                 continue 
                            
                    else:
                        print("\nE-mail inválido. O e-mail deve conter '@'.")
                        time.sleep(3)
                        continue
                            
                elif atributo == "CNPJ":
                    nome_escolha = 'CNPJ'
                    titulo = 'cpf_cnpj'
                    
                    cnpj = re.sub(r'\D', '', input("\n- Novo CNPJ (10 dígitos, somente números. O 0001 será adicionado automaticamente.):\t"))
                    if len(cnpj) == 10 and cnpj.isdigit():
                        cnpj = cnpj[:8] + '0001' + cnpj[8:]
                        self._cpf_cnpj = int(cnpj)
                        update = self._cpf_cnpj
                        
                        for estabelecimento_banco in lista_estabelecimentos:
                            if estabelecimento_banco.cpf_cnpj == self._cpf_cnpj:
                                print('\n| CNPJ já cadastrado.')
                                time.sleep(3)
                                n_alterado = True
                                continue
                            
                    else:
                        print("\nNúmero de CNPJ inválido. Por favor, digite novamente.")
                        time.sleep(3)
                        continue
                            
                elif atributo == "Senha":
                    nome_escolha = 'Senha'
                    titulo = 'senha'
                    
                    senha = input("\n- Nova Senha:\t")
                    if len(senha) >= 6:
                        self._senha = senha
                        update = senha
                            
                    else:
                        print("\nA senha deve ter pelo menos 6 dígitos. Por favor, digite novamente.")
                        time.sleep(3)
                        continue                  
                
                if n_alterado == False:
                    
                    # Restrições de entrada
                    certeza = input("\nTem certeza que deseja salvar a alteração? (s/n):\t")
                    certeza_limpo = limpar_texto(certeza)
                    if (certeza_limpo != 's' and certeza_limpo != 'n'):
                        print("\n(Entrada Inválida!)")
                        time.sleep(2)
                        continue
                    elif certeza_limpo == 's':
                        
                        comando = f""" UPDATE Usuarios
                                        SET {titulo} = ?
                                        WHERE id = ?;"""
                        cursor.execute(comando,update,numero)
                        cursor.commit()
                        
                        if nome_escolha == 'Senha':
                            print(f'\n\n| {nome_escolha} alterada com sucesso!')
                            time.sleep(3)
                            return
                        else:
                            print(f'\n\n| {nome_escolha} alterado com sucesso!')
                            time.sleep(3)
                            return
                        
                    elif certeza_limpo == 'n':
                        return
                
            else:
                print("\n(Entrada Inválida!)")
                time.sleep(2)

    # Método que exibe os itens cadastrados no cardápio.
    def exibe_cardapio(self, estabelecimento) -> bool:
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
                input('\n\nPressione ENTER para voltar.\t')
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
            return True
        
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
        time.sleep(3) 

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
            
            while True:
                limpar_tela()
                print('\n------------------ Altera Item ------------------')
                print(f'\n\n1 - Nome:\t{item_encontrado.nome}')
                print(f'\n2 - Descrição:\t{item_encontrado.descricao}')
                print(f'\n3 - Preço:\tR${item_encontrado.preco:.2f}')
                
                escolha = input('\n\nQual atributo deseja modificar? (1, 2 ou 3):\t')
                escolha_limpo = limpar_texto(escolha)
                
                if (escolha_limpo != '1' and escolha_limpo != '2' and escolha_limpo != '3'):
                    print("\n(Entrada Inválida!)")
                    time.sleep(2)
                    continue
                
                if escolha_limpo == '1':
                    nome_escolha = 'Nome'
                    titulo = 'nome'
                    
                    consulta = "SELECT nome FROM Itens WHERE loja_id = ?"   #Consulta SQL
                    cursor.execute(consulta, (item_encontrado.loja_id,))   #Executa a consulta
                    resultados = cursor.fetchall()   #Recupera os resultados
                    nomes_dos_itens = [resultado[0] for resultado in resultados]   #Armazena os nomes na lista
                    
                    nome = input("\n- Novo Nome:\t")     
                    novo_nome_limpo = limpar_texto(nome)
                    nomes_dos_itens_limpo = [limpar_texto(n) for n in nomes_dos_itens]
                    
                    update = nome
                    
                    # Restrição de nome do produto já existente
                    if novo_nome_limpo in nomes_dos_itens_limpo:
                        print('\n\n| Nome já existente. Por favor, digite outro nome.')
                        time.sleep(3)
                        continue
                
                elif escolha_limpo == '2':
                    nome_escolha = 'Descrição'
                    titulo = 'descricao'
                    
                    nova_descricao = input("\n- Nova Descrição:\t")
                    update = nova_descricao
                    if nova_descricao == item_encontrado.descricao:
                        print('\n\n| Descrição já existente. Por favor, digite outra descrição.')
                        time.sleep(3)
                        continue
                    
                elif escolha_limpo == '3':
                    nome_escolha = 'Preço'
                    titulo = 'preco'
                    
                    try:
                        preco_str = input("\n- Novo Preço:\tR$")
                        # Substitui ',' por '.' para permitir ambas as entradas
                        preco_str = preco_str.replace(',', '.')
                        update = float(preco_str)
                        
                        # Verifica se o preço é positivo
                        if update <= 0:
                            raise ValueError
                        
                        if update == item_encontrado.preco:
                            print('\n\n| Mesmo preço. Por favor, digite outro valor.')
                            time.sleep(3)
                            continue

                    except ValueError:
                        print("\n(Valor Inválido!)")
                        time.sleep(2)
                        continue
                    
                # Restrições de entrada
                certeza = input("\n| Deseja confirmar a alteração? (s/n):\t")
                certeza_limpo = limpar_texto(certeza)
                
                if (certeza_limpo != 's' and certeza_limpo != 'n'):
                    print("\n(Entrada Inválida!)")
                    time.sleep(2)
                    continue
                elif certeza_limpo == 'n':
                    return
                elif certeza_limpo == 's':
                                              
                    comando = f""" UPDATE Itens
                                    SET {titulo} = ?
                                    WHERE item_id = ?;"""
                    cursor.execute(comando,update,item_encontrado.item_id)
                    cursor.commit()
                    
                    if nome_escolha == 'Descrição':
                        print(f'\n\n| {nome_escolha} alterada com sucesso!')
                        time.sleep(3)
                        return
                    else:
                        print(f'\n\n| {nome_escolha} alterado com sucesso!')
                        time.sleep(3)
                        return
                    
        else:
            print('\n(Nome Inválido!)')
            time.sleep(2)
            return