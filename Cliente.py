####################### BANCO DE DADOS ######################

from Conex_SQL import connection

cursor = connection.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################

import re
import time
from Usuario import Usuario
from Utilitarios import limpar_tela, limpar_texto

class Cliente(Usuario):
    # Constantes
    # Regex para garantir que o telefone tenha exatamente 11 dígitos
    padrao_telefone = r"^\d{11}$"
    # Regex para garantir que o nome só contenha letras e espaços
    padrao_nome = r"^[a-zA-ZÀ-ÿ ]+$"
    # Regex para garantir que o cpf tenha exatamente 11 dígitos
    padrao_cpf = r"^\d{11}$"

    def __init__(self):
        super().__init__()
        self._nome = None
        self._endereco = None
        self._telefone = None
        self._email = None
        self._cpf_cnpj = None
        self._senha = None
        self.tipo = self.__class__.__name__

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
                if len(nome.split()) >= 2 and re.fullmatch(self.padrao_nome, nome):
                    self._nome = nome
                    break
                else:
                    print(
                        "Nome inválido. Por favor, digite um nome com no mínimo nome e sobrenome, contendo apenas letras e espaços.")
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

        # Tratamento de exceção para o cpf
        while True:
            try:
                if self.tipo == 'Cliente':
                    cpf = re.sub(r'\D', '', input(
                        "CPF (11 dígitos somente números.): "))
                    if re.fullmatch(self.padrao_cpf, cpf):
                        self._cpf_cnpj = int(cpf)
                        break
                    else:
                        print("Número de CPF inválido. Por favor, digite novamente.")
            except:
                print("Número de CPF inválido. Por favor, digite novamente.")

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
        lista_clientes  = []
        for busca in tabela:
            lista_clientes.append(busca) 
        
        atributos = {
            "1": "Nome",
            "2": "Endereço",
            "3": "Telefone",
            "4": "E-mail",
            "5": "CPF",
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
                    if len(nome.split()) >= 2 and re.fullmatch(self.padrao_nome, nome):
                        self._nome = nome
                        update = self._nome
                        
                    else:
                        print("\nNome inválido. Por favor, digite um nome com no mínimo nome e sobrenome, contendo apenas letras e espaços.")
                        time.sleep(4)
                        continue
                    
                elif atributo == "Endereço":
                    nome_escolha = "Endereço"
                    titulo = 'endereco'
                    
                    self._endereco = str(input("\n- Novo Endereço:\t"))
                    update = self._endereco
                        
                elif atributo == "Telefone":
                    nome_escolha = 'Telefone'
                    titulo = 'telefone'
                    
                    telefone = input("\n- Novo Telefone (11 dígitos com DDD):\t")
                    if re.fullmatch(self.padrao_telefone, telefone):
                        self._telefone = int(telefone)
                        update = self._telefone
                        
                        for cliente_banco in lista_usuarios:
                            if cliente_banco.telefone == self._telefone: #alterei para email ou cpf/cnpj iguais
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
                        
                        for cliente_banco in lista_usuarios:
                            
                            if limpar_texto(cliente_banco.email) == limpar_texto(self._email):
                                 print('\n| E-mail já cadastrado.')
                                 time.sleep(3)
                                 n_alterado = True
                                 continue 
                            
                    else:
                        print("\nE-mail inválido. O e-mail deve conter '@'.")
                        time.sleep(3)
                        continue
                
                elif atributo == "CPF":
                    nome_escolha = 'CPF'
                    titulo = 'cpf_cnpj'
                    
                    cpf = re.sub(r'\D', '', input("\n- Novo CPF (11 dígitos, somente números.):\t"))
                    if re.fullmatch(self.padrao_cpf, cpf):
                        self._cpf_cnpj = int(cpf)
                        update = self._cpf_cnpj
                        
                        for cliente_banco in lista_clientes:
                            if cliente_banco.cpf_cnpj == self._cpf_cnpj:
                                print('\n| CPF já cadastrado.')
                                time.sleep(3)
                                n_alterado = True
                                continue
                            
                    else:
                        print("\nNúmero de CPF inválido. Por favor, digite novamente.")
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