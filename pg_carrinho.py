from ctypes import alignment
from decimal import Decimal
from cgitb import text
from itertools import product
from multiprocessing import Value
from textwrap import wrap
import time
from tkinter import Scrollbar
from tkinter.tix import DisplayStyle, Tree
from turtle import bgcolor, color, title
from typing import Text
from wsgiref import validate
from annotated_types import T
import flet as ft
import pyodbc
from Cliente import Cliente
from Conex_SQL import connection
from Estabelecimento import Estabelecimento
from Carrinho import Carrinho
from Pedido import Pedido
from types import SimpleNamespace
import pg_aux
import datetime
import asyncio
import pg_login
import pg_inicio

cliente_teste = Cliente()


cursor = connection.cursor()

tabela = []
def cardapio(id):
    consulta = """ SELECT * FROM Itens
                        WHERE loja_id = ?;
            """ #consulta o banco de dados
    cursor.execute(consulta,id) 
    aux = cursor.fetchall()
    tabela.clear()
    for p in aux:
         tabela.append(p)

dados_estabelecimento = []
def busca(id):
    busca_estabelecimento = """ SELECT * FROM Usuarios
                        WHERE id = ?;
            """ #consulta o banco de dados
    cursor.execute(busca_estabelecimento,id) 
    aux = cursor.fetchall()
    dados_estabelecimento.clear()
    for p in aux:
         dados_estabelecimento.append(p)

lista_carrinho = []

estab_provisorio = None
item_provisorio = None


def page_cardapio_cliente(page: ft.Page):
    
    
    # print(cliente)
    estabelecimento = pg_inicio.retorna_estab()
    cliente_teste = pg_login.retorna_dados_usuario()
    
    print(cliente_teste)
    cardapio(estabelecimento.id)

    page.bgcolor = '#ffffff'
    page.window_title_bar_hidden = False
    page.window_resizable = True
    page.window_width = 725
    # page.window_height = 1047
    page.window_height = 760
    page.window_max_width = 725


# CARRINHO ##################################################################################
    
    
    msg_add = ft.Row(controls=[
        ft.Icon(name=ft.icons.CHECK_CIRCLE,color='#ffffff'),
        ft.Text(
                value="Produto adicionado ao carrinho!",
                color='#ffffff',
                size=20),
    ])

    item_add = ft.SnackBar(
                    elevation= 1,
                    content=msg_add,
                    bgcolor='#0f6e72',
                    duration=2000
                    )
    
    msg_limite = ft.Row(controls=[
        ft.Icon(name=ft.icons.CANCEL,color='#ffffff'),
        ft.Text(
                value="Limite de 10 unidades por produto!",
                color='#ffffff',
                size=20),
        
    ])

    item_limite = ft.SnackBar(
                    content=msg_limite,
                    bgcolor='#fa3839',
                    duration=2000
                    )
    
    def aviso_limite():
        page.show_snack_bar(item_limite)
        page.update()

    
    def aviso_add():
        page.show_snack_bar(item_add)
        page.update()

    def close_estab(e):
        aviso_estab_dif.open = False
        aviso_estab_dif.update()
        page.update()
    

    
    # ITENS DE DIFERENTES ESTABELECIMENTOS
    def estab_diferente(item, estab):
        global estab_provisorio, item_provisorio
        item_provisorio = item
        estab_provisorio = estab
        aviso_estab_dif.open = True
        aviso_estab_dif.update()
        page.update()
        
    
    def limpa_e_add(e):
        lista_carrinho.clear()
        global estab_provisorio, item_provisorio
        add_carrinho(item_provisorio, estab_provisorio)
        print('Carrinho',lista_carrinho)
        aviso_estab_dif.open = False
        aviso_estab_dif.update()
        page.update()

    
    aviso_estab_dif = ft.BottomSheet(
        ft.Container(
            ft.Column(
                controls=[
                    ft.Divider(height=10,color=ft.colors.TRANSPARENT),
                    ft.Text(value='Não é possível adicionar itens de diferentes estabelecimentos',
                            size=20,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD,                            
                            color=ft.colors.BLACK,),
                    ft.Text(value='Deseja esvaziar o carrinho e adicionar este item?',
                            size=20,
                            color=ft.colors.GREY_800),
                    ft.ElevatedButton(content=ft.Text(value='Esvaziar e adicionar',size=20),
                                    bgcolor='#ff312f',
                                    color='#ffffff',
                                    width=400,
                                    style=ft.ButtonStyle(
                                        shape= ft.RoundedRectangleBorder(radius=5)
                                        ),
                                    on_click= limpa_e_add
                                    ),
                    ft.TextButton(content=ft.Text(value='Voltar',size=20),
                                    style=ft.ButtonStyle(color='#ff312f'),
                                    width=400,
                                    on_click= close_estab
                                    ),
                ],
                horizontal_alignment= ft.CrossAxisAlignment.CENTER
            ),
            height=220,
            width=700,
        ),
        open=False,
        bgcolor='#ffffff',
    )

    page.overlay.append(aviso_estab_dif)



    # ADICIONAR AO CARRINHO
    def add_carrinho(item,estabelecimento):
        
        encontrado = False
        ok = True

        # Verificar se o item já está no carrinho
        for p in lista_carrinho:
   
            if p.estab_nome != estabelecimento.nome: #condição de seleção de itens de diferentes estabelecimentos
                ok = False
                estab_diferente(item,estabelecimento)
                break
                 
            if item.item_id == p.item_id:
                if p.quant_item< 10:
                    p.quant_item += 1
                    encontrado = True
                    aviso_add()

                if p.quant_item == 10:
                    encontrado = True
                    aviso_limite()
                    btn_visib()

        if not encontrado and ok == True:
            
                # Se o item não estiver no carrinho, adicionar como novo item
                novo_item = SimpleNamespace(item_id=item.item_id, loja_id = item.loja_id, nome = item.nome ,descricao = item.descricao ,preco = item.preco, estab_nome = estabelecimento.nome, quant_item=1, subtotal = item.preco ,nome_cliente = cliente_teste.get_nome(), cliente_id = cliente_teste.get_id(), endereco = cliente_teste.get_endereco())
                lista_carrinho.append(novo_item)
                aviso_add()
        btn_visib()

    total = 0
    
    
   
    total_text = ft.Text(value=f"{total}", size=20, color='#ff312f',style=ft.TextStyle(weight=ft.FontWeight.BOLD))
    page.update() 
            

    def itens_row(carrinho):
            
            carrinho.subtotal = carrinho.quant_item * carrinho.preco
            
            def excluir_item(page, item):
                lista_carrinho.remove(item)
                atualiza_total()
                if lista_carrinho == []:
                    btn_visib()
                    page.dialog.open = False
                    page.update()
                    car_limpo()
                    
                if lista_carrinho != []:
                    exibe_carrinho(page)
                    print (lista_carrinho)
                    
                    
                

            def atualiza_total():
                total = 0
                if lista_carrinho == []:
                    total = 0
                    total_text.value = total

                for p in lista_carrinho:
                    total += p.subtotal
                    total_text.value = total
                    page.update() 
                pass
            
            atualiza_total()

            def atualizar_quantidade(): # Atualiza os valores visíveis
                
                quantidade_text.value = carrinho.quant_item
                subtotal_text.value = carrinho.subtotal
                print(lista_carrinho)
                atualiza_total()
                
                
                page.update()

            def menos_click(e):
                if carrinho.quant_item > 1:
                    carrinho.quant_item -= 1
                    carrinho.subtotal = carrinho.quant_item * carrinho.preco
                    page.dialog.update()
                    
                    atualizar_quantidade()

            def mais_click(e):
                if carrinho.quant_item < 10:
                    carrinho.quant_item += 1
                    carrinho.subtotal = carrinho.quant_item * carrinho.preco
                    page.dialog.update()
                    aviso_add()
                    atualizar_quantidade()
            
            # Elementos que precisam ser atualizados
            quantidade_text = ft.Text(value=f"{carrinho.quant_item}", size=20, color=ft.colors.BLACK)
            subtotal_text = ft.Text(value=f"{carrinho.subtotal}", size=20, color=ft.colors.BLACK)

             
            return ft.Container(
                ft.Row(
                controls=[
                    ft.ElevatedButton(
                        content=ft.Icon(name=ft.icons.FASTFOOD_ROUNDED,size=50,color='#ff312f'),
                        width=100,
                        height=100,
                        style=ft.ButtonStyle(
                             shape= ft.RoundedRectangleBorder(radius=12),
                             bgcolor='#ffffff',
                             overlay_color='#ffffff'
                            )
                        ),
                    ft.ElevatedButton(
                        content=ft.Container(
                            content=ft.Row(
                                controls=[ft.Column(
                                    [
                                        ft.Text(value=carrinho.nome,size=20,color=ft.colors.BLACK),

                                        ft.Text(value=f"R${carrinho.preco}",size=15,color=ft.colors.GREY_700),
                                        
                                    ],
                                    # width=250,
                                    height=100,
                                    # spacing = 15,
                                    
                                    alignment= ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment= ft.CrossAxisAlignment.START,
                                    ),
                                    ft.Row( controls = [
                                        ft.IconButton(icon = ft.icons.REMOVE,icon_color='#ff312f', on_click=menos_click),
                                        quantidade_text,
                                        ft.IconButton(icon = ft.icons.ADD,icon_color='#ff312f', on_click=mais_click),
                                        ]
                                    ),
                                    ft.Row( controls = [
                                        ft.Text(value="R$",size=20,color=ft.colors.BLACK),
                                        subtotal_text
                                        ],
                                        spacing=1
                                    ),
                                    ft.IconButton(icon = ft.icons.DELETE,icon_color='#ff312f', on_click=lambda e: excluir_item(page, carrinho)),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                )
                            ),
                        style=ft.ButtonStyle(
                             shape= ft.RoundedRectangleBorder(radius=12),
                             bgcolor='#ffffff',
                             overlay_color='#ffffff'
                            ),
                            expand = True,
                        
                    ),
                ],
                    
                alignment=ft.MainAxisAlignment.START
            ),
            
        )
    
    msg_limpar = ft.Row(controls=[
        ft.Icon(name=ft.icons.REMOVE_SHOPPING_CART,color='#ffffff'),
        ft.Text(
                value="Seu carrinho está vazio agora!",
                color='#ffffff',
                size=20),
        
    ])

    car_limpar = ft.SnackBar(
                    content=msg_limpar,
                    bgcolor='#fa3839',
                    duration=2000
                    )
    def car_limpo():
        page.show_snack_bar(car_limpar)
        page.update()

    def limpar_carrinho(page):
        lista_carrinho.clear()
        page.dialog.open = False
        car_limpo()
        btn_visib()


    def exibe_carrinho(page):
        

        itens = [itens_row(carrinho) for carrinho in lista_carrinho]

        col = ft.Container(
                content=ft.Column(
                controls=itens,
                scroll=ft.ScrollMode.AUTO
                ),
                height=350,
                
            )
        nome_loja = None
        total = Decimal(0)
        endereco = None
        for p in lista_carrinho:
            total += p.subtotal
            endereco = p.endereco
            nome_loja = p.estab_nome

        titulo = ft.Container(
                content = ft.Column(
                        controls=[
                                # ft.Divider(height=5,color=ft.colors.TRANSPARENT),
                                ft.Row(controls=[
                                    ft.Icon(name=ft.icons.STOREFRONT,size=40,color='#ff312f'),
                                    ft.Text(value=f"{nome_loja}",size=30,color=ft.colors.BLACK)
                                    ],
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                                    ),
                                ft.Divider(height=5,color=ft.colors.TRANSPARENT),
                        ]
                ),
                border=ft.Border(
                    bottom=ft.BorderSide(0.85, ft.colors.GREY)
                    
                    ),
                width=600
                )

        # CAMPOS INFERIORES ###################

        info_final = ft.Container(
                content = ft.Column(
                        controls=[
                                ft.Divider(height=5,color=ft.colors.TRANSPARENT),
                                ft.Row(controls = [
                                        ft.Icon(name=ft.icons.CALCULATE_OUTLINED,size=30,color='#ff312f'),
                                        ft.Text(value=f" Valor total: ",size=20,color=ft.colors.BLACK),
                                        ft.Text(value=f"R$",size=20,color='#ff312f',style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                                        total_text
                                        ],
                                        spacing=1
                                    ),
                                ft.Row(controls = [
                                        ft.Icon(name=ft.icons.LOCATION_ON_OUTLINED,size=30,color='#ff312f'),
                                        ft.Text(value=f" Endereço de entrega: {endereco}",size=20,color=ft.colors.BLACK)
                                    ],
                                        spacing=1
                                ),
                                ft.Row(controls = [
                                        ft.Icon(name=ft.icons.INFO_OUTLINED,size=30,color='#ff312f'),
                                        ft.Text(value=f" Pagamento no ato da entrega!",size=20,color='#ff312f')
                                    ],
                                        spacing=1
                                )
                        ]
                ),
                border=ft.Border(
                    top=ft.BorderSide(0.85, ft.colors.GREY)
                    
                    ),
                expand=True
                )
        

        def close_carrinho(e):
             page.dialog.open = False
             page.update()
        
        msg_pedido = ft.Row(controls=[
        ft.Icon(name=ft.icons.FEED_OUTLINED,color='#ffffff'),
        ft.Text(
                value="Pedido Enviado!",
                color='#ffffff',
                size=20),
        
    ])

        pedido_enviado = ft.SnackBar(
                    content=msg_pedido,
                    bgcolor='#0f6e72',
                    duration=2000
                    )
        
            
        def finalizar_pedido(lista):
            data_hora_atual = datetime.datetime.now()
            data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y às %H:%M:%S") #Formata a data e a hora no formato desejado         
            data_horario_pedido = str(data_hora_formatada)
            lista_pedido =[]
            for p in lista:
                 lista_pedido.append(p)
            print('finalizou')
            lista_carrinho.clear()
            cursor.execute("SELECT MAX(id) FROM Pedidos")
            ultimo_id = cursor.fetchone()[0]
            id = ultimo_id + 1
            
            for p in lista_pedido:
                comando = """ INSERT INTO Pedidos(id, loja_id, cliente_id, id_item, quant_item, preco, subtotal, endereco, data_horario_pedido, status_pedido, nome_cliente, nome_loja, nome_item)
                VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                cursor.execute(comando, id, p.loja_id, p.cliente_id, p.item_id, p.quant_item, p.preco, p.subtotal, p.endereco, data_horario_pedido, 'Pendente', p.nome_cliente, p.estab_nome, p.nome)
                cursor.commit()

            page.dialog.open = False
            page.show_snack_bar(pedido_enviado)
            page.update()

            time.sleep(2.5)
            page.go('/pedidos')

        car = ft.AlertDialog(

            content=ft.Container(
                content=ft.Column(
                [
                     titulo,
                     col,
                     info_final
                          ],
                
                
                ),
                height=600,
                width=715
                

            ),

            actions=[
                ft.Row(controls = [
            ft.TextButton(  content=ft.Text("Voltar"),
                            style=ft.ButtonStyle(color= '#ff312f',bgcolor=ft.colors.TRANSPARENT),
                             on_click=close_carrinho),
            ft.TextButton(  content=ft.Text("Limpar"),
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#ff312f'),
                             on_click= lambda e: limpar_carrinho(page)),
            ft.TextButton(  content=ft.Text("Finalizar"),
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#036666'),
                            on_click=lambda e: finalizar_pedido(lista_carrinho,)),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        ],
        bgcolor = '#ffffff',
        
        )
        page.dialog = car
        car.open = True
        page.update()

       
    
    btn_car = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name=ft.icons.SHOPPING_CART_OUTLINED,size=25),
                ft.Text(value='CARRINHO',size=20)
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),

        on_click=lambda e: exibe_carrinho(page),
        width=700,
        height=50,
        bgcolor='#ff312f',
        color='#ffffff',
        style=ft.ButtonStyle(
            shape= ft.RoundedRectangleBorder(radius=5),
            overlay_color='#0d1b2a'
        ),

    )
    
    def btn_visib():
        if lista_carrinho != []:  # Verificar se o carrinho está vazio
            btn_car.visible = True
        if lista_carrinho == []:
            btn_car.visible = False
        page.update()

# MENSAGEM INICIAL ########################################################################### 
    
    nome = [ft.Text(
            value=f"| Cardápio - {estabelecimento.nome}",
            color=ft.colors.BLACK,
            size=25,)]    

    welcome = ft.Column(
          controls=nome,
          alignment=ft.CrossAxisAlignment.CENTER,
          width=600,
          )
    btn_back = ft.ElevatedButton(   
                                content=ft.Icon(name=ft.icons.ARROW_BACK,
                                                color='#ff312f',
                                                size=30
                                                ),
                                bgcolor='#ffffff',
                                on_click=lambda e: page.go('/inicio')
                                ),

    back = ft.Column(
              controls=btn_back
        )
    
# LISTA DE ITENS ###########################################################################
    btn_visib()
    def create_product_row(item):
            # estabelecimento = pg_aux.variavel_auxiliar_geral_2
            cardapio(estabelecimento.id)

            return ft.Container(
                    ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            content=ft.Icon(name=ft.icons.FASTFOOD_ROUNDED,size=50,color='#ff312f'),
                            width=100,
                            height=100,
                            style=ft.ButtonStyle(
                                shape= ft.RoundedRectangleBorder(radius=12),
                                bgcolor= '#ffffff',
                                overlay_color='#ffffff',
                                        
                                )
                            ),
                        ft.ElevatedButton(
                            content=ft.Container(
                                content=ft.Row(
                                    controls=[ft.Column(
                                        [
                                            ft.Text(value=item.nome,size=20,color=ft.colors.BLACK),
                                            ft.Text(value=item.descricao,size=15,color=ft.colors.GREY_700),
                                            
                                        ],
                                        # width=340,
                                        height=100,
                                        # spacing = 15,
                                        
                                        alignment= ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment= ft.CrossAxisAlignment.START,
                                        ),
                                        # ft.VerticalDivider(width=340),
                                        ft.Text(value=f"R${item.preco}",size=20,color=ft.colors.BLACK),

                                        
                                        
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                        
                                        
                                    )
                                ),
                            style=ft.ButtonStyle(
                                shape= ft.RoundedRectangleBorder(radius=12),
                                bgcolor= '#ffffff',
                                overlay_color='#ffffff',
                                ),
                                expand = True,
                            
                        ),
                        ft.ElevatedButton(
                            content=ft.Icon(name = ft.icons.ADD_SHOPPING_CART,color = '#ff312f',size=50,),
                            width=100,
                            height=100,
                            style=ft.ButtonStyle(
                                shape= ft.RoundedRectangleBorder(radius=12),
                                bgcolor= '#ffffff',
                                #  shadow_color = '#ffffff',
                                overlay_color='#ffffff',
                                #  shadow_color='#ffffff'
                                ),
                                # expand = True,
                            on_click= lambda e: add_carrinho(item, estabelecimento)
                                            
                        ),

                    ],
                        
                    alignment=ft.MainAxisAlignment.START
                ),
                
            )

    vetor_itens = [create_product_row(item) for item in tabela]

    
    if tabela == []:
        vetor_itens = [ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src='images/NÃO EXCLUIR.png',
                                height=500,
                                width=500,
                            ),
                            ft.Text(value=f"O cardápio está vazio!",size=25,color=ft.colors.GREY_600)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,  # Alinha o container ao centro da página
                    padding=20
                )
        ]
        
        
        

    coluna_itens = ft.Column(
            controls=vetor_itens,
            scroll=ft.ScrollMode.HIDDEN
            
            
           
        )


    itens = ft.Container(
            content=coluna_itens,
            bgcolor='#ffffff',
            expand=True
            
        )

# RODAPÉ ########################################################################### 

    rodape = ft.Container(
        content=
                ft.Row(
                    controls= [
                        ft.IconButton(
                        icon = ft.icons.HOME_OUTLINED,
                        selected_icon = ft.icons.HOME,
                        selected_icon_color=ft.colors.BLACK,
                        icon_color = ft.colors.GREY,
                        selected=True,                
                        icon_size=30,
                        on_click= lambda e: page.go('/inicio')
                        ),
                        ft.IconButton(
                        icon = ft.icons.FEED_OUTLINED,
                        # label='Pedidos',
                        selected_icon = ft.icons.FEED_ROUNDED,
                        selected_icon_color=ft.colors.BLACK,
                        icon_color = ft.colors.GREY,
                        # selected=False
                        icon_size=30,
                        on_click= lambda e: page.go('/pedidos')
                        ),
                        ft.IconButton(
                        icon = ft.icons.PERSON_OUTLINED,
                        # label='Perfil',
                        selected_icon = ft.icons.PERSON,
                        icon_color = ft.colors.GREY,
                        selected_icon_color=ft.colors.BLACK,
                        selected=False,
                        icon_size=30,
                        on_click= lambda e: page.go('/cliente')
                        ),
                    ],
                        alignment = ft.MainAxisAlignment.SPACE_AROUND,
                    # vertical_alignment=ft.CrossAxisAlignment.END,
                    # expand=True
                ),
        border=ft.Border(
            top=ft.BorderSide(0.85, ft.colors.GREY)
        )

    ) 
    

    cont_rodape = ft.Container(
        content=rodape,
        # border=ft.border.all (1, ft.colors.BLACK),
        border_radius=5,

    )

# LOGO CABEÇALHO ########################################################################### 

    row2 = ft.Row(
    controls= [
        ft.Image(
            src='images/SVG LOGO UFMG.svg',
            height=150,
            width=150,
        ),
    ],
    alignment = ft.MainAxisAlignment.CENTER,
    vertical_alignment=ft.CrossAxisAlignment.START,
)
    

# CHAMA CRIAÇÕES ########################################################################### 
    return ft. Container(
          ft.Column(
                controls=[
                        row2,
                        back,
                        welcome,
                        itens,
                        btn_car,
                        cont_rodape
                        ]
          ),
        bgcolor= '#ffffff',

        
        height=975,
        width=760,
        padding=10,
        expand=True
    )