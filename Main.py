import time
from Usuario import Usuario
from Cliente import Cliente
from Estabelecimento import Estabelecimento
from Sistema import Sistema
from Pedido import Pedido
from Utilitarios import limpar_tela, limpar_texto



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
            limpar_tela()
            print("-----------------  UFMGFood  -----------------\n\n")
            print("| O melhor aplicativo de delivery da UFMG!\n")
            print('1 - Login')
            print('2 - Cadastrar')
            print('0 - Sair')
            
            conta_existe = input("\n\nDigite a opção desejada:\t")
            
            if conta_existe == '1':
                
                login = sistema1.login_usuario()

                if login == True:
                        usuario1 = sistema1.retorna_dados_usuario()
                        
                        if usuario1.tipo == 'Cliente':
                            limpar_tela()
                            cliente1 = usuario1
                            menu_app_cliente(cliente1)

                        if usuario1.tipo == 'Estabelecimento':
                            limpar_tela()
                            estabelecimento1 = usuario1
                            menu_app_estabelecimento(estabelecimento1)
                        
                

            if conta_existe == '2':

                opcao = None
                while opcao != '9':
                    limpar_tela()
                    print('--------------  Cadastro   --------------\n\n')
                    print('1 - Cadastrar como cliente')
                    print('2 - Cadastrar como estabelecimento')
                    print('0 - Voltar')
                    opcao = input("\n\nDigite a opção desejada:\t")
                    
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
                    print(f"\n| UFMGFood te aguarda em breve!")
                    time.sleep(3)
                    break
                if sair == 'n':
                    pass
                

    def menu_app_cliente(cliente):

        while True:
            limpar_tela()
            print("-----------------  UFMGFood  -----------------\n\n")
            print(f"| Olá, {cliente.nome}!\n")
            print('1 - Estabelecimentos')
            print('2 - Produtos')
            print('3 - Pedidos')
            print('4 - Perfil')
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
                pass

            if opcao == '3':
                limpar_tela()
                pedido_aux = Pedido()
                pedido_aux.historico_pedidos_cliente(cliente)

            limpar_tela()
            if opcao == '4':
                limpar_tela()
                print("-----------------  Seus Dados  -----------------\n\n")
                print(f"| Nome: {cliente.nome}")
                print(f"| Endereço: {cliente.endereco}")
                print(f"| Telefone: {cliente.telefone}")
                print(f"| Email: {cliente.email}")
                print(f"| CPF: {cliente.cpf_cnpj}")
                input('\nPressione ENTER para voltar\n')
                
            sair = None
            if opcao == '0':
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
                        estab_classe.atualiza_Usuario()
                        
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
        