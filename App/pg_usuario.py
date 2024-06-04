from cgitb import text
from ctypes import alignment
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
                    WHERE id = 1;
        """ #consulta o banco de dados
cursor.execute(consulta) 
tabela = cursor.fetchall()


def main(page: ft.Page):
    page.bgcolor = '#e3dac9'


# MENSAGEM INICIAL ########################################################################### 
    
    welcome = ft.Text(
            value=f'| GABRIEL ROCHA!',
            color=ft.colors.BLACK,
            size=25,
            # alignment=ft.MainAxisAlignment.CENTER
        )
    

    # def get_nome(usuario):
    #     usuario = usuario,
    #     return usuario




# DADOS ###########################################################################

    def dados_usuario(usuario):
            return ft.Container(
                ft.Column(
                controls=[
                    ft.ElevatedButton(f"Nome: {usuario.nome}",width=400, height = 50),
                    ft.ElevatedButton(f"Endereço: {usuario.endereco}",width=400, height = 50 ),
                    ft.ElevatedButton(usuario.telefone,width=400, height = 50),
                    ft.ElevatedButton(usuario.email,width=400, height = 50 ),
                    ft.ElevatedButton(usuario.cpf_cnpj,width=400, height = 50 ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            # alignment=ft.MainAxisAlignment.CENTER,
            expand = True
        )

    vetor_usuario = [dados_usuario(usuario) for usuario in tabela]


    coluna_dados = ft.Column(
            controls=vetor_usuario,           
        )


    dados = ft.Container(
            content=coluna_dados,
            # alignment=ft.MainAxisAlignment.SPACE_AROUND,
            bgcolor=ft.colors.RED,
            expand=True
            
        )

# RODAPÉ ########################################################################### 

    rodape = ft.Row(
    controls= [
        ft.IconButton(
        icon = ft.icons.HOME_OUTLINED,
        selected_icon = ft.icons.HOME,
        selected_icon_color=ft.colors.BLACK,
        icon_color = ft.colors.GREY,
        selected=False
        ),
        ft.IconButton(
        icon = ft.icons.SEARCH,
        selected_icon = ft.icons.SEARCH,
        icon_color = ft.colors.GREY,
        selected_icon_color=ft.colors.BLACK,
        # icon = ft.icons.COLOR_LENS
        selected=False
        ),
        ft.IconButton(
        icon = ft.icons.LIST_ALT_OUTLINED,
        selected_icon = ft.icons.LIST_ALT_OUTLINED,
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
        # border=ft.border.all (1, ft.colors.BLACK),
        border_radius=5,

    )

# LOGO CABEÇALHO ########################################################################### 

    row2 = ft.Row(
    controls= [
        ft.Image(
            src='images/SVG LOGO UFMG.svg',
            height=200,
            width=200,
        ),
    ],
    alignment = ft.MainAxisAlignment.CENTER,
    vertical_alignment=ft.CrossAxisAlignment.START,
)

# CHAMA CRIAÇÕES ########################################################################### 

    page.add(row2,welcome,dados,cont_rodape)
    page.update()




ft.app(target=main, assets_dir='assets') 