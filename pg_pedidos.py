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
from Cliente import Cliente

cliente_teste = Cliente()

pedido_aux = Pedido()


cursor = connection.cursor()
tabela = []
# BUSCA SOMENTE OS PEDIDOS DO USUARIO LOGADO
def pedidos_usuario(id):
    consulta = """ SELECT DISTINCT id, status_pedido, nome_loja, data_horario_pedido, avaliacao
                                    FROM Pedidos
                                    WHERE cliente_id = ?
            """ #consulta o banco de dados
    cursor.execute(consulta,id) 
    aux = cursor.fetchall()
    tabela.clear()
    for p in aux:
         tabela.append(p)
        

dados_cliente = []
# BUSCA OS DADOS DO USUARIO
def busca_usuario(id):
    
    busca_cliente = """ SELECT * FROM Usuarios
                        WHERE id = ?;
            """ #consulta o banco de dados
    cursor.execute(busca_cliente, id) 
    aux = cursor.fetchall()
    dados_cliente.clear()
    for p in aux:
         dados_cliente.append(p)

busca_avaliacao = []
def buscar_avaliacao(id):
    consulta = """ SELECT DISTINCT avaliacao
                                    FROM Pedidos
                                    WHERE id = ?
            """ #consulta o banco de dados
    cursor.execute(consulta,id) 
    aux = cursor.fetchall()
    busca_avaliacao.clear()
    for p in aux:
         busca_avaliacao.append(p)
    


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
    informacoes = """ SELECT DISTINCT id, status_pedido, nome_loja, data_horario_pedido
                                    FROM Pedidos
                                    WHERE id = ?
            """ #consulta o banco de dados
    cursor.execute(informacoes,pedido.id) 
    aux = cursor.fetchall()
    info.clear()
    for p in aux:
         info.append(p)
    




def page_pedidos(page: ft.Page):
    cliente_teste = pg_login.retorna_dados_usuario()

    busca_usuario(cliente_teste.get_id())
    pedidos_usuario(cliente_teste.get_id())
    
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

# MENSAGEM INICIAL ########################################################################### 
    
    nome = [ft.Text(
            value=f"| Seus Pedidos, {cliente_teste.get_nome()}!",
            color=ft.colors.BLACK,
            size=25,
         )]     

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
                                    ft.Icon(name=ft.icons.STOREFRONT,size=30,color='#ff312f'),
                                    ft.Text(value=f"{pedido.nome_loja}",size=22,color=ft.colors.BLACK)
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
        print(pedido.avaliacao)
        buscar_pedido(pedido)
        buscar_avaliacao(pedido.id)
        
        # INÍCIO ###################

        titulo(pedido)

        tit = [titulo_row(pedido) for pedido in info]

        detalhes = ft.Container(
                content=ft.Column(
                controls=tit,
                scroll=ft.ScrollMode.AUTO
                ),    
        )

        # CONTEÚDO LISTA ###################

        itens = [itens_row(pedido) for pedido in itens_pedido]

        col = ft.Container(
                content=ft.Column(
                controls=itens,
                scroll=ft.ScrollMode.AUTO
                ),
                height=325,
                
            )
        
        
        total = Decimal(0)
        for p in itens_pedido:
            total += p.subtotal
            endereco = p.endereco

        
        # CAMPOS INFERIORES ###################

        def avaliar_pedido(nota):
            estrelas = [estrela_1, estrela_2, estrela_3, estrela_4, estrela_5]
            for i, estrela in enumerate(estrelas, start=1):
                estrela.selected = i <= nota
            for p in busca_avaliacao:
                busca_avaliacao.clear()
                p.avaliacao = nota
                busca_avaliacao.append(p)
            page.dialog.update()
            page.update()
            
        msg_limpar = ft.Row(controls=[
        ft.Icon(name=ft.icons.STAR_HALF,color='#ffffff'),
        ft.Text(
                value="Avaliação enviada!",
                color='#ffffff',
                size=20),
        
        ])

        aval_enviada = ft.SnackBar(
                    content=msg_limpar,
                    bgcolor='#fa3839',
                    duration=2000
                    )
        def aviso_ava():
            page.show_snack_bar(aval_enviada)
            page.update()

        def envia_avaliacao(page):
            global nota
            for p in busca_avaliacao:
                nota = p.avaliacao
            cliente_teste.avaliar_pedido(nota, pedido.id)
            pedidos_usuario(cliente_teste.get_id())
            pedido_aux.consulta_avaliacao(pedido.id,busca_avaliacao)
            page.dialog.open = False
            page.go('/atualizar')
            page.update()
            time.sleep(0.01)
            page.go('/pedidos')
            page.update()
            time.sleep(0.25)
            atualiza_avaliacao()
            aviso_ava()
            page.update()
                

        estrela_1 = ft.IconButton(
            icon=ft.icons.STAR_BORDER,
            icon_color= '#ff312f',
            selected_icon=ft.icons.STAR_SHARP,
            selected_icon_color='#ff312f',
            on_click= lambda e: avaliar_pedido(1)
            )
        estrela_2  = ft.IconButton(
            icon=ft.icons.STAR_BORDER,
            icon_color= '#ff312f',
            selected_icon=ft.icons.STAR_SHARP,
            selected_icon_color='#ff312f',
            on_click= lambda e: avaliar_pedido(2)
        )
        estrela_3 = ft.IconButton(
            icon=ft.icons.STAR_BORDER,
            icon_color= '#ff312f',
            selected_icon=ft.icons.STAR_SHARP,
            selected_icon_color='#ff312f',
            on_click= lambda e: avaliar_pedido(3)
        )
        estrela_4 = ft.IconButton(
            icon=ft.icons.STAR_BORDER,
            icon_color= '#ff312f',
            selected_icon=ft.icons.STAR_SHARP,
            selected_icon_color='#ff312f',
            on_click= lambda e: avaliar_pedido(4)
        )
        estrela_5 = ft.IconButton(
            icon=ft.icons.STAR_BORDER,
            icon_color= '#ff312f',
            selected_icon=ft.icons.STAR_SHARP,
            selected_icon_color='#ff312f',
            on_click= lambda e: avaliar_pedido(5)
        )
        btn_envia_avaliacao = ft.ElevatedButton(
             text='Enviar Avaliação',
             color='#ffffff',
             bgcolor='#036666',
             on_click=lambda e: envia_avaliacao(page)
        )    
        
        estrelas = [estrela_1, estrela_2, estrela_3, estrela_4, estrela_5]
       
            
        def atualiza_avaliacao():
            for p in busca_avaliacao:
                if p.avaliacao != None:
                    for estrela in estrelas:
                        estrela.disabled = True
                        btn_envia_avaliacao.visible = False

                        for i, estrela in enumerate(estrelas, start=1):
                            estrela.selected = i <= p.avaliacao
                if pedido.status_pedido != 'Concluído':
                    for estrela in estrelas:
                        estrela.visible = False
                    btn_envia_avaliacao.visible = False
                     
        
        atualiza_avaliacao()
        
        def aval_row(auxiliar):

            # if pedido.avaliacao == None:
                return  ft.Container(
                            content=
                                    ft.Row(controls=[
                                            estrela_1,
                                            estrela_2,
                                            estrela_3,
                                            estrela_4,
                                            estrela_5
                                           
                                        ],
                                    )
                            )

        aval = [aval_row(pedido) for pedido in busca_avaliacao]

        avaliacao = ft.Container(
            content= ft.Column(
                  controls=aval
             )
        )

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
            page.update()
            page.go('/atualizar')
            page.update()
            time.sleep(0.05)
            page.go('/pedidos')

        

        dialog_pedido = ft.AlertDialog (

        content=
            ft.Container(content=
                ft.Column(
                            [
                            detalhes,
                            col ,
                            info_final,
                            avaliacao,
                            ],
                        ),
            width=500,
            height=650,
            ),

        actions=[
            
            ft.TextButton(  "Voltar",
                            # bgcolor = '#ff312f',
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#ff312f'),
                             on_click=close_pop),
            btn_envia_avaliacao
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
                                        ft.Text(value=pedido.nome_loja,size=15,color=ft.colors.GREY_700)
                                        
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
                            ft.Text(value=f"Você ainda não realizou nenhum pedido!",size=25,color=ft.colors.GREY_600)
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
                icon = ft.icons.HOME_OUTLINED,
                selected_icon = ft.icons.HOME,
                selected_icon_color=ft.colors.BLACK,
                icon_color = ft.colors.GREY,
                selected=False,
                icon_size=30,
                on_click= lambda e: page.go('/inicio')
                ),
                ft.IconButton(
                icon = ft.icons.FEED_OUTLINED,
                selected_icon = ft.icons.FEED_ROUNDED,
                icon_color = ft.colors.GREY,
                selected_icon_color=ft.colors.BLACK,
                selected=True,
                icon_size=30,
                on_click= lambda e: page.go('/pedidos')
                ),
                ft.IconButton(
                icon = ft.icons.PERSON_OUTLINED,
                selected_icon = ft.icons.PERSON,
                icon_color = ft.colors.GREY,
                selected_icon_color=ft.colors.BLACK,
                selected=False,
                icon_size=30,
                on_click= lambda e: page.go('/cliente'),
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