

from pickle import TRUE
import time
from click import pause
from Usuario import Usuario
from Cliente import Cliente
from Estabelecimento import Estabelecimento
from Sistema import Sistema
from typing import Type


if __name__ == "__main__":

    #Classes
    sistema1 = Sistema()
    usuario1 = Usuario()
    # cliente1 = Cliente()
    # estabelecimento1 = Estabelecimento()
    
    def menu_inicial():

        #Variáveis auxiliares
        conta_existe = None
        opcao = None
        cliente1 = Cliente()
        estabelecimento1 = Estabelecimento()
        
        while True:
            print('\033[H\033[2J')
            print("-----------------  UFMGFood  -----------------\n\n")
            print("| O melhor aplicativo de delivery da UFMG!\n")
            print('1 - Login')
            print('2 - Cadastrar')
            print('9 - Sair')
            
            conta_existe = input("\n\nDigite a opção desejada:\t")
            
            if conta_existe == '1':
                
                login = sistema1.login_usuario()

                if login == True:
                        usuario1 = sistema1.retorna_dados_usuario()
                        
                        if usuario1.tipo == 'Cliente':
                            cliente1 = usuario1
                            menu_app_cliente(cliente1)

                        if usuario1.tipo == 'Estabelecimento':
                            estabelecimento1 = usuario1
                            menu_app_estabelecimento(estabelecimento1)
                        
                

            if conta_existe == '2':

                opcao = None
                while opcao != '9':
                    print('\033[H\033[2J')
                    print('--------------  Cadastro   --------------\n\n')
                    print('1 - Cadastrar como cliente')
                    print('2 - Cadastrar como estabelecimento')
                    print('9 - Voltar')
                    opcao = input("\n\nDigite a opção desejada:\t")
                    
                    if opcao == '1':
                        cliente1.cria_Usuario()
                        sistema1.cria_cadastro_cliente(cliente1)
                        print('\033[H\033[2J')
                        break

                    if opcao == '2':
                        estabelecimento1.cria_Usuario()
                        sistema1.cria_cadastro_estabelecimento(estabelecimento1)  
                        break

                    if opcao == '9':
                        print('\033[H\033[2J')
                        break
                    
            if conta_existe == '9':
                sair = None
                sair = input('\nTem certeza que deseja sair do app? \t(s/n)\n')
                if sair == 's':
                    print(f"\n| UFMGFood te aguarda em breve!")
                    time.sleep(3)
                    break
                if sair == 'n':
                    pass
                

    def menu_app_cliente(cliente):

        while True:
            print('\033[H\033[2J')
            print("-----------------  UFMGFood  -----------------\n\n")
            print(f"| Olá, {cliente.nome}!\n")
            print('1 - Início')
            print('2 - Busca')
            print('3 - Pedidos')
            print('4 - Perfil')
            print('9 - Logout')
            
            opcao = None
            opcao = input('\nDigite a opção desejada:\t')
                        
            if opcao == '1':
                print('\033[H\033[2J')
                print("-----------------  Lista de Estabelecimentos  -----------------\n\n")
                pass

            if opcao == '2':
                print('\033[H\033[2J')
                pass

            if opcao == '3':
                print('\033[H\033[2J')
                print("-----------------  Seus Pedidos  -----------------\n\n")
                pass

            if opcao == '4':
                print('\033[H\033[2J')
                print("-----------------  Seus Dados  -----------------\n\n")
                print(f"| Nome: {cliente.nome}")
                print(f"| Endereço: {cliente.endereco}")
                print(f"| Telefone: {cliente.telefone}")
                print(f"| Email: {cliente.email}")
                print(f"| CPF: {cliente.cpf_cnpj}")
                input('\nPressione qualquer tecla para voltar\n')
                
            
            sair = None
            if opcao == '9':
                sair = input('\nTem certeza que deseja desconectar? \t(s/n)\n')
                if sair == 's':
                    print(f"\n| Desconectando {cliente.nome}")
                    time.sleep(3)
                    break
                if sair == 'n':
                    pass


    def menu_app_estabelecimento(estabelecimento):

        estab_classe = Estabelecimento() #variavel auxiliar

        while True:
            print('\033[H\033[2J')
            print("-----------------  UFMGFood  -----------------\n")
            print(f"\n| Olá, {estabelecimento.nome}!\n")
            print('1 - Pedidos Pendentes')
            print('2 - Pedidos Finalizados')
            print('3 - Cardápio')
            print('4 - Perfil')
            print('9 - Sair')
            
            opcao = None
            opcao = input('\nDigite a opção desejada:\t')

            if opcao == '3':

                pg = None
                while pg != '9':
                    print('\033[H\033[2J')
                    print(f"-----------------  Cardápio -{estabelecimento.nome}  -----------------\n\n")
                    #estab_classe.exibe_cardapio(estabelecimento)
                    print('1 - Cadastram Novo Item')
                    print('2 - Alterar Item')
                    print('3 - Remover Item')
                    print('9 - Sair')
                    pg = input('\nDigite a opção desejada:\t')
                    if pg == '1':
                        estab_classe.cadastra_item(estabelecimento)
                    
                    if pg == '9':
                        break

            if opcao == '4':
                print('\033[H\033[2J')
                print("-----------------  Seus Dados  -----------------\n\n")
                print(f"| Nome: {estabelecimento.nome}")
                print(f"| Endereço: {estabelecimento.endereco}")
                print(f"| Telefone: {estabelecimento.telefone}")
                print(f"| Email: {estabelecimento.email}")
                print(f"| CNPJ: {estabelecimento.cpf_cnpj}")
                input('\nPressione qualquer tecla para voltar\n')
            
            sair = None
            if opcao == '9':
                sair = input('\nTem certeza que deseja desconectar? \t(s/n)\n')
                if sair == 's':
                    print(f"\n| Desconectando {estabelecimento.nome}")
                    time.sleep(3)
                    break
                if sair == 'n':
                    pass
        
        
    menu_inicial()
        