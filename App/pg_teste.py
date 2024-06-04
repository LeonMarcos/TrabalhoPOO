from cgitb import text
from itertools import product
from multiprocessing import Value
from tkinter import Scrollbar
from tkinter.tix import DisplayStyle
from turtle import bgcolor, color
from typing import Text
from annotated_types import T
import flet as ft
import pyodbc
from Cliente import Cliente
from Conex_SQL import connection
from Estabelecimento import Estabelecimento
from Carrinho import Carrinho
from Pedido import Pedido



cursor = connection.cursor()

consulta = """ SELECT * FROM Usuarios
                    WHERE tipo = 'Estabelecimento';
        """ #consulta o banco de dados
cursor.execute(consulta) 
tabela = cursor.fetchall()


def main(page: ft.Page):
    page.bgcolor = '#e3dac9'


# MENSAGEM INICIAL ########################################################################### 
    
    welcome = ft.Text(
            value=f'| Olá, Usuário!',
            color=ft.colors.BLACK,
            size=25,
        )
    

    # def get_nome(usuario):
    #     usuario = usuario,
    #     return usuario




# LISTA DE ESTABELECIMENTOS ###########################################################################

    def create_product_row(estabelecimento):
            return ft.Container(
                ft.Row(
                controls=[
                    ft.ElevatedButton(estabelecimento.nome,width=400, height = 75),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND
            ),
            
        )

    vetor_estabelecimentos = [create_product_row(estabelecimento) for estabelecimento in tabela]
    


    coluna_estabelecimentos = ft.Column(
            controls=vetor_estabelecimentos,
            scroll=ft.ScrollMode.HIDDEN
            
            
           
        )


    estabelecimentos = ft.Container(
            content=coluna_estabelecimentos,
            bgcolor=ft.colors.RED,
            expand=True
            
        )

# RODAPÉ ########################################################################### 

    rodape = ft.NavigationBar(
    destinations= [
        ft.NavigationDestination(
            icon = ft.icons.HOME_OUTLINED,
            label='Início',
            # icon_content=ft.Container(bgcolor=ft.colors.GREY),
            selected_icon = ft.icons.HOME,
            
            # selected_icon_color=ft.colors.BLACK,
            # icon_color = ft.colors.GREY,
            # selected=True
            ),
            ft.NavigationDestination(
            icon = ft.icons.SEARCH,
            label='Busca',
            selected_icon = ft.icons.SEARCH,
            # icon_color = ft.colors.GREY,
            # selected_icon_color=ft.colors.BLACK,
            # icon = ft.icons.COLOR_LENS
            # selected=False
            ),
            ft.NavigationDestination(
            icon = ft.icons.LIST_ALT_OUTLINED,
            label='Pedidos',
            selected_icon = ft.icons.LIST_ALT_OUTLINED,
            # selected_icon_color=ft.colors.BLACK,
            # icon_color = ft.colors.GREY,
            # selected=False
            ),
            ft.NavigationDestination(
            icon = ft.icons.PERSON_OUTLINED,
            label='Perfil',
            selected_icon = ft.icons.PERSON,
            # icon_color = ft.colors.GREY,
            # selected_icon_color=ft.colors.BLACK,
            # selected=False
            # on_click = ,
            ),
    ],
    # alignment = ft.MainAxisAlignment.SPACE_AROUND,
    # vertical_alignment=ft.CrossAxisAlignment.END,
    selected_index=0,
    bgcolor='#e3dac9',
    expand=True
        
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
            src='images/logo_UFMGFood_png.png',
            height=200,
            width=200,
        ),
    ],
    alignment = ft.MainAxisAlignment.CENTER,
    vertical_alignment=ft.CrossAxisAlignment.START,
)

# CHAMA CRIAÇÕES ########################################################################### 

    page.add(row2,welcome,estabelecimentos,cont_rodape)
    page.update()




ft.app(target=main, assets_dir='assets') 