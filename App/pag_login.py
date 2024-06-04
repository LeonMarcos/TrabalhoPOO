from cgitb import text
from itertools import product
from sre_parse import State
from tkinter import HORIZONTAL
from tkinter.tix import DisplayStyle
from turtle import bgcolor, color
from typing import Text
from annotated_types import T
import flet as ft

def main(page: ft.Page):
    # page.bgcolor = '#000000'
    page.bgcolor = '#ff312f'
    page.window_title_bar_hidden = False
    page.window_max_width = 100
    page.window_resizable = True
    
    btn = ft.Column(
        controls=[
            ft.ElevatedButton(
            text='Login',
            width=400,
            height = 75,
            
            style=ft.ButtonStyle(
                color= '#e3dac9',
                # bgcolor='#ff312f',
                bgcolor = {ft.MaterialState.HOVERED: ft.colors.BLACK, '': '#ff312f'},
                padding={ft.MaterialState.DEFAULT: 20},
                animation_duration=1000
                
                ),
            ),

            ft.ElevatedButton(
            text='Cadastro',
            
            width=400,
            height = 75,

            style=ft.ButtonStyle(
                color= '#e3dac9',
                # bgcolor='#ff312f',
                bgcolor = {ft.MaterialState.HOVERED: ft.colors.BLACK, '': '#ff312f'},
                padding={ft.MaterialState.DEFAULT: 20},
                
                animation_duration=1000
                
                ),
            ),
        ],
        width=800,
        height=500,
        spacing=50,
        alignment = ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    row1 = ft.Row(
            controls= [
                ft.Image(
                    src='images/logo_UFMGFood_png.png',
                    height=300,
                    width=300,
                ),
            ],
        alignment = ft.MainAxisAlignment.CENTER,
        # horizontal_alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment= ft.CrossAxisAlignment.CENTER,
    )

    column = ft.Column(controls=[
        row1,
        btn
    ],
    # alignment=ft.MainAxisAlignment.center
    )

    cont_principal = ft.Container(
        bgcolor= '#e3dac9',
        height=800,
        width=600,
        margin=ft.margin.all(100),
        border_radius = ft.border_radius.all(30),
        content= column
        
            
    )
    
    
    page.add(cont_principal)
    page.update()
    

    

ft.app(target=main, assets_dir='assets') 