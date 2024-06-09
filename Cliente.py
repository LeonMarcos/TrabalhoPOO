# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:18:22 2024

"""

from Usuario import Usuario
from Utilitarios import limpar_tela
import re
# from Pedido import Pedido
# from typing import Type


class Cliente(Usuario):
    # Constantes
    # Regex para garantir que o telefone tenha exatamente 11 dígitos
    padrao_telefone = r"^\d{11}$"
    # Regex para garantir que o nome só contenha letras e espaços
    padrao_nome = r"^[a-zA-Z ]+$"
    # Regex para garantir que o cpf tenha exatamente 11 dígitos
    padrao_cpf = r"^\d{11}$"

    def __init__(self):
        super().__init__()
        self._nome = None
        self._endereco = None
        self._telefone = None
        self._email = None
        self._cpf_cnpj = None
        self._senha = None
        self.tipo = self.__class__.__name__

    def get_nome(self) -> str:
        return self._nome

    def get_endereco(self) -> str:
        return self._endereco

    def get_telefone(self) -> int:
        return self._telefone

    def get_email(self) -> str:
        return self._email

    def get_cpf_cnpj(self) -> int:
        return self._cpf_cnpj

    def get_senha(self) -> str:
        return self._senha

    def cria_Usuario(self) -> None:
        limpar_tela()
        print(f"\n---------  Cadastrar {self.__class__.__name__}  ---------\n")

        # Tratamento de exceção para o nome
        while True:
            try:
                nome = str(input("\nNome: "))
                if len(nome.split()) >= 2 and re.fullmatch(self.padrao_nome, nome):
                    self._nome = nome
                    break
                else:
                    print(
                        "Nome inválido. Por favor, digite um nome com no mínimo nome e sobrenome, contendo apenas letras e espaços.")
            except:
                print("Nome inválido. Por favor, digite novamente.")

        # Tratamento de exceção para o endereço
        while True:
            try:
                self._endereco = str(input("Endereço: "))
                break
            except:
                print("Endereço inválido. Por favor, digite novamente.")

        # Tratamento de exceção para o telefone
        while True:
            try:
                telefone = input("Telefone (11 dígitos com DDD): ")
                if re.fullmatch(self.padrao_telefone, telefone):
                    self._telefone = int(telefone)
                    break
                else:
                    print(
                        "Número de telefone inválido. Por favor, digite um número com 11 dígitos (DDD + número).")
            except:
                print("Número de telefone inválido. Por favor, digite novamente.")

        # Tratamento de exceção para o email
        while True:
            try:
                self._email = str(input("E-mail: "))
                if "@" in self._email:
                    break
                else:
                    print("E-mail inválido. O e-mail deve conter '@'.")
            except:
                print("E-mail inválido. Por favor, digite novamente.")

        # Tratamento de exceção para o cpf
        while True:
            try:
                if self.tipo == 'Cliente':
                    cpf = re.sub(r'\D', '', input(
                        "CPF (11 dígitos somente números.): "))
                    if re.fullmatch(self.padrao_cpf, cpf):
                        self._cpf_cnpj = int(cpf)
                        break
                    else:
                        print("Número de CPF inválido. Por favor, digite novamente.")
            except:
                print("Número de CPF inválido. Por favor, digite novamente.")

        # Tratamento de exceção para a senha
        while True:
            try:
                senha = input("Digite sua senha: ")
                if len(senha) >= 6:
                    self._senha = senha
                    break
                else:
                    print(
                        "A senha deve ter pelo menos 6 dígitos. Por favor, digite novamente.")
            except:
                print("Senha inválida. Por favor, digite novamente.")

    # Método para atualizar usuário
    def atualiza_Usuario(self) -> None:
        limpar_tela()
        print(f"\n---------  Atualizar {self.__class__.__name__}  ---------\n")
        atributos = {
            "1": "Nome",
            "2": "Endereço",
            "3": "Telefone",
            "4": "E-mail",
            "5": "CPF",
            "6": "Senha"
        }
        while True:
            print("\nEscolha o atributo a ser atualizado:")
            for key, value in atributos.items():
                print(f"{key}. {value}")
            escolha = input("Digite o número do atributo (ou '0' para sair): ")
            if escolha == '0':
                break
            elif escolha in atributos:
                atributo = atributos[escolha]
                if atributo == "Nome":
                    while True:
                        try:
                            nome = str(input("\nNovo Nome: "))
                            if len(nome.split()) >= 2 and re.fullmatch(self.padrao_nome, nome):
                                self._nome = nome
                                break
                            else:
                                print(
                                    "Nome inválido. Por favor, digite um nome com no mínimo nome e sobrenome, contendo apenas letras e espaços.")
                        except:
                            print("Nome inválido. Por favor, digite novamente.")
                elif atributo == "Endereço":
                    while True:
                        try:
                            self._endereco = str(input("Novo Endereço: "))
                            break
                        except:
                            print("Endereço inválido. Por favor, digite novamente.")
                elif atributo == "Telefone":
                    while True:
                        try:
                            telefone = input(
                                "Novo Telefone (11 dígitos com DDD): ")
                            if re.fullmatch(self.padrao_telefone, telefone):
                                self._telefone = int(telefone)
                                break
                            else:
                                print(
                                    "Número de telefone inválido. Por favor, digite um número com 11 dígitos (DDD + número).")
                        except:
                            print(
                                "Número de telefone inválido. Por favor, digite novamente.")
                elif atributo == "E-mail":
                    while True:
                        try:
                            self._email = str(input("Novo E-mail: "))
                            if "@" in self._email:
                                break
                            else:
                                print("E-mail inválido. O e-mail deve conter '@'.")
                        except:
                            print("E-mail inválido. Por favor, digite novamente.")
                elif atributo == "CPF":
                    while True:
                        try:
                            cpf = re.sub(r'\D', '', input(
                                "Novo CPF (11 dígitos somente números.): "))
                            if re.fullmatch(self.padrao_cpf, cpf):
                                self._cpf_cnpj = int(cpf)
                                break
                            else:
                                print(
                                    "Número de CPF inválido. Por favor, digite novamente.")
                        except:
                            print(
                                "Número de CPF inválido. Por favor, digite novamente.")
                elif atributo == "Senha":
                    while True:
                        try:
                            senha = input("Nova Senha: ")
                            if len(senha) >= 6:
                                self._senha = senha
                                break
                            else:
                                print(
                                    "A senha deve ter pelo menos 6 dígitos. Por favor, digite novamente.")
                        except:
                            print("Senha inválida. Por favor, digite novamente.")
            else:
                print("Escolha inválida. Por favor, tente novamente.")

        # self.tipo = self.__class__.__name__
        limpar_tela()


if __name__ == "__main__":
    clienteum = Cliente()
    clienteum.cria_Usuario()
    print("\n")
    print(clienteum.get_nome())
    print(clienteum.get_endereco())
    print(clienteum.get_telefone())
    print(clienteum.get_email())
    print(clienteum.get_cpf_cnpj())
    print(clienteum.get_senha())
    clienteum.atualiza_Usuario()
    print("\n")
    print(clienteum.get_nome())
    print(clienteum.get_endereco())
    print(clienteum.get_telefone())
    print(clienteum.get_email())
    print(clienteum.get_cpf_cnpj())
    print(clienteum.get_senha())
