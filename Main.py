####################### BANCO DE DADOS ######################

from Conex_SQL import connection

cursor = connection.cursor() #utiliza-se o cursor para apontar para as variaveis dentro do sql

#############################################################

import time
from Cliente import Cliente
from Estabelecimento import Estabelecimento
from Sistema import Sistema
from Pedido import Pedido
from Utilitarios import limpar_tela, limpar_texto


if __name__ == "__main__":

    #Classes
    sistema1 = Sistema()
    
    def menu_inicial()->None:

        #Variáveis auxiliares
        conta_existe = None
        opcao = None
        
        
        while True:
            limpar_tela()
            print("-----------------  UFMGFood  -----------------\n\n")
            print("| O melhor aplicativo de delivery da UFMG!\n")
            print('1 - Login')
            print('2 - Cadastrar')
            print('0 - Sair')
            
            conta_existe = input("\n\nDigite a opção desejada:\t")
            
            if conta_existe == '1':
                limpar_tela()
                print("-----------------  Login  -----------------\n\n")
                print("Fazer login como:")
                print('\n1 - Cliente')
                print('2 - Estabelecimento')
                print('\n0 - Voltar.')
                
                opcao_login = input("\n\nDigite a opção desejada:\t")
                
                cliente1 = Cliente()
                estabelecimento1 = Estabelecimento()
                
                if opcao_login == '0':
                    continue
                
                # Login de usuário
                login = sistema1.login_usuario(cliente1 if opcao_login == '1' else estabelecimento1)
                            
                if login:
                    usuario = sistema1.retorna_dados_usuario()
            
                    if usuario.tipo == 'Cliente':
                        limpar_tela()
                        cliente1 = usuario
                        menu_app_cliente(cliente1)
            
                    else:
                        limpar_tela()
                        estabelecimento1 = usuario
                        menu_app_estabelecimento(estabelecimento1)
                        

            if conta_existe == '2':

                opcao = None
                while opcao != '9':
                    limpar_tela()
                    print('--------------  Cadastro   --------------\n\n')
                    print('1 - Cadastrar como Cliente.')
                    print('2 - Cadastrar como Estabelecimento.')
                    print('0 - Voltar.')
                    opcao = input("\nDigite a opção desejada:\t")
                    
                    if opcao == '1':
                        limpar_tela()
                        cliente1.cria_Usuario()
                        sistema1.cria_cadastro_cliente(cliente1)
                        break

                    if opcao == '2':
                        limpar_tela()
                        estabelecimento1.cria_Usuario()
                        sistema1.cria_cadastro_estabelecimento(estabelecimento1)  
                        break

                    if opcao == '0':
                        limpar_tela()
                        break
                    
            if conta_existe == '0':
                sair = None
                sair = input('\nTem certeza que deseja sair do app? \t(s/n)\n')
                if sair == 's':
                    print("\n| UFMGFood te aguarda em breve!")
                    time.sleep(3)
                    break
                if sair == 'n':
                    pass
                

    def menu_app_cliente(cliente:Cliente)->None:
        
        client_classe = Cliente()

        while True:
            limpar_tela()
            print("-----------------  UFMGFood  -----------------\n\n")
            print(f"| Olá, {cliente.nome}!\n")
            print('1 - Início')
            print('2 - Pedidos')
            print('3 - Perfil')
            print('0 - Logout')
            
            opcao = None
            opcao = input('\nDigite a opção desejada:\t')
            limpar_tela()
                        
            if opcao == '1':
                limpar_tela()
                print("-----------------  Lista de Estabelecimentos  -----------------\n\n")
                sistema1.exibe_estabelecimentos(cliente)

            if opcao == '2':
                limpar_tela()
                pedido_aux = Pedido()
                pedido_aux.historico_pedidos_cliente(cliente)

            limpar_tela()
            if opcao == '3':
                a=1
                while a:
                    consulta = """ SELECT * FROM Usuarios WHERE id = ?; """  # consulta o banco de dados
                    cursor.execute(consulta, cliente.id)
                    tabela = cursor.fetchall()
                    usuarios = []
                    for busca in tabela:
                        usuarios.append(busca)
                    
                    for client in usuarios:
                        if client.id == cliente.id:
                            cliente = client
                            break
                    exb_dados = None
                    limpar_tela()
                    print("-----------------  Seus Dados  -----------------\n\n")
                    print(f"| Nome: {cliente.nome}")
                    print(f"| Endereço: {cliente.endereco}")
                    print(f"| Telefone: {cliente.telefone}")
                    print(f"| Email: {cliente.email}")
                    print(f"| CPF: {cliente.cpf_cnpj}")
                    
                    exb_dados = input('\nDeseja alterar seus dados? (s/n):\t')
                    exb_dados_limpo = limpar_texto(exb_dados)
                    
                    if (exb_dados_limpo != 's' and exb_dados_limpo != 'n'):
                        print("\n(Entrada Inválida!)")
                        time.sleep(2)
                        continue                   
                
                    elif exb_dados_limpo == 's':
                        
                        if client_classe.atualiza_Usuario(cliente.id):
                            continue
                        
                    elif exb_dados_limpo == 'n':
                        a = 0
                
            sair = None
            if opcao == '0':
                sair = input('\nTem certeza que deseja desconectar? \t(s/n)\n')
                if sair == 's':
                    print(f"\n| Desconectando {cliente.nome}")
                    time.sleep(3)
                    break
                if sair == 'n':
                    pass


    def menu_app_estabelecimento(estabelecimento:Estabelecimento)->None:

        estab_classe = Estabelecimento() #variavel auxiliar

        while True:
            limpar_tela()
            print("-----------------  UFMGFood  -----------------\n")
            print(f"\n| Olá, {estabelecimento.nome}!\n")
            print('1 - Pedidos Pendentes')
            print('2 - Pedidos Finalizados')
            print('3 - Cardápio')
            print('4 - Perfil')
            print('0 - Sair')
            
            opcao = None
            opcao = input('\nDigite a opção desejada:\t')

            if opcao == '1':
                limpar_tela()
                pedido_aux = Pedido()
                pedido_aux.historico_pedidos_estabelecimento(estabelecimento,'Pendente')

            if opcao == '2':
                limpar_tela()
                pedido_aux = Pedido()
                pedido_aux.historico_pedidos_estabelecimento(estabelecimento,'Finalizado')

            if opcao == '3':
                
                pg = None
                while pg != '0':
                    limpar_tela()
                    estab_classe.exibe_cardapio(estabelecimento)
                    print('\n1 - Cadastrar Novo Item.')
                    print('2 - Alterar Item.')
                    print('3 - Remover Item.')
                    print('0 - Voltar.')
                    pg = input('\nDigite a opção desejada:\t')
                    
                    if pg == '1':
                        estab_classe.cadastra_item(estabelecimento)
                        
                    elif pg == '2':
                        if estab_classe.altera_item_cardapio():
                            continue
                        
                    elif pg == '3':
                        if estab_classe.remove_item_cardapio():
                            continue
                    
                    elif pg == '0':
                        break
            limpar_tela()
            if opcao == '4':
                a=1
                while a:
                    consulta = """ SELECT * FROM Usuarios WHERE id = ?; """  # consulta o banco de dados
                    cursor.execute(consulta, estabelecimento.id)
                    tabela = cursor.fetchall()
                    usuarios = []
                    for busca in tabela:
                        usuarios.append(busca)
                    
                    for estab in usuarios:
                        if estab.id == estabelecimento.id:
                            estabelecimento = estab
                            break
                    exb_dados = None
                    limpar_tela()
                    print("-----------------  Seus Dados  -----------------\n\n")
                    print(f"| Nome: {estabelecimento.nome}")
                    print(f"| Endereço: {estabelecimento.endereco}")
                    print(f"| Telefone: {estabelecimento.telefone}")
                    print(f"| Email: {estabelecimento.email}")
                    print(f"| CNPJ: {estabelecimento.cpf_cnpj}")
                    
                    exb_dados = input('\nDeseja alterar seus dados? (s/n):\t')
                    exb_dados_limpo = limpar_texto(exb_dados)
                    
                    if (exb_dados_limpo != 's' and exb_dados_limpo != 'n'):
                        print("\n(Entrada Inválida!)")
                        time.sleep(2)
                        continue                   
                
                    elif exb_dados_limpo == 's':
                        
                        if estab_classe.atualiza_Usuario(estabelecimento.id):
                            continue
                        
                    elif exb_dados_limpo == 'n':
                        a = 0
                        

            
            sair = None
            if opcao == '0':
                sair = input('\nTem certeza que deseja desconectar? \t(s/n)\n')
                if sair == 's':
                    print(f"\n| Desconectando {estabelecimento.nome}")
                    time.sleep(3)
                    break
                if sair == 'n':
                    pass
        
        
    menu_inicial()
        