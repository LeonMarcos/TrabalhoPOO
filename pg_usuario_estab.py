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
from Conex_SQL import connection
import pg_login
import time
from Estabelecimento import Estabelecimento

estabelecimento_teste = Estabelecimento()


cursor = connection.cursor()

tabela = []
def busca_usuario(id):
    consulta = """ SELECT * FROM Usuarios
                        WHERE id = ?;
            """ #consulta o banco de dados
    cursor.execute(consulta,id) 
    aux = cursor.fetchall()
    tabela.clear()
    for p in aux:
         tabela.append(p)


lista_de_usuarios=[]
def consulta_sql():
    consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados

    cursor.execute(consulta) 
    aux = cursor.fetchall()
    lista_de_usuarios.clear()
    for p in aux:
          lista_de_usuarios.append(p)


msg_alt = ft.Row(controls=[
        ft.Icon(name=ft.icons.CHECK_CIRCLE,color='#ffffff'),
        ft.Text(
                value="Seus dados foram alterados com sucesso!",
                color='#ffffff',
                size=20),
        
    ])

dado_alt = ft.SnackBar(
                content=msg_alt,
                bgcolor='#0f6e72',
                duration=2000
                )
def msg_dados(page):
    time.sleep(0.1)
    page.show_snack_bar(dado_alt)
    page.update()


ok = True

cpf_cnpj_provisorio = None
email_provisorio = None


nome_cadastro = ft.TextField(
        label='Nome',
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.OUTLINE,
        border_radius=ft.border_radius.all(7),
        border_width=2,
        border_color=ft.colors.GREY_700,
        prefix_icon=ft.icons.STOREFRONT,
        color=ft.colors.BLACK,
        cursor_color=ft.colors.BLACK,
        cursor_width=1,
        hint_text='Nome do seu Estabelecimento',
        hint_style=ft.TextStyle(color=ft.colors.GREY),
        # input_filter=ft.TextOnlyInputFilter(),
        error_text = None,
        error_style = None
)

endereco_cadastro = ft.TextField(
        label='Endereço',
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.OUTLINE,
        border_radius=ft.border_radius.all(7),
        border_width=2,
        border_color=ft.colors.GREY_700,
        prefix_icon= ft.icons.HOME,
        color=ft.colors.BLACK,
        cursor_color=ft.colors.BLACK,
        cursor_width=1,
        error_text = None,
        error_style = None
)

cpf_cnpj_cadastro = ft.TextField(
        label='CNPJ',
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.OUTLINE,
        border_radius=ft.border_radius.all(7),
        border_width=2,
        border_color=ft.colors.GREY_700,
        prefix_icon=ft.icons.FINGERPRINT,
        color=ft.colors.BLACK,
        cursor_color=ft.colors.BLACK,
        cursor_width=1,
        hint_text='00.000.000/0000-00',
        hint_style=ft.TextStyle(color=ft.colors.GREY),
        input_filter=ft.NumbersOnlyInputFilter(),
        # value='0001',
        error_text=None,
        error_style=None,

            
)
telefone_cadastro = ft.TextField(
        label='Telefone',
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.OUTLINE,
        border_radius=ft.border_radius.all(7),
        border_width=2,
        border_color=ft.colors.GREY_700,
        prefix_icon=ft.icons.LOCAL_PHONE,
        color=ft.colors.BLACK,
        cursor_color=ft.colors.BLACK,
        hint_text='(00)00000-0000',
        hint_style=ft.TextStyle(color=ft.colors.GREY),
        cursor_width=1,
        input_filter=ft.NumbersOnlyInputFilter(),
        error_text=None,
        error_style=None,
)     
email_cadastro = ft.TextField(
        label='Email',
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.OUTLINE,
        border_radius=ft.border_radius.all(7),
        border_width=2,
        border_color=ft.colors.GREY_700,
        prefix_icon=ft.icons.EMAIL_OUTLINED,
        color=ft.colors.BLACK,
        hint_text='exemplo@gmail.com',
        hint_style=ft.TextStyle(color=ft.colors.GREY),
        cursor_color=ft.colors.BLACK,
        cursor_width=1,
        error_text=None,
        error_style=None,
)   
senha_cadastro = ft.TextField(
        label = 'Senha',
        password=True,can_reveal_password=True,
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.OUTLINE,
        border_radius=ft.border_radius.all(7),
        border_width=2,
        border_color=ft.colors.GREY_700,
        prefix_icon=ft.icons.KEY,
        hint_text='6-20',
        hint_style=ft.TextStyle(color=ft.colors.GREY),
        color=ft.colors.BLACK,
        cursor_color=ft.colors.BLACK,
        cursor_width=1,
        error_text = None,
        error_style = None
)


def page_estabelecimento(page: ft.Page):
    estabelecimento_teste = pg_login.retorna_dados_usuario()
    busca_usuario(estabelecimento_teste.get_id())
    
    page.bgcolor = '#ffffff'
    page.window_title_bar_hidden = False
    page.window_resizable = True
    page.window_width = 725
    # page.window_height = 1047
    page.window_height = 760
    page.window_max_width = 725
    
    page.theme = ft.Theme(
         color_scheme=ft.ColorScheme(
                                    on_surface_variant='#ff3230',
                                    error='#ff3230',
                                    on_error='#ff3230',
                                    surface='#ff3230')
    )


# MENSAGEM INICIAL ########################################################################### 

    nome = [ ft.Text(
            value=f"| Seu perfil, {estabelecimento_teste.get_nome()}!",
            color=ft.colors.BLACK,
            size=25,
         )]    

    welcome = ft.Column(
          controls=nome
          )


    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            thumb_color=ft.colors.GREY
        ),
        color_scheme=ft.ColorScheme(
                                    on_surface_variant='#ff3230',
                                    error='#ff3230',
                                    on_error='#ff3230',
                                    surface='#ff3230')
    )

# DADOS ###########################################################################

    def dados_usuario(usuario):
            return ft.Container(
                ft.Column(
                scroll=ft.ScrollMode.AUTO,
                controls=[
                     ft.Divider(height=10,color='#ffffff'),
                     ft.Row(
                          controls=[
                               ft.TextField(
                                    label = 'Nome',
                                    label_style=ft.TextStyle(color=ft.colors.BLACK),
                                    border=ft.InputBorder.OUTLINE,
                                    border_radius=ft.border_radius.all(7),
                                    border_width=2,
                                    border_color=ft.colors.GREY_700,
                                    prefix_icon=ft.icons.STOREFRONT,
                                    color=ft.colors.BLACK,
                                    cursor_color=ft.colors.BLACK,
                                    cursor_width=1,
                                    # hint_text='exemplo@gmail.com',
                                    hint_style = ft.TextStyle(color=ft.colors.GREY),
                                    value = usuario.nome,
                                    read_only = True,
                                    width=550,
                                    
                               )
                          ]
                     ),
                     ft.Divider(height=10,color='#ffffff'),
                     ft.Row(
                          controls=[
                               
                               ft.TextField(
                                    label = 'Endereço',
                                    label_style=ft.TextStyle(color=ft.colors.BLACK),
                                    border=ft.InputBorder.OUTLINE,
                                    border_radius=ft.border_radius.all(7),
                                    border_width=2,
                                    border_color=ft.colors.GREY_700,
                                    prefix_icon=ft.icons.HOME,
                                    color=ft.colors.BLACK,
                                    cursor_color=ft.colors.BLACK,
                                    cursor_width=1,
                                    hint_text='exemplo@gmail.com',
                                    hint_style = ft.TextStyle(color=ft.colors.GREY),
                                    value = usuario.endereco,
                                    read_only = True,
                                    width=550,
                                    
                               )
                          ]
                     ),
                     ft.Divider(height=10,color='#ffffff'),
                     ft.Row(
                          controls=[
                               
                               ft.TextField(
                                    label = 'Telefone',
                                    label_style=ft.TextStyle(color=ft.colors.BLACK),
                                    border=ft.InputBorder.OUTLINE,
                                    border_radius=ft.border_radius.all(7),
                                    border_width=2,
                                    border_color=ft.colors.GREY_700,
                                    prefix_icon=ft.icons.LOCAL_PHONE,
                                    color=ft.colors.BLACK,
                                    cursor_color=ft.colors.BLACK,
                                    cursor_width=1,
                                    hint_text='exemplo@gmail.com',
                                    hint_style = ft.TextStyle(color=ft.colors.GREY),
                                    value = usuario.telefone,
                                    read_only = True,
                                    width=550,
                                    
                               )
                          ]
                     ),
                     ft.Divider(height=10,color='#ffffff'),
                     ft.Row(
                          controls=[
                               
                               ft.TextField(
                                    label = 'Email',
                                    label_style=ft.TextStyle(color=ft.colors.BLACK),
                                    border=ft.InputBorder.OUTLINE,
                                    border_radius=ft.border_radius.all(7),
                                    border_width=2,
                                    border_color=ft.colors.GREY_700,
                                    prefix_icon=ft.icons.MAIL_OUTLINE,
                                    color=ft.colors.BLACK,
                                    cursor_color=ft.colors.BLACK,
                                    cursor_width=1,
                                    hint_text='exemplo@gmail.com',
                                    hint_style = ft.TextStyle(color=ft.colors.GREY),
                                    value = usuario.email,
                                    read_only = True,
                                    width=550,
                                    
                               )
                                
                          ]
                     ),
                     ft.Divider(height=10,color='#ffffff'),
                     ft.Row(
                        controls=[
                               
                              ft.TextField(
                                    label = 'CNPJ',
                                    label_style=ft.TextStyle(color=ft.colors.BLACK),
                                    border=ft.InputBorder.OUTLINE,
                                    border_radius=ft.border_radius.all(7),
                                    border_width=2,
                                    border_color=ft.colors.GREY_700,
                                    prefix_icon=ft.icons.FINGERPRINT,
                                    color=ft.colors.BLACK,
                                    cursor_color=ft.colors.BLACK,
                                    cursor_width=1,
                                    hint_text='exemplo@gmail.com',
                                    hint_style = ft.TextStyle(color=ft.colors.GREY),
                                    value = usuario.cpf_cnpj,
                                    read_only = True,
                                    width=550,
                                    
                               )

                        ]
                    ),
                    
                ],
                
                alignment=ft.MainAxisAlignment.START,
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
            bgcolor='#ffffff',
            expand=True,
            )




# ALTERAR DADOS ###########################################################################
    
    def open_cadastro(e):
        global cpf_cnpj_cadastro, nome_cadastro, endereco_cadastro, telefone_cadastro,email_cadastro
        busca_usuario(estabelecimento_teste.get_id())
        for p in tabela:
            cpf_cnpj_cadastro.value = p.cpf_cnpj
            nome_cadastro.value = p.nome
            endereco_cadastro.value = p.endereco
            telefone_cadastro.value = p.telefone
            email_cadastro.value = p.email
        
        page.dialog = dialog_cadastro
        dialog_cadastro.open = True
        page.update()

    # Função para fechar o diálogo
    def close_cadastro(e):
        entradas = [cpf_cnpj_cadastro,email_cadastro,telefone_cadastro,nome_cadastro,senha_cadastro,endereco_cadastro]
        for entrada in entradas:
                entrada.error_text = None
                entrada.error_style = None
                entrada.value = None
        dialog_cadastro.open = False
        page.update()

    def cadastrar():
        
        global cpf_cnpj_provisorio,email_provisorio,lista_de_usuarios

        cpf_cnpj_provisorio = estabelecimento_teste.get_cpf_cnpj()
        email_provisorio = estabelecimento_teste.get_email()

        consulta_sql()

        nome = nome_cadastro.value 
        endereco = endereco_cadastro.value 
        cpf_cnpj = cpf_cnpj_cadastro.value
        telefone = telefone_cadastro.value
        email = email_cadastro.value
        senha = senha_cadastro.value

        cpf_cnpj = int(cpf_cnpj)
        telefone = int(telefone)
        
        ok = True
        if  email not in lista_de_usuarios:
            email_cadastro.error_text = None
            email_cadastro.error_style = None
        
        if len(str(cpf_cnpj)) == 14 and cpf_cnpj_cadastro not in lista_de_usuarios:
            cpf_cnpj_cadastro.error_text = None
            cpf_cnpj_cadastro.error_style = None
        
        if len(nome.split()) >= 1:
            nome_cadastro.error_text = None
            nome_cadastro.error_style = None
        
        if '@' in email and '.' in email:
            email_cadastro.error_text = None
            email_cadastro.error_style = None

        if len(senha) >= 6 or len(senha) <= 20:
            senha_cadastro.error_text = None
            senha_cadastro.error_style = None

        if len(endereco) >= 10:
            endereco_cadastro.error_text = None
            endereco_cadastro.error_style = None

        if len(str(telefone)) == 11:
            telefone_cadastro.error_text = None
            telefone_cadastro.error_style = None

        for usuario_banco in lista_de_usuarios :
                
                if usuario_banco.email == email:
                    if email != email_provisorio:
                        ok = False
                        print('| Email já cadastrado por outro usuário!')
                        email_cadastro.error_text = 'Email já cadastrado!'
                        email_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)

                if len(str(cpf_cnpj)) != 14:
                    ok = False
                    cpf_cnpj_cadastro.error_text = 'CNPJ deve conter 14 dígitos!'
                    cpf_cnpj_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)

                if len(nome.split()) < 1:
                    ok = False
                    nome_cadastro.error_text = 'Digite um nome!'
                    nome_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)
                
                if not '@' in email or not '.' in email:
                    ok = False
                    email_cadastro.error_text = 'Digite um email válido!'
                    email_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)

                if len(senha) < 6 or len(senha) > 20:
                    ok = False
                    senha_cadastro.error_text = 'Senha deve ter entre 6-20 caracteres!'
                    senha_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)
                
                if len(endereco) < 10:
                    ok = False
                    endereco_cadastro.error_text = 'Endereço deve ter pelo menos 10 caracteres!'
                    endereco_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)

                if len(str(telefone)) != 11:
                    ok = False
                    telefone_cadastro.error_text = 'Telefone deve conter 11 dígitos!'
                    telefone_cadastro.error_style = ft.TextStyle(color='#ff3230',size=15)
                    
                if usuario_banco.cpf_cnpj == cpf_cnpj:
                        if cpf_cnpj != cpf_cnpj_provisorio:
                            ok = False
                            cpf_cnpj_cadastro.error_text = 'CNPJ já cadastrado!'
                            cpf_cnpj_cadastro.error_style = ft.TextStyle(color='#ff3230')
                            print('| CNPJ já cadastrado por outro usuário!')
        page.update()

        if ok == True:
            entradas = [cpf_cnpj_cadastro,email_cadastro,telefone_cadastro,nome_cadastro,senha_cadastro,endereco_cadastro]
            for entrada in entradas:
                    entrada.error_text = None
                    entrada.error_style = None
                    entrada.value = None
            estabelecimento_teste.alterar_dados(nome, endereco, telefone,email,cpf_cnpj,senha,estabelecimento_teste.get_id())
            busca_usuario(estabelecimento_teste.get_id())
            for p in tabela:
                estabelecimento_teste.set_nome(p.nome)
                estabelecimento_teste.set_endereco(p.endereco)
                estabelecimento_teste.set_telefone(p.telefone)
                estabelecimento_teste.set_email(p.email)
                estabelecimento_teste.set_cpf_cnpj(p.cpf_cnpj)
            page.dialog.open = False
            page.go('/atualizar')
            page.update()
            time.sleep(0.01)
            page.go('/estabelecimento')
            page.update()
            time.sleep(0.25)
            msg_dados(page)

        

    dialog_cadastro = ft.AlertDialog (

        title=ft.Text("ALTERAR DADOS",color=ft.colors.BLACK),
        content=
            ft.Container(
                ft.Column(
                            [
                            nome_cadastro,
                            endereco_cadastro,
                            cpf_cnpj_cadastro,
                            telefone_cadastro,
                            email_cadastro,
                            senha_cadastro
                            ],
                            spacing=20
                        ),
            width=400,
            height=650,
            ),
        actions=[
            ft.TextButton(  "Cancelar",
                            # bgcolor = '#ff312f',
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#ff312f'),
                            on_click=close_cadastro),
            ft.TextButton(  "Confirmar",
                            # bgcolor = '#ff312f',
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#036666'),
                            on_click= lambda e: cadastrar()
                            ),
        ],
        bgcolor='#ffffff',
    )
    comandos = ft.Row(
                    controls=[
                            ft.ElevatedButton(
                                 text='Logout',
                                 style=ft.ButtonStyle(color='#ffffff', bgcolor='#000814'),
                                 on_click=lambda e: confirma_logout()

                                 ),
                            ft.ElevatedButton(
                                 text='Alterar Dados',
                                 style=ft.ButtonStyle(color='#ffffff', bgcolor='#ff312f'),
                                 on_click=open_cadastro
                                 )
                        ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
         )
    
    

    def confirma_logout():
        
        def close_aviso(e):
            aviso_remover.open = False
            aviso_remover.update()
            page.update()

        aviso_remover = ft.BottomSheet(
            ft.Container(
                ft.Column(
                    controls=[
                        ft.Divider(height=10,color=ft.colors.TRANSPARENT),
                        ft.Text(value=f"Tem certeza que deseja sair?",
                                size=20,
                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.BOLD,                            
                                color=ft.colors.BLACK,),
                        ft.Divider(height=5,color=ft.colors.TRANSPARENT),
                        ft.ElevatedButton(content=ft.Text(value='Fazer Logout',size=20),
                                        bgcolor='#ff312f',
                                        color='#ffffff',
                                        width=400,
                                        style=ft.ButtonStyle(
                                            shape= ft.RoundedRectangleBorder(radius=5)
                                            ),
                                        on_click= lambda e: page.go('/login')
                                        ),
                        ft.TextButton(content=ft.Text(value='Cancelar',size=20),
                                        style=ft.ButtonStyle(color='#ff312f'),
                                        width=400,
                                        on_click= close_aviso
                                        ),
                        
                        
                    ],
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER
                ),
                height=200,
                width=500,
            ),
            open=True,
            bgcolor='#ffffff',
        )

        page.overlay.append(aviso_remover)

        page.update()
    

# RODAPÉ ########################################################################### 

    rodape = ft.Container(
    content = ft.Row(
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
                selected=False,
                icon_size=30,
                on_click= lambda e: page.go('/cardapio_estab')
                ),
                ft.IconButton(
                icon = ft.icons.PERSON_OUTLINED,
                selected_icon = ft.icons.PERSON,
                icon_color = ft.colors.GREY,
                selected_icon_color=ft.colors.BLACK,
                selected=True,
                icon_size=30,
                on_click= lambda e: page.go('/estabelecimento'),
                ),
            ],
            alignment = ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.END,
            expand=True
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
                            dados,
                            comandos,
                            cont_rodape
                            ],
                                
                                
                ),
                height=975,
                width=760,
                bgcolor = '#ffffff',
                padding=10,
                expand=True
    )