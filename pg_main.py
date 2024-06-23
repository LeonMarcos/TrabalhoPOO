from cgitb import text
from itertools import product
from multiprocessing import Value
from tkinter import LEFT, Scrollbar
from tkinter.tix import DisplayStyle, Tree
from turtle import bgcolor, color, left, onclick
from typing import Text
from annotated_types import T
from multiprocessing import Value

from turtle import bgcolor, color, screensize

import flet as ft
# import pyodbc



# from backup.App.pg_carrinho import page_carrinho
from pg_pedidos import page_pedidos
from pg_usuario_cliente import page_cliente
from pg_usuario_estab import page_estabelecimento
from pg_inicio import page_inicio
from pg_login import page_login
from pg_carrinho import page_cardapio_cliente
from pg_cardapio import page_cardapio_estab
from pg_ped_pend import page_pendentes
from pg_ped_final import page_finalizados
from pg_aux import auxiliar

# import pg_teste

def main(page: ft.Page):
    
    # page.bgcolor = '#ffffff'
    page.padding = 0
    page.window_title_bar_hidden = False
    
    
    page.window_width = 725
    page.window_height = screensize
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            thumb_color=ft.colors.GREY
        ),
        page_transitions=ft.PageTransitionsTheme(ft.PageTransitionTheme.OPEN_UPWARDS,) 
    )
    
    def route_change(route):

        page.views.clear()
        page.views.append(
            ft.View(
                route="/login", controls=[page_login(page,),], padding=0
                
            )
        )

        if page.route == "/atualizar":
            page.views.append(
                ft.View(
                    "/atualizar",
                    [auxiliar(page)],
                    padding=0
                )
            )
        
        if page.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    [page_login(page)],
                    padding=0
                )
            )

        if page.route == "/inicio":
            page.views.append(
                ft.View(
                    "/inicio",
                    [page_inicio(page,),],
                    padding=0
                )
            )

        if page.route == "/pendentes":
            page.views.append(
                ft.View(
                    "/pendentes",
                    [page_pendentes(page,),],
                    padding=0
                )
            )
        
        if page.route == "/finalizados":
            page.views.append(
                ft.View(
                    "/finalizados",
                    [page_finalizados(page,),],
                    padding=0
                )
            )

        if page.route == "/cardapio_cliente":
            page.views.append(
                ft.View(
                    "/cardapio_cliente",
                    [page_cardapio_cliente(page),],
                    padding=0
                )
            )
        
        if page.route == "/cardapio_estab":
            page.views.append(
                ft.View(
                    "/cardapio_estab",
                    [page_cardapio_estab(page),],
                    padding=0
                )
            )

        if page.route == "/pedidos":
            page.views.append(
                ft.View(
                    "/pedidos",
                    [page_pedidos(page),],
                    padding=0
                )
            )


        if page.route == "/cliente":
            page.views.append(
                ft.View(
                    "/cliente",
                    
                    [page_cliente(page,),],
                    padding=0
                   
                )
            )
        
        if page.route == "/estabelecimento":
            page.views.append(
                ft.View(
                    "/estabelecimento",
                    
                    [page_estabelecimento(page,),],
                    padding=0
                   
                )
            )

        page.update()

    page.on_route_change = route_change

    # Define a rota inicial ao iniciar a aplicação
    page.go(page.route)

# Execute a aplicação
ft.app(target=main, assets_dir='assets')