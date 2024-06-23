from cgitb import text
from decimal import Decimal
from itertools import product
from multiprocessing import Value
from tkinter import Scrollbar
from tkinter.tix import DisplayStyle
from turtle import bgcolor, color
from typing import Text
from annotated_types import T
from arrow import get
import flet as ft
import pyodbc
from Conex_SQL import connection
from types import SimpleNamespace
# from pg_usuario import page_usuario
import pg_login
import time
from Pedido import Pedido
from Estabelecimento import Estabelecimento

estabelecimento_teste = Estabelecimento()

pedido_aux = Pedido()


cursor = connection.cursor()
tabela = []
# BUSCA SOMENTE OS PEDIDOS DO USUARIO LOGADO
def pedidos_usuario(id):
    consulta = """ SELECT DISTINCT id, status_pedido, nome_cliente, data_horario_pedido
                                    FROM Pedidos
                                    WHERE loja_id = ? AND status_pedido = 'Pendente' 
            """ #consulta o banco de dados
    cursor.execute(consulta,id) 
    aux = cursor.fetchall()
    tabela.clear()
    for p in aux:
         tabela.append(p)

dados_estab = []
# BUSCA OS DADOS DO USUARIO
def busca_estab(id):
    busca_estabelecimento = """ SELECT * FROM Usuarios
                    WHERE id = ?;
        """ #consulta o banco de dados
    cursor.execute(busca_estabelecimento,id) 
    aux= cursor.fetchall()
    dados_estab.clear()
    for p in aux:
        dados_estab.append(p)


#BUSCA OS ITENS E TODAS AS INFORMAÇÕES DOS PEDIDOS

itens_pedido = []

def buscar_pedido(pedido):

    busca = """ SELECT * FROM Pedidos
                    WHERE id = ?
            """ #consulta o banco de dados
    cursor.execute(busca,pedido.id) 
    aux = cursor.fetchall()
    itens_pedido.clear()
    for p in aux:
         itens_pedido.append(p)


#BUSCA QUE UNIFICA OS DADOS DO PEDIDO, PARA NÃO IMPRIMIR VÁRIAS VEZES
info = []
def titulo(pedido):
    informacoes = """ SELECT DISTINCT id, status_pedido, nome_cliente, data_horario_pedido
                                    FROM Pedidos
                                    WHERE id = ?
            """ #consulta o banco de dados
    cursor.execute(informacoes,pedido.id) 
    aux = cursor.fetchall()
    info.clear()
    for p in aux:
         info.append(p)
    




def page_pendentes(page: ft.Page):
    estabelecimento_teste = pg_login.retorna_dados_usuario()
    busca_estab(estabelecimento_teste.get_id())
    pedidos_usuario(estabelecimento_teste.get_id())
    
    page.bgcolor = '#ffffff'
    page.window_title_bar_hidden = False
    page.window_resizable = True
    page.window_width = 725
    # page.window_height = 1047
    page.window_height = 760
    page.window_max_width = 725
    
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            thumb_color=ft.colors.GREY
        )
    )
    msg_conf = ft.Row(controls=[
        ft.Icon(name=ft.icons.CHECK_CIRCLE,color='#ffffff'),
        ft.Text(
                value="Pedido confirmado!",
                color='#ffffff',
                size=20),
        
        ])

    pedido_conf = ft.SnackBar(
                    content=msg_conf,
                    bgcolor='#0f6e72',
                    duration=2000
                    )
    
    def aviso_conf():
        page.show_snack_bar(pedido_conf)
        page.update()

    msg_canc = ft.Row(controls=[
        ft.Icon(name=ft.icons.CANCEL,color='#ffffff'),
        ft.Text(
                value="Pedido cancelado!",
                color='#ffffff',
                size=20),
        
        ])

    pedido_canc = ft.SnackBar(
                    content=msg_canc,
                    bgcolor='#fa3839',
                    duration=2000
                    )
    
    def aviso_canc():
        page.show_snack_bar(pedido_canc)
        page.update()

    def confirmar_pedido(id):
        estabelecimento_teste.confirmar_pedido(id)
        pedidos_usuario(estabelecimento_teste.get_id()) # VERIFICAR
        page.dialog.open = False
        page.update()
        page.go('/atualizar')
        page.update()
        time.sleep(0.01)
        page.go('/pendentes')
        page.update()
        time.sleep(0.25)
        aviso_conf()
    
    def cancelar_pedido(id):
        estabelecimento_teste.cancelar_pedido(id)
        page.dialog.open = False
        pedidos_usuario(estabelecimento_teste.get_id())  # VERIFICAR
        page.go('/atualizar')
        page.update()
        time.sleep(0.01)
        page.go('/pendentes')
        page.update()
        time.sleep(0.25)
        aviso_canc()



# MENSAGEM INICIAL ########################################################################### 
    
    def nome_estab(estabelecimento):
         return ft.Text(
            value=f"| Novos Pedidos - {estabelecimento.nome}",
            color=ft.colors.BLACK,
            size=25,
         )
         
    nome = [nome_estab(estabelecimento) for estabelecimento in dados_estab]    

    welcome = ft.Column(
          controls=nome
          )

# FUNÇÕES POP-UP ########################################################################### 
   
    def titulo_row(pedido):
            icon = None
            if pedido.status_pedido == 'Concluído':
                 icon = ft.Icon(name=ft.icons.CHECK_CIRCLE,size=30,color='#ff312f')
            if pedido.status_pedido == 'Cancelado':
                 icon = ft.Icon(name=ft.icons.CANCEL,size=30,color='#ff312f')
            if pedido.status_pedido == 'Pendente':
                 icon = ft.Icon(name=ft.icons.PENDING,size=30,color='#ff312f')
            return ft.Container(
                content = ft.Row(controls=
                    [ft.Column(
                            controls=[
                                ft.Row(controls=[
                                    ft.Icon(name=ft.icons.TAG,size=30,color='#ff312f'),
                                    ft.Text(value=f"{pedido.id}",size=22,color=ft.colors.BLACK)
                                    ],
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=0
                                    ),
                                
                            ],
                        ),
                        ft.Column(
                        controls=[
                                ft.Row(controls=[
                                    icon,
                                    ft.Text(value=f"{pedido.status_pedido}",size=22,color=ft.colors.BLACK)
                                    ],
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=5
                                    ),
                                
                        ]
                        ),
                        ft.Column(
                            controls=[

                                ft.Row(controls=[
                                    ft.Icon(name=ft.icons.PERSON,size=30,color='#ff312f'),
                                    ft.Text(value=f"{pedido.nome_cliente}",size=22,color=ft.colors.BLACK)
                                    ],
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=5
                                    ),
                                
                        ],
                        ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                height=40,
                border=ft.Border(
                    bottom=ft.BorderSide(0.85, ft.colors.GREY)
                    
                    ),
                
                )



# LISTA DE ITENS

    def itens_row(pedido):
             
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
                                        ft.Text(value=pedido.nome_item,size=20,color=ft.colors.BLACK),
                                        ft.Text(value=f"R${pedido.preco} x {pedido.quant_item}",size=15,color=ft.colors.GREY_700),
                                        
                                    ],
                                    width=250,
                                    height=100,
                                    # spacing = 15,
                                    
                                    alignment= ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment= ft.CrossAxisAlignment.START,
                                    ),
                                    ft.Text(value=f"R${pedido.subtotal}",size=20,color=ft.colors.BLACK),
                                    ],
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


# POP-UP PEDIDO ###########################################################################    

    def open_pedido(page, pedido):
        buscar_pedido(pedido)
        
        # INÍCIO ###################

        titulo(pedido)

        tit = [titulo_row(pedido) for pedido in info]

        # CONTEÚDO LISTA ###################

        itens = [itens_row(pedido) for pedido in itens_pedido]

        col = ft.Container(
                content=ft.Column(
                controls=itens,
                scroll=ft.ScrollMode.AUTO
                ),
                height=350,
                
            )
        
        
        total = Decimal(0)
        for p in itens_pedido:
            total += p.subtotal
            endereco = p.endereco

        # CAMPOS INFERIORES ###################

        info_final = ft.Container(
                content = ft.Column(
                        controls=[
                                ft.Divider(height=5,color=ft.colors.TRANSPARENT),
                                ft.Row(controls = [
                                        ft.Icon(name=ft.icons.CALCULATE_OUTLINED,size=30,color='#ff312f'),
                                        ft.Text(value=f" Valor total: ",size=20,color=ft.colors.BLACK),
                                        ft.Text(value=f"R$ {total}",size=20,color='#ff312f',style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
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
                                        ft.Icon(name=ft.icons.CALENDAR_MONTH_OUTLINED,size=30,color='#ff312f'),
                                        ft.Text(value=f" {pedido.data_horario_pedido}",size=20,color=ft.colors.BLACK)
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

        
        def close_pop(e):
            page.dialog.open = False
            page.go('/atualizar')
            page.update()
            time.sleep(0.01)
            page.go('/pendentes')
            page.update()

        

        dialog_pedido = ft.AlertDialog (
        
        title=ft.Column(controls=tit),
        content=
            ft.Container(content=
                ft.Column(
                            [
                            col ,
                            info_final
                            ],
                        # scroll=ft.ScrollMode.AUTO   
                        ),
            width=500,
            height=500,
            ),

        actions=[
            ft.TextButton(  "Voltar",
                            # bgcolor = '#ff312f',
                            style=ft.ButtonStyle(color= '#ff312f',bgcolor=ft.colors.TRANSPARENT),
                             on_click=close_pop),
            ft.TextButton(  "Cancelar",
                            # bgcolor = '#ff312f',
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#ff312f'),
                             on_click= lambda e: cancelar_pedido(pedido.id)),
            ft.TextButton(  "Confirmar",
                            # bgcolor = '#ff312f',
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#036666'),
                            on_click=lambda e: confirmar_pedido(pedido.id)),
        ],
        bgcolor='#ffffff',
    )
        page.dialog = dialog_pedido
        dialog_pedido.open = True
        page.update()
    

# LISTA DE PEDIDOS ###########################################################################

    def pedidos_row(pedido):
            
            # pedido1 = pedido
            data_formatada = pedido.data_horario_pedido[:10]
            return ft.Container(
                ft.Row(
                controls=[
                    ft.ElevatedButton(
                        content=ft.Icon(name=ft.icons.FEED_OUTLINED,size=50,color='#ff312f'),
                        width=100,
                        height=100,
                        style=ft.ButtonStyle(
                             shape= ft.RoundedRectangleBorder(radius=12),
                             bgcolor='#ffffff'
                            )
                        ),
                    ft.ElevatedButton(
                        content=ft.Container(
                            content=ft.Row(
                                controls=[ft.Column(
                                    [
                                        ft.Text(value=f"#{pedido.id} - {pedido.status_pedido}",size=20,color=ft.colors.BLACK),
                                        ft.Text(value=pedido.nome_cliente,size=15,color=ft.colors.GREY_700)
                                        
                                    ],
                                    width=400,
                                    height=100,
                                    
                                    # spacing = 15,
                                    
                                    alignment= ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment= ft.CrossAxisAlignment.START,
                                    ),
                                    ft.Text(value=data_formatada,size=20,color=ft.colors.BLACK),
                                    ],
                                )
                            ),
                        style=ft.ButtonStyle(
                             shape= ft.RoundedRectangleBorder(radius=12),
                             bgcolor='#ffffff',
                            ),
                        expand = True,
                        on_click= lambda _: open_pedido(page, pedido) #################################################
                        
                    ),
                ], 
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            
        )

    vetor_pedidos = [pedidos_row(pedido) for pedido in reversed(tabela)]
    
    if tabela == []:
        vetor_pedidos = [ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src='images/NÃO EXCLUIR.png',
                                height=500,
                                width=500,
                            ),
                            ft.Text(value=f"Você ainda não tem novos pedidos!",size=25,color=ft.colors.GREY_600)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,  # Alinha o container ao centro da página
                    padding=20
                )
        ]

    coluna_pedidos = ft.Column(
            controls=vetor_pedidos,
            scroll=ft.ScrollMode.HIDDEN           
           
        )


    pedidos = ft.Container(
            content=coluna_pedidos,
            bgcolor='#ffffff',
            expand=True
            
        )

# RODAPÉ ########################################################################### 

    rodape = ft.Container(
          content= ft.Row(
            controls= [
                ft.IconButton(
                icon = ft.icons.BOOKMARK_ADD_OUTLINED,
                selected_icon = ft.icons.BOOKMARK_ADD,
                icon_color = ft.colors.GREY,
                selected_icon_color=ft.colors.BLACK,
                selected=True,
                icon_size=30,
                on_click= lambda e: page.go('/pendentes')
                ),
                ft.IconButton(
                icon = ft.icons.BOOKMARK_ADDED_OUTLINED,
                selected_icon = ft.icons.BOOKMARK_ADDED,
                selected_icon_color=ft.colors.BLACK,
                icon_color = ft.colors.GREY,
                selected=False,
                icon_size=30,
                on_click= lambda e: page.go('/finalizados')
                ),
                ft.IconButton(
                icon = ft.icons.MENU_BOOK,
                selected_icon = ft.icons.MENU_BOOK,
                icon_color = ft.colors.GREY,
                selected_icon_color=ft.colors.BLACK,
                # icon = ft.icons.COLOR_LENS
                selected=False,
                icon_size=30,
                on_click= lambda e: page.go('/cardapio_estab')
                ),
                ft.IconButton(
                icon = ft.icons.PERSON_OUTLINED,
                selected_icon = ft.icons.PERSON,
                icon_color = ft.colors.GREY,
                selected_icon_color=ft.colors.BLACK,
                selected=False,
                icon_size=30,
                on_click= lambda e: page.go('/estabelecimento'),
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
    return ft.Container(
        content= ft.Column(
                    controls= [
                            row2,
                            welcome,
                            pedidos,
                            cont_rodape
                            ],
                                
                                
                ),
                height=975,
                width=760,
                bgcolor = '#ffffff',
                padding=10,
                expand=True
    )