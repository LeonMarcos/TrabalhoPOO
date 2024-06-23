from cgitb import text
from itertools import product
from multiprocessing import Value
from tkinter import LEFT, Scrollbar
from tkinter.tix import DisplayStyle, Tree
from turtle import bgcolor, color, left, onclick
from typing import Text
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
import pg_login

cliente_teste = Cliente()



cursor = connection.cursor()

consulta = """ SELECT * FROM Usuarios
                    WHERE tipo = 'Estabelecimento';
        """ #consulta o banco de dados
cursor.execute(consulta) 
aux_1 = cursor.fetchall()
aux_2 = [] #tabela auxiliar para receber os dados do tipo pyodbc.Row
for busca in aux_1:
    aux_2.append(busca)
tabela = [] #converte 
for row in aux_2:
    # Cria um dicionário com os nomes das colunas e valores da linha
    row_dict = {column[0]: value for column, value in zip(cursor.description, row)}
    
    # Cria um SimpleNamespace a partir do dicionário
    row_namespace = SimpleNamespace(**row_dict)
    
    # Adiciona o objeto SimpleNamespace à lista custom_rows
    tabela.append(row_namespace)



dados_usuario = []
def busca_cliente(id):

    procura = """ SELECT * FROM Usuarios
                        WHERE id = ?;
            """ #consulta o banco de dados
    cursor.execute(procura, id) 
    aux = cursor.fetchall()
    dados_usuario.clear()
    for p in aux:
            dados_usuario.append(p)

    print(dados_usuario)


def abrir_cardapio(page):  
          page.go('/cardapio')

nav_estab = None
def salva_estab(estabelecimento):
    global nav_estab
    nav_estab = estabelecimento
def retorna_estab():
    return nav_estab

def page_inicio(page: ft.Page):

    page.bgcolor = '#ffffff'
    page.window_title_bar_hidden = False
    page.window_resizable = True
    page.window_width = 725
    # page.window_height = 1047
    page.window_height = 760
    page.window_max_width = 725

    cliente_teste = pg_login.retorna_dados_usuario()
    busca_cliente(cliente_teste.get_id())


# MENSAGEM INICIAL ########################################################################### 
 
    nome = [ft.Text(
            value=f"| Olá, {cliente_teste.get_nome()}!",
            color=ft.colors.BLACK,
            size=25,
         )
    ]
    welcome = ft.Column(
          controls=nome
          )
    
    def go_cardapio(page, estabelecimento):
        salva_estab(estabelecimento)
        page.go('/cardapio_cliente')
    
# LISTA DE ESTABELECIMENTOS ###########################################################################
    
    def create_product_row(estabelecimento):
            return ft.Container(
                ft.Row(
                controls=[
                    ft.ElevatedButton(
                        content=ft.Icon(name=ft.icons.STOREFRONT,size=50,color='#ff312f'),
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
                            content=ft.Column(
                                [
                                    ft.Text(value=estabelecimento.nome,size=20,color=ft.colors.BLACK,text_align=LEFT),
                                    ft.Text(value=estabelecimento.endereco,size=15,color=ft.colors.GREY_700),
                                ],
                                
                                height=100,
                                alignment= ft.MainAxisAlignment.CENTER,
                                horizontal_alignment= ft.CrossAxisAlignment.START,
                                ),
                                alignment=ft.alignment.center_left
                                
                            ),
                        style=ft.ButtonStyle(
                             shape= ft.RoundedRectangleBorder(radius=12),
                             bgcolor='#ffffff',
                             overlay_color='#ffffff'
                             
                            ),
                        on_click= lambda e: go_cardapio(page,estabelecimento),
                        expand=True
                        
                    ),
                ],
                    
                alignment=ft.MainAxisAlignment.START,
                expand=True
            ),
            
        )

    vetor_estabelecimentos = [create_product_row(estabelecimento) for estabelecimento in tabela]
    


    coluna_estabelecimentos = ft.Column(
            controls=vetor_estabelecimentos,
            scroll=ft.ScrollMode.AUTO
        )
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            thumb_color=ft.colors.GREY,  # Cor do "polegar" da barra de rolagem
        )
    )


    estabelecimentos = ft.Container(
            content=coluna_estabelecimentos,
            bgcolor='#ffffff',
            expand=True,
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
                ),
        border=ft.Border(
            top=ft.BorderSide(0.85, ft.colors.GREY)
        )

    ) 
    

    cont_rodape = ft.Container(
        content=rodape,
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
                            estabelecimentos,
                            cont_rodape
                            ],
                                
                                
                ),
                height=975,
                width=760,
                bgcolor = '#ffffff',
                padding=10,
                expand=True
    )