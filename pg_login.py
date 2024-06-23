from cgitb import text
from itertools import product
from sre_parse import State
from tkinter import HORIZONTAL
from tkinter.tix import DisplayStyle
from turtle import bgcolor, color, screensize
from typing import Text
from annotated_types import T
from click import password_option
import flet as ft
import pg_aux
from Conex_SQL import connection
from Usuario import Usuario
from types import SimpleNamespace
import time
from Cliente import Cliente
from Estabelecimento import Estabelecimento
from Sistema import Sistema

cliente = Cliente()
estabelecimento_teste = Estabelecimento()
sistema_aux = Sistema()

cursor = connection.cursor()

usuario_login = None

def salva_dados_usuario(usuario):
        global cliente,estabelecimento_teste,usuario_login
        if usuario.tipo == 'Cliente':
            cliente.set_nome(usuario.nome)
            cliente.set_endereco(usuario.endereco)
            cliente.set_telefone(usuario.telefone)
            cliente.set_email(usuario.email)
            cliente.set_cpf_cnpj(usuario.cpf_cnpj)
            cliente.set_id(usuario.id)
            usuario_login = 'Cliente'

        if usuario.tipo == 'Estabelecimento':
            estabelecimento_teste.set_nome(usuario.nome)
            estabelecimento_teste.set_endereco(usuario.endereco)
            estabelecimento_teste.set_telefone(usuario.telefone)
            estabelecimento_teste.set_email(usuario.email)
            estabelecimento_teste.set_cpf_cnpj(usuario.cpf_cnpj)
            estabelecimento_teste.set_id(usuario.id)
            usuario_login = 'Estabelecimento'
            
         
    
def retorna_dados_usuario():
        if usuario_login == 'Cliente':
            return cliente
        if usuario_login == 'Estabelecimento':
            return estabelecimento_teste

lista_de_usuarios=[]
def consulta_sql():
    consulta = """ SELECT * FROM Usuarios; """ #consulta o banco de dados

    cursor.execute(consulta) 
    aux = cursor.fetchall()
    lista_de_usuarios.clear()
    for p in aux:
          lista_de_usuarios.append(p)


ok = True

def login_usuario(page, email, senha):

    consulta_sql()

    # sistema_aux.login(page, email, senha, lista_de_usuarios,login_email,login_senha,salva_dados_usuario)
    
    for usuario_banco in lista_de_usuarios:
                    global ok
                    
                    if usuario_banco.email != email:
                            login_email.error_text = 'Email não cadastrado!'
                            login_email.error_style = ft.TextStyle(color='#ff3230',size=15)
                            login_senha.error_text = None
                            login_senha.error_style = None
                    
                    if usuario_banco.senha != senha:
                            ok = False
                            login_senha.error_text = 'Senha incorreta!'
                            login_senha.error_style = ft.TextStyle(color='#ff3230',size=15)
                    
                    if usuario_banco.email == email and \
                        usuario_banco.senha == senha:
                        ok = True
                        salva_dados_usuario(usuario_banco)
                        if usuario_banco.tipo == 'Cliente':
                            page.go('/inicio')
                            
                        if usuario_banco.tipo == 'Estabelecimento':
                            page.go('/pendentes')

                    if ok == True:
                        entradas = [login_email,login_senha]
                        for entrada in entradas:
                                entrada.error_text = None
                                entrada.error_style = None
                                entrada.value = None
                                
    
    for p in lista_de_usuarios:
        if p.email == email:
            login_email.error_text = None
            login_email.error_style = None

    page.update()


msg_cad = ft.Row(controls=[
                            ft.Icon(name=ft.icons.CHECK_CIRCLE,color='#ffffff'),
                            ft.Text(
                                    value="Cadastro realizado com sucesso!",
                                    color='#ffffff',
                                    size=20),
             ])

cad_feito = ft.SnackBar(
                content=msg_cad,
                bgcolor='#0f6e72',
                duration=2000
                )
def cad_msg(page):
    time.sleep(0.25)
    page.show_snack_bar(cad_feito)
    page.update()

def cadastro_usuario(page, nome, endereco, cpf_cnpj, telefone, email, senha):
        consulta_sql()

        sistema_aux.cadastro(page, nome, endereco, cpf_cnpj, telefone, email, senha, tipo_usuario,lista_de_usuarios,email_cadastro,cpf_cnpj_cadastro,nome_cadastro,senha_cadastro,endereco_cadastro,telefone_cadastro,login_email,login_senha,cad_msg)
        

tipo_usuario = 'Cliente'

print(tipo_usuario)
def mudar_tipo_usuario(e,page):
    global tipo_usuario

    if e.control.value:
        tipo_usuario = 'Estabelecimento'
        cpf_cnpj_cadastro.label = 'CNPJ'
        cpf_cnpj_cadastro.hint_text='00.000.000/0000-00'
        nome_cadastro.prefix_icon=ft.icons.STOREFRONT_OUTLINED
        nome_cadastro.label = 'Nome'
        nome_cadastro.hint_text = 'Nome do Estabelecimento'
  
    else:
        cpf_cnpj_cadastro.label = 'CPF'
        tipo_usuario = 'Cliente'
        cpf_cnpj_cadastro.hint_text='000.000.000-00'
        nome_cadastro.prefix_icon=ft.icons.PERSON
        nome_cadastro.label = 'Nome Completo'
        nome_cadastro.hint_text = 'Nome Sobrenome'

    print(tipo_usuario)
    page.dialog.open = False
    page.update()
    page.dialog.open = True
    page.update()



login_email = ft.TextField(
     
        label='Email',
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.OUTLINE,
        border_radius=ft.border_radius.all(7),
        border_width=2,
        border_color=ft.colors.GREY_700,
        prefix_icon=ft.icons.EMAIL_OUTLINED,
        color=ft.colors.BLACK,
        cursor_color=ft.colors.BLACK,
        cursor_width=1,
        hint_text='exemplo@gmail.com',
        hint_style = ft.TextStyle(color=ft.colors.GREY),
        error_text = None,
        error_style = None
        )

login_senha = ft.TextField(
     
        label = 'Senha',
        password=True,
        can_reveal_password=True,
        # reveal_password_icon_color=ft.colors.BLACK,
        
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.OUTLINE,
        border_radius=ft.border_radius.all(7),
        border_width=2,
        border_color=ft.colors.GREY_700,
        prefix_icon=ft.icons.KEY,
        color=ft.colors.BLACK,
        cursor_color=ft.colors.BLACK,
        cursor_width=1,
        error_text = None,
        error_style = None
        )

nome_cadastro = ft.TextField(
        label='Nome Completo',
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.OUTLINE,
        border_radius=ft.border_radius.all(7),
        border_width=2,
        border_color=ft.colors.GREY_700,
        prefix_icon=ft.icons.PERSON,
        color=ft.colors.BLACK,
        cursor_color=ft.colors.BLACK,
        cursor_width=1,
        hint_text='Nome Sobrenome',
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
        label='CPF',
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        border=ft.InputBorder.OUTLINE,
        border_radius=ft.border_radius.all(7),
        border_width=2,
        border_color=ft.colors.GREY_700,
        prefix_icon=ft.icons.FINGERPRINT,
        color=ft.colors.BLACK,
        cursor_color=ft.colors.BLACK,
        cursor_width=1,
        hint_text='000.000.000-00',
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



numeros_cpf_cnpj = 0
numeros_telefone = 0
      
def page_login(page: ft.Page):
    

    def extrair_numeros(e):
        global numeros_cpf_cnpj,numeros_telefone
        texto = cpf_cnpj_cadastro.value
        aux2 = telefone_cadastro.value
        numeros_cpf_cnpj = ''.join(filter(str.isdigit, texto))
        numeros_telefone = ''.join(filter(str.isdigit, aux2))
        print(numeros_telefone)
        page.update()

    def formatar_cpf_cnpj(e):
        if cpf_cnpj_cadastro.label == 'CPF':
            texto = e.control.value
            # Remove qualquer caractere não numérico
            texto = ''.join(filter(str.isdigit, texto))
            
            # Limita a entrada a no máximo 11 números
            if len(texto) > 11:
                texto = texto[:11]
            
            # Aplica a formatação de CPF (XXX.XXX.XXX-XX)
            if len(texto) > 2:
                texto = texto[:3] + '.' + texto[3:]
            if len(texto) > 6:
                texto = texto[:7] + '.' + texto[7:]
            if len(texto) > 10:
                texto = texto[:11] + '-' + texto[11:]
            
            # Atualiza o valor no campo de texto
            e.control.value = texto
            extrair_numeros(e)
            # print(numeros_cpf_cnpj)
            page.update()
        
        if cpf_cnpj_cadastro.label == 'CNPJ':
            texto = e.control.value
            # Remove qualquer caractere não numérico
            texto = ''.join(filter(str.isdigit, texto))
            
            # Limita a entrada a no máximo 11 números
            if len(texto) > 11:
                texto = texto[:10]
            
            # Aplica a formatação de CPF (XXX.XXX.XXX-XX)
            if len(texto) > 1:
                texto = texto[:2] + '.' + texto[2:]
            if len(texto) > 5:
                texto = texto[:6] + '.' + texto[6:]
            if len(texto) > 9:
                texto = texto[:10] + '/0001' + texto[10:]
            if len(texto) > 14:
                texto = texto[:15] + '-' + texto[15:]
            
            
            
            # Atualiza o valor no campo de texto
            e.control.value = texto
            extrair_numeros(e)
            # print(numeros_cpf_cnpj)
            page.update()
    
    def formatar_telefone(e):
            texto = e.control.value
            # Remove qualquer caractere não numérico
            texto = ''.join(filter(str.isdigit, texto))
            
            # Limita a entrada a no máximo 11 números
            if len(texto) > 11:
                texto = texto[:11]
            
            # Aplica a formatação de CPF (XXX.XXX.XXX-XX)
            if len(texto) > 0:
                texto = texto[:0] + '(' + texto[0:]
            if len(texto) > 2:
                texto = texto[:3] + ')' + texto[3:]
            if len(texto) > 8:
                texto = texto[:9] + '-' + texto[9:]
            if len(texto) > 12:
                texto = texto[:14] + '' + texto[14:]
            
            # Atualiza o valor no campo de texto
            e.control.value = texto
            extrair_numeros(e)
            # print(numeros_cpf_cnpj)
            page.update()
    
    cpf_cnpj_cadastro.on_change = lambda e: formatar_cpf_cnpj(e)
    telefone_cadastro.on_change = lambda e: formatar_telefone(e)



    switch_aux = [
                ft.Row(
                    controls = [

                    ft.Switch(
                        thumb_icon={
                            ft.MaterialState.DEFAULT: ft.icons.PERSON,
                            ft.MaterialState.SELECTED: ft.icons.STOREFRONT
                        },
                        scale=1.25,
                        on_change=lambda e: mudar_tipo_usuario(e,page)
                        ),

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
            ),
    ]

    switch = ft.Column(
         controls=switch_aux,
         alignment=ft.MainAxisAlignment.CENTER
    )

    page.bgcolor = '#ff3230'
    page.window_title_bar_hidden = False
    # page.window_resizable = False
    page.window_width = 725
    # page.window_height = 1047
    page.window_height = 760
    page.window_resizable = True
    page.window_max_width = 725

    # Aplicando o esquema de cores à página
    page.theme = ft.Theme(
         color_scheme=ft.ColorScheme(
                                    on_surface_variant='#ff3230',
                                    error='#ff3230',
                                    on_error='#ff3230',
                                    surface='#ff3230')
    )

# POP-UP LOGIN_usuario ###########################################################################################################
    
    def open_login(e):
        page.dialog = dialog_login
        dialog_login.open = True
        page.update()

    # Função para fechar o diálogo
    def close_login(e):
        dialog_login.open = False
        page.update()

    # Conteúdo do diálogo
    
    dialog_login = ft.AlertDialog (
        icon_color = '',

        title=ft.Text("LOGIN",color=ft.colors.BLACK),
        content=
            ft.Container(
                ft.Column(
                    controls=[
                            login_email,
                            login_senha
                            ],
                        ),
            width=400,
            height=165,
            ),
        actions=[
            ft.TextButton(  "Voltar",
                            # bgcolor = '#ff312f',
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#ff312f'),
                            on_click=close_login),
            ft.TextButton(  "Entrar",
                            # bgcolor = '#ff312f',
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#036666'),
                            # on_click=lambda e: login_usuario(login_email.value,login_senha.value),
                            on_click=lambda e: login_usuario(page,login_email.value,login_senha.value)
            )
                
        ],
        
        bgcolor='#ffffff',
    )
    

# POP-UP CADASTRO ###########################################################################################################

    def open_cadastro(e):
        page.dialog = dialog_cadastro
        dialog_cadastro.open = True
        page.update()

    # Função para fechar o diálogo
    def close_cadastro(e):
        dialog_cadastro.open = False
        page.update()


    # Conteúdo do diálogo
    dialog_cadastro = ft.AlertDialog (
         icon_color='000000',

        title=ft.Text("CADASTRO",color=ft.colors.BLACK),
        content=
            ft.Container(
                ft.Column(
                            [
                            switch,
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
            height=700
            ),
        actions=[
            ft.TextButton(  "Voltar",
                            # bgcolor = '#ff312f',
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#ff312f'),
                            on_click=close_cadastro,
                        ),
            ft.TextButton(  "Cadastrar",
                            # bgcolor = '#ff312f',
                            style=ft.ButtonStyle(color= '#ffffff',bgcolor='#036666'),
                            on_click=lambda e: cadastro_usuario(page,nome_cadastro.value,endereco_cadastro.value,numeros_cpf_cnpj,numeros_telefone,email_cadastro.value,senha_cadastro.value),
                            # page.update()
                        )
            
        ],
        bgcolor='#ffffff'
    )

# BOTÕES DE LOGIN E CADASTRO ###########################################################################################################

    btn = ft.Column(
        controls= [
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        icon = ft.icons.LOGIN,
                        text='Login',
                        width=400,
                        height = 75,
                        on_click=open_login,
                        
                        style=ft.ButtonStyle(
                            color= '#ffffff',
                            # bgcolor='#ff312f',
                            bgcolor = {ft.MaterialState.HOVERED: ft.colors.BLACK, '': '#ff312f'},
                            padding={ft.MaterialState.DEFAULT: 20},
                            animation_duration=1000
                            )
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text='Cadastro',
                        icon = ft.icons.ASSIGNMENT_IND_OUTLINED,
                        
                        width=400,
                        height = 75,
                        on_click=open_cadastro,
                        style=ft.ButtonStyle(
                            color= '#ffffff',
                            # bgcolor='#ff312f',
                            bgcolor = {ft.MaterialState.HOVERED: ft.colors.BLACK, '': '#ff312f'},
                            padding={ft.MaterialState.DEFAULT: 20},
                            
                            animation_duration=1000
                            )
                        )
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
        )
        ],
        width=800,
        height=500,
        spacing=50,
        alignment = ft.MainAxisAlignment.START
        # horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

# LOGO ###########################################################################################################

    row1 = ft.Row(
            controls= [
                ft.Image(
                    src='images/SVG LOGO UFMG.svg',
                    height=150,
                    width=150,
                ),
            ],
        alignment = ft.MainAxisAlignment.CENTER,
        vertical_alignment= ft.CrossAxisAlignment.CENTER,
    )

    cont_principal = ft.Container(
        ft.Column(
            controls=[
                ft.Divider(height=20,color='#ffffff'),
                row1,
                ft.Divider(height=20,color='#ffffff'),
                # video,
                btn,
                ],
        ),
        bgcolor= '#ffffff',
        height=800,
        width=600,
        margin=ft.margin.all(100),
        border_radius = ft.border_radius.all(30),
        
    )

    return ft.Container(
        content=cont_principal,
        
        bgcolor= '#ff3230',
        height=screensize,
        width=760,
        expand=True
    )