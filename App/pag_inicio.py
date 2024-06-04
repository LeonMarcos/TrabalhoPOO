from itertools import product
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



def main(page: ft.Page):
    page.bgcolor = '#e3dac9'
    
    welcome = ft.Text(
            value='| Olá, Usuário!',
            color=ft.colors.BLACK,
            size=25,
        )
    

    rodape = ft.Row(
        controls= [
            ft.IconButton(
            icon = ft.icons.HOME_OUTLINED,
            selected_icon = ft.icons.HOME,
            selected_icon_color=ft.colors.BLACK,
            icon_color = ft.colors.GREY,
            selected=True
            ),
            ft.IconButton(
            icon = ft.icons.SEARCH,
            # selected_icon = ft.icons.HOME,
            icon_color = ft.colors.GREY,
            selected_icon_color=ft.colors.BLACK,
            # icon = ft.icons.COLOR_LENS
            selected=False
            ),
            ft.IconButton(
            icon = ft.icons.LIST_ALT_OUTLINED,
            # selected_icon = ft.icons.HOME,
            selected_icon_color=ft.colors.BLACK,
            icon_color = ft.colors.GREY,
            selected=False
            ),
            ft.IconButton(
            icon = ft.icons.PERSON_OUTLINED,
            selected_icon = ft.icons.PERSON,
            icon_color = ft.colors.GREY,
            selected_icon_color=ft.colors.BLACK,
            selected=True
            # on_click = ,
            ),
        ],
        alignment = ft.MainAxisAlignment.SPACE_AROUND,
        vertical_alignment=ft.CrossAxisAlignment.END,
        expand=True
         
    )

    cont_rodape = ft.Container(
        content=rodape,
        border=ft.border.all (1, ft.colors.BLACK),
        border_radius=5,
    )

    lista_estabelecimentos = ft.Row(
        controls=[
            ft.Text(
                value='| TESTE!',
                color=ft.colors.WHITE,
                size=25,
            ),
        ],
        alignment = ft.MainAxisAlignment.SPACE_EVENLY,
    )

    coluna_estabelecimentos = ft.Column(
        controls=[
            lista_estabelecimentos
        
        ],
        
    )

    estabelecimentos = ft.Container(
        content=coluna_estabelecimentos,
        bgcolor=ft.colors.RED,
        expand=True
        
    )

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

    page.add(row2,welcome,estabelecimentos,cont_rodape)
    page.update()
    

    

ft.app(target=main, assets_dir='assets') 