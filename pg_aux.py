###############################
# Página auxiliar somente para conseguir atualizar os dados de alguma das páginas
##############################
import flet as ft

def auxiliar(page: ft.Page):
    page.bgcolor = '#ffffff'
    cont = ft.Container(bgcolor='#ffffff')

    return cont
