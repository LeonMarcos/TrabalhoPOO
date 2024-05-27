


####################### BANCO DE DADOS ######################

from Conex_SQL import connection


cursor = connection.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################

from Carrinho import Carrinho
from Usuario import Usuario
from Cliente import Cliente
from Estabelecimento import Estabelecimento
from typing import Type
import time

dados_usuario = None

class Sistema:
    # Atributos e construtor da classe Sistema
    def __init__(self) -> None:
        self.__lista_de_usuarios = []
        self.__lista_de_estabelecimentos = []
        self.__numeros_estabelecimentos = []

    def salva_dados_usuario(self, usuario):  
        self.dados_usuario = usuario
         
    
    def retorna_dados_usuario(self):
         return self.dados_usuario

        
        
    # método que verifica se o cliente existe na lista de cliente
    def __verifica_login_usuario(self, usuario: Type[Usuario]) -> bool:
        usuario_login = usuario
        consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados
        cursor.execute(consulta) 
        tabela = cursor.fetchall()
        self.__lista_de_usuarios  = []
        for busca in tabela:
            self.__lista_de_usuarios.append(busca)
        
        if usuario_login.get_email() == None and usuario_login.get_senha() == None:
           login_email = input("\nDigite seu e-mail: ")
           login_senha = input("Digite sua senha: ")
           
           for usuario_banco in self.__lista_de_usuarios:
               if usuario_banco.email == login_email and \
                   usuario_banco.senha == login_senha:
                        self.salva_dados_usuario(usuario_banco) #tem que retornar os dados do cliente tbm e não só se o login foi aprovado
                        return True
                           
        else:         
            for usuario_banco in self.__lista_de_usuarios :
                if usuario_banco.email == usuario_login._email:
                    print('| Email já cadastrado por outro usuário!')
                    time.sleep(3)
                    print('\033[H\033[2J') 
                    return True 
                
                if usuario_banco.cpf_cnpj == usuario_login._cpf_cnpj: #alterei para email OU cpf/cnpj iguais
                    print('| CPF já cadastrado por outro usuário!')
                    time.sleep(3)
                    print('\033[H\033[2J') 
                    return True
                     
        return False
     
    
    # método que retorna o cliente
    def login_usuario(self) -> bool:
        
        print('\033[H\033[2J')
        usuario_classe = Usuario()      
        print(f"-------------- Login --------------\n")
        login = None 
        login = self.__verifica_login_usuario(usuario_classe)
        print('\n---------------------------------------')
        
        if login == True:
            print("\n| O login foi efetuado com sucesso!")
            time.sleep(3)
            print('\033[H\033[2J') 
        else:
            login = False
            print("\n| O login não é válido.")
            time.sleep(3)
            print('\033[H\033[2J')
            
            
        return login
    
        
    
    # método que cria um cadastro para cliente   
    def cria_cadastro_cliente(self, cliente: Type[Cliente]) -> None:
        cliente = cliente
        cliente_existente = None
        cliente_existente = self.__verifica_login_usuario(cliente)
        
        if cliente_existente == False:
            comando = """ INSERT INTO Usuarios(nome, endereco, telefone, email, cpf_cnpj, senha, tipo)
            VALUES
              (?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(comando, cliente._nome, cliente._endereco, cliente._telefone, cliente._email, cliente._cpf_cnpj, cliente._senha, cliente.tipo )
            cursor.commit()
            consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados
            cursor.execute(consulta) 
            tabela = cursor.fetchall()
            self.__lista_de_clientes  = []
            for busca in tabela:
             self.__lista_de_clientes .append(busca)

            print("\n| O cadastro foi realizado com sucesso!")
            time.sleep(3)
            print('\033[H\033[2J') 
            

        else:
            #cliente já cadastrado - Resposta ao usuário na função verifica_login
            pass
            
    # método que verifica se o estabelecimento existe na lista de estabelecimento
    def __verifica_login_estabelecimento(self, estabelecimento: Type[Estabelecimento]) -> bool:
        estabelecimento_login = estabelecimento
        consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados
        cursor.execute(consulta) 
        tabela = cursor.fetchall()
        self.__lista_de_estabelecimentos  = []
        for busca in tabela:
            self.__lista_de_estabelecimentos.append(busca)
        if estabelecimento_login.get_email() == None and estabelecimento_login.get_senha() == None:
           login_email = input("\nDigite seu e-mail: ")
           login_senha = input("Digite sua senha: ")
           for estabelecimento_banco in self.__lista_de_estabelecimentos:
               if estabelecimento_banco.email == login_email and \
                   estabelecimento_banco.senha == login_senha:
                       return True    
        else:    
            for estabelecimento_banco in self.__lista_de_estabelecimentos:
                if estabelecimento_banco.email == estabelecimento_login._email:
                     print('| Email já cadastrado por outro usuário!')
                     time.sleep(3)
                     print('\033[H\033[2J') 
                     return True 
                if estabelecimento_banco.cpf_cnpj == estabelecimento_login._cpf_cnpj: #alterei para email ou cpf/cnpj iguais
                    print('| CNPJ já cadastrado por outro usuário!')
                    time.sleep(3)
                    print('\033[H\033[2J') 
                    return True
        return False       
    
    # método que cria um cadastro para estabelecimento   
    def cria_cadastro_estabelecimento(self, estabelecimento: Type[Estabelecimento]) -> None:
        estabelecimento = estabelecimento
        estabelecimento_existente = None
        estabelecimento_existente = self.__verifica_login_estabelecimento(estabelecimento)
        if estabelecimento_existente == False:
            comando = """ INSERT INTO Usuarios(nome, endereco, telefone, email, cpf_cnpj, senha, tipo)
            VALUES
              (?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(comando, estabelecimento._nome, estabelecimento._endereco, estabelecimento._telefone, estabelecimento._email, estabelecimento._cpf_cnpj, estabelecimento._senha, estabelecimento.tipo )
            cursor.commit()
            consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados
            cursor.execute(consulta) 
            tabela = cursor.fetchall()
            self.__lista_de_estabelecimentos  = []
            for busca in tabela:
                self.__lista_de_estabelecimentos.append(busca)
            print("\n|O cadastro foi realizado com sucesso!")
            time.sleep(3)
            print('\033[H\033[2J') 
        else:
            #estabelecimento já cadastrado - Resposta ao usuário na função verifica_login
            pass
            
    # Método que exibe uma lista de estabelecimentos cadastrados e associa cada estabelecimento a um número inteiro diferente
    def exibe_estabelecimentos(self, cliente) ->"Estabelecimento":
        cliente = cliente
        carrinho_aux = Carrinho()
        
        consulta = """ SELECT * FROM Usuarios
                        WHERE tipo = 'Estabelecimento';
           """ #consulta o banco de dados
        cursor.execute(consulta) 
        tabela = cursor.fetchall()
        self.__lista_de_estabelecimentos  = []
        self.__numeros_estabelecimentos = []
        for busca in tabela:
            self.__lista_de_estabelecimentos.append(busca)

        # self.__lista_de_estabelecimentos = [] # tirar comentário para simular nenhum estabelecimento cadastrado
        if not self.__lista_de_estabelecimentos:
            print("\n| Não existem estabelecimento cadastradas no aplicativo.")
            time.sleep(3)
        else:
            while True:
                print('\033[H\033[2J')
                print("-----------------  Lista de Estabelecimentos  -----------------\n")
                numero = 0
                
                for estab in self.__lista_de_estabelecimentos:
                    numero = numero + 1
                    print(estab.id,"–", estab.nome)
                    if not numero in self.__numeros_estabelecimentos:
                        self.__numeros_estabelecimentos.append(numero)
                        #self.__lista_de_estabelecimentos.append(estabelecimento)
                    print("-"*50)
                print("0 – Voltar") 
                
                navegar = 0
                navegar = int(input('\nDigite a opção desejada:\t'))
                
                for proc in self.__lista_de_estabelecimentos:
                    if proc.id == navegar:
                            print('\033[H\033[2J')
                            carrinho_aux.menu(proc, cliente)
                            return False
                            
                            

                if navegar == 0:
                    return False
        
            
            
        
            
if __name__ == "__main__":
    
        sistemaum = Sistema()    
        estabelecimentoum = Estabelecimento()
        
        estabelecimentoum.cria_Usuario()
        print("\n")
        print(estabelecimentoum.get_nome())
        print(estabelecimentoum.get_endereco())
        print(estabelecimentoum.get_telefone())
        print(estabelecimentoum.get_email())
        print(estabelecimentoum.get_cpf_cnpj())
        print(estabelecimentoum.get_senha())
        
        sistemaum.cria_cadastro_estabelecimento(estabelecimentoum) 
        
        estabelecimentodois = Estabelecimento()
        estabelecimentodois.cria_Usuario()
        sistemaum.cria_cadastro_estabelecimento(estabelecimentodois)
        
        sistemaum.exibe_estabelecimentos()
        