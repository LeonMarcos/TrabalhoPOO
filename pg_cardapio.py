from decimal import Decimal
from cgitb import text
import glob
from itertools import product
from multiprocessing import Value
import time
from tkinter import Scrollbar
from tkinter.tix import DisplayStyle, Tree
from turtle import bgcolor, color, title
from typing import Text
from annotated_types import T
import flet as ft
import pyodbc
from Conex_SQL import connection
from Estabelecimento import Estabelecimento
from Carrinho import Carrinho
from Pedido import Pedido
from types import SimpleNamespace
import pg_aux
import datetime
import pg_login


estabelecimento_teste = Estabelecimento()

cursor = connection.cursor()

lixeira = []
nome_provisorio = None
id_provisorio = None

item_provisorio = None
descricao_provisoria = None
preco_provisorio = None


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

lista_carrinho = []


nome_cadastro = ft.TextField(
        label='Nome',
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.OUTLINE,
        border_radius=ft.border_radius.all(7),
        border_width=2,
        border_color=ft.colors.GREY_700,
        prefix_icon=ft.icons.FASTFOOD,
        color=ft.colors.BLACK,
        cursor_color=ft.colors.BLACK,
        cursor_width=1,
        hint_text='Nome do item',
        hint_style=ft.TextStyle(color=ft.colors.GREY),
        value=None,
        # input_filter=ft.TextOnlyInputFilter(),
        error_text = None,
        error_style = None
)
descricao_cadastro = ft.TextField(
        label='Descrição',
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.OUTLINE,
        border_radius=ft.border_radius.all(7),
        border_width=2,
        border_color=ft.colors.GREY_700,
        prefix_icon= ft.icons.INFO_OUTLINE,
        color=ft.colors.BLACK,
        cursor_color=ft.colors.BLACK,
        hint_text='Breve descrição do seu item',
        hint_style=ft.TextStyle(color=ft.colors.GREY),
        value=None,
        cursor_width=1,
        error_text = None,
        error_style = None
)
preco_cadastro = ft.TextField(
        label='Preço',
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.OUTLINE,
        border_radius=ft.border_radius.all(7),
        border_width=2,
        border_color=ft.colors.GREY_700,
        prefix_text='R$ ',
        prefix_style=ft.TextStyle(color=ft.colors.BLACK,size=17),
        prefix_icon=ft.icons.ATTACH_MONEY,
        color=ft.colors.BLACK,
        cursor_color=ft.colors.BLACK,
        hint_text='00.00',
        hint_style=ft.TextStyle(color=ft.colors.GREY),
        value=None,
        cursor_width=1,
        input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9.]"
        ),
        
        error_text=None,
        error_style=None,
)  



def page_cardapio_estab(page: ft.Page):
    
    

    estabelecimento_teste = pg_login.retorna_dados_usuario()

    
    
    cardapio(estabelecimento_teste.get_id())

    page.bgcolor = '#ffffff'
    page.window_title_bar_hidden = False
    page.window_resizable = True
    page.window_width = 725
    # page.window_height = 1047
    page.window_height = 760
    page.window_max_width = 725
          
#
            

    

# MENSAGEM INICIAL ########################################################################### 
    
    def nome_estabeleciment():
        
         return ft.Container(
              ft. Row(
              controls=[
                   ft.Text(
                        value=f"| Cardápio - {estabelecimento_teste.get_nome()}",
                        color=ft.colors.BLACK,
                        size=25,
                    ),
                    ft.ElevatedButton(
                        content=ft.Container(
                            content = ft.Row(
                                    controls = [
                                            ft.Icon(
                                                name=ft.icons.ADD,
                                                color='#ffffff',
                                                size=17
                                                ),

                                            ft.Text(
                                                "Adicionar Item",
                                                text_align=ft.TextAlign.START,
                                                color='#ffffff',
                                                size=17)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                            )
                        ),
                        bgcolor='#ff312f',
                        width=200,
                        height=40,
                        on_click= lambda e: open_cadastro(e)
                    )
         ],
         alignment=ft.MainAxisAlignment.SPACE_BETWEEN
         
         )
         )
         
    nome = [nome_estabeleciment()]    

    welcome = ft.Column(
          controls=nome,
          alignment=ft.CrossAxisAlignment.CENTER,
          width=710,
          )
    
    msg_add = ft.Row(controls=[
        ft.Icon(name=ft.icons.FASTFOOD_ROUNDED,color='#ffffff'),
        ft.Text(
                value="Item cadastrado no cardápio!",
                color='#ffffff',
                size=20),
        
    ])

    item_add = ft.SnackBar(
                    content=msg_add,
                    bgcolor='#0f6e72',
                    duration=2000
                    )
    def msg_item():
        time.sleep(0.1)
        page.show_snack_bar(item_add)
        page.update()

             
    
    def cadastro_item(page,nome,descricao,preco):
        cardapio(estabelecimento_teste.get_id())
        ok = True

        if len(nome) >= 3 or len(nome) <= 20:
            nome_cadastro.error_text = None
            nome_cadastro.error_style = None
        
        if len(descricao) >= 3 or len(descricao) <= 50:
            descricao_cadastro.error_text = None
            descricao_cadastro.error_style = None
        
        if preco_cadastro.value != '':
            preco = float(preco)
            if preco > 0:
                preco_cadastro.error_text = None
                preco_cadastro.error_style = None
        


        for busca in tabela:
            if busca.nome == nome:
                    if nome == item_provisorio: 
                        ok = True
                    if nome != item_provisorio:
                        ok = False
                        nome_cadastro.error_text = 'Item existente no seu cardápio!'
                        nome_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)
                        page.update()

        if len(nome) < 3 or len(nome) > 20:
            ok = False
            nome_cadastro.error_text = 'Nome deve conter entre 3-20 caracteres'
            nome_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)
        
        if len(descricao) < 3 or len(descricao) > 50:
            ok = False
            descricao_cadastro.error_text = 'Descrição deve conter entre 3-50 caracteres'
            descricao_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)
        
        if preco_cadastro.value == '':
            ok = False
            preco_cadastro.error_text = 'O preço deve ser maior que 0'
            preco_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)
            print('deu erro')
        
        if preco_cadastro.value != '':
             if preco  <= 0 :
                ok = False
                preco_cadastro.error_text = 'O preço deve ser maior que 0'
                preco_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)
                 
        if ok == True:
            entradas = [nome_cadastro, descricao_cadastro, preco_cadastro]
            for entrada in entradas:
                 entrada.error_text = None
                 entrada.error_style = None

            estabelecimento_teste.cadastrar_item(estabelecimento_teste.get_id(), nome, descricao, preco)
            
            page.dialog.open = False
            page.go('/atualizar')
            page.update()
            time.sleep(0.01)
            page.go('/cardapio_estab')
            page.update()
            msg_item()

        page.update()
                    
    
    def alterar_item(page,nome,descricao,preco,id):
        cardapio(estabelecimento_teste.get_id())
        ok = True

        if len(nome) >= 3 or len(nome) <= 20:
            nome_cadastro.error_text = None
            nome_cadastro.error_style = None
        
        if len(descricao) >= 3 or len(descricao) <= 50:
            descricao_cadastro.error_text = None
            descricao_cadastro.error_style = None
        
        if preco_cadastro.value != '':
            preco = float(preco)
            if preco > 0:
                preco_cadastro.error_text = None
                preco_cadastro.error_style = None
        


        for busca in tabela:
            if busca.nome == nome:
                    if nome == item_provisorio: 
                        ok = True
                    if nome != item_provisorio:
                        ok = False
                        nome_cadastro.error_text = 'Item existente no seu cardápio!'
                        nome_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)
                        page.update()

        if len(nome) < 3 or len(nome) > 20:
            ok = False
            nome_cadastro.error_text = 'Nome deve conter entre 3-20 caracteres'
            nome_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)
        
        if len(descricao) < 3 or len(descricao) > 50:
            ok = False
            descricao_cadastro.error_text = 'Descrição deve conter entre 3-50 caracteres'
            descricao_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)
        
        if preco_cadastro.value == '':
            ok = False
            preco_cadastro.error_text = 'O preço deve ser maior que 0'
            preco_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)
            print('deu erro')
        
        if preco_cadastro.value != '':
             preco = float(preco)
             if preco  <= 0 :
                ok = False
                preco_cadastro.error_text = 'O preço deve ser maior que 0'
                preco_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)
             

        if ok == True:
            entradas = [nome_cadastro, descricao_cadastro, preco_cadastro]
            for entrada in entradas:
                 entrada.error_text = None
                 entrada.error_style = None

            estabelecimento_teste.alterar_item(nome,descricao,preco,id)
            page.dialog.open = False
            page.go('/atualizar')
            page.update()
            time.sleep(0.01)
            page.go('/cardapio_estab')
            page.update()
            time.sleep(0.1)
            msg_item()

        page.update()
     

    def confirma_remover(page, item):
        
        def close_aviso(e):
            aviso_remover.open = False
            aviso_remover.update()
            page.update()

        aviso_remover = ft.BottomSheet(
            ft.Container(
                ft.Column(
                    controls=[
                        ft.Divider(height=10,color=ft.colors.TRANSPARENT),
                        ft.Text(value=f"Deseja excluir {item.nome} do seu cardápio?",
                                size=20,
                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.BOLD,                            
                                color=ft.colors.BLACK,),
                        ft.Text(value='Esta ação é irreversível',
                                size=20,
                                color=ft.colors.GREY_800),
                        ft.ElevatedButton(content=ft.Text(value='Excluir',size=20),
                                        bgcolor='#ff312f',
                                        color='#ffffff',
                                        width=400,
                                        style=ft.ButtonStyle(
                                            shape= ft.RoundedRectangleBorder(radius=5)
                                            ),
                                        on_click= lambda e: remover_item(page, item.item_id)
                                        ),
                        ft.TextButton(content=ft.Text(value='Voltar',size=20),
                                        style=ft.ButtonStyle(color='#ff312f'),
                                        width=400,
                                        on_click= close_aviso
                                        ),
                        
                        
                    ],
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER
                ),
                height=220,
                width=700,
            ),
            open=True,
            bgcolor='#ffffff',
        )

        page.overlay.append(aviso_remover)

        page.update()
        

        msg_excluir = ft.Row(controls=[
            ft.Icon(name=ft.icons.FASTFOOD_ROUNDED,color='#ffffff'),
            ft.Text(
                    value="Item excluído do seu cardápio!",
                    color='#ffffff',
                    size=20),
            
        ])

        item_excluido = ft.SnackBar(
                        content=msg_excluir,
                        bgcolor='#fa3839',
                        duration=2000
                        )
        
        def aviso_excluido():
            time.sleep(0.1)
            page.show_snack_bar(item_excluido)
            page.update()


            
        def remover_item(page, id):

            estabelecimento_teste.remover_item(id)
            
            aviso_remover.open = False
            page.go('/atualizar')
            page.update()
            time.sleep(0.01)
            page.go('/cardapio_estab')
            page.update()
            aviso_excluido()
            
                 

# CADASTRAR ITEM ###########################################################################
    
    def open_cadastro(e):
        global item_provisorio, descricao_provisoria, preco_provisorio
        item_provisorio = None
        descricao_provisoria = None
        preco_provisorio = None
        nome_cadastro.value = None
        descricao_cadastro.value = None
        preco_cadastro.value = None
        page.dialog = dialog_cadastro
        dialog_cadastro.open = True
        entradas = [nome_cadastro, descricao_cadastro, preco_cadastro]
        for entrada in entradas:
                entrada.error_text = None
                entrada.error_style = None
        page.update()

    # Função para fechar o diálogo
    def close_cadastro(e):
        dialog_cadastro.open = False
        page.update()


    dialog_cadastro = ft.AlertDialog (

        title=ft.Text("CADASTRAR ITEM",color=ft.colors.BLACK),
        content=
            ft.Container(
                ft.Column(
                            [
                            nome_cadastro,
                            descricao_cadastro,
                            preco_cadastro,
                            ],
                            spacing=20
                        ),
            width=400,
            height=400,
            ),
        actions=[
            ft.TextButton(  "Cancelar",
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#ff312f'),
                            on_click=close_cadastro),
            ft.TextButton(  "Confirmar",
                            # bgcolor = '#ff312f',
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#036666'),
                            on_click=lambda e: cadastro_item(page,nome_cadastro.value,descricao_cadastro.value,preco_cadastro.value)
                            ),
        ],
        bgcolor='#ffffff',
    )

# ALTERAR ITEM ###########################################################################
    
    def open_edit(e,item):
        print('ITEM AQUI',item)
        global item_provisorio, descricao_provisoria, preco_provisorio, id_provisorio
        item_provisorio = item.nome
        descricao_provisoria = item.descricao
        preco_provisorio = item.preco
        id_provisorio = item.item_id
        nome_cadastro.value = item_provisorio
        descricao_cadastro.value = descricao_provisoria
        preco_cadastro.value = preco_provisorio
        page.dialog = dialog_edit
        print(item_provisorio)
        dialog_edit.open = True
        entradas = [nome_cadastro, descricao_cadastro, preco_cadastro]
        for entrada in entradas:
                entrada.error_text = None
                entrada.error_style = None
        page.update()

    # Função para fechar o diálogo
    def close_edit(e):
        dialog_edit.open = False
        page.update()

    dialog_edit = ft.AlertDialog (

        title=ft.Text("ALTERAR ITEM",color=ft.colors.BLACK),
        content=
            ft.Container(
                ft.Column(
                            [
                            nome_cadastro,
                            descricao_cadastro,
                            preco_cadastro,
                            ],
                            spacing=20
                        ),
            width=400,
            height=400,
            ),
        actions=[
            ft.TextButton(  "Cancelar",
                            # bgcolor = '#ff312f',
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#ff312f'),
                            on_click=close_edit),
            ft.TextButton(  "Confirmar",
                            # bgcolor = '#ff312f',
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#036666'),
                            on_click=lambda e: alterar_item(page,nome_cadastro.value,descricao_cadastro.value,preco_cadastro.value,id_provisorio)
                            ),
        ],
        bgcolor='#ffffff',
    )


    
# CARDÁPIO ###########################################################################
    
    def create_product_row(item):
            cardapio(estabelecimento_teste.get_id())
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
                        content=ft.Icon(name = ft.icons.DRIVE_FILE_RENAME_OUTLINE_SHARP,color = '#ff312f',size=35,),
                        width=75,
                        height=100,
                        style=ft.ButtonStyle(
                             shape= ft.RoundedRectangleBorder(radius=12),
                             bgcolor= '#ffffff',
                             overlay_color='#ffffff',
                            ),
                        on_click= lambda e: open_edit(e,item)
                                        
                    ),
                    ft.ElevatedButton(
                        content=ft.Icon(name = ft.icons.DELETE,color = '#ff312f',size=35,),
                        width=75,
                        height=100,
                        style=ft.ButtonStyle(
                             shape= ft.RoundedRectangleBorder(radius=12),
                             bgcolor= '#ffffff',
                            #  shadow_color = '#ffffff',
                             overlay_color='#ffffff',
                            #  shadow_color='#ffffff'
                            ),
                            # expand = True,
                        on_click= lambda e: confirma_remover(page, item)
                                        
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
                            ft.Text(value=f"Você ainda não cadastrou itens no cardápio!",size=25,color=ft.colors.GREY_600)
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
                        icon = ft.icons.BOOKMARK_ADD_OUTLINED,
                        selected_icon = ft.icons.BOOKMARK_ADD,
                        icon_color = ft.colors.GREY,
                        selected_icon_color=ft.colors.BLACK,
                        selected=False,
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
                        selected=True,
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
    return ft. Container(
          ft.Column(
                controls=[
                        row2,
                        welcome,
                        itens,
                        cont_rodape
                        ]
          ),
        bgcolor= '#ffffff',

        
        height=975,
        width=760,
        padding=10,
        expand=True
    )