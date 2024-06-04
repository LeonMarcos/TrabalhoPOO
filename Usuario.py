from abc import ABC, abstractmethod
import re
import os

class Usuario:
    # Constantes
    # Regex para garantir que o telefone tenha exatamente 11 dígitos
    padrao_telefone = r"^\d{11}$"
    # Regex para garantir que o nome só contenha letras e espaços
    padrao_nome = r"^[a-zA-Z ]+$"
    # Regex para garantir que o cpf tenha exatamente 11 dígitos
    padrao_cpf = r"^\d{11}$"
    # Regex para garantir que o cnpj tenha exatamente 14 dígitos
    padrao_cnpj = r"^\d{14}$"

    # Atributos e construtor da classe Usuario
    def __init__(self) -> None:
        self._nome = None
        self._endereco = None
        self._telefone = None
        self._email = None
        self._cpf_cnpj = None
        self._senha = None
        self._saldo = None
        self.tipo = self.__class__.__name__

    # Métodos getters
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

    def atualiza_saldo(self, saldo) -> None:
        self._saldo = saldo

    def get_saldo(self) -> float:
        return self._saldo

    # Método responsável por criar o usuário
    def cria_Usuario(self) -> None:
        os.system('cls')
        print(f"\n---------  Cadastrar {self.__class__.__name__}  ---------\n")

        # Tratamento de exceção para o nome
        while True:
            try:
                nome = str(input("\nNome: "))
                if len(nome.split()) >= 2 and re.fullmatch(self.padrao_nome, nome):
                    self._nome = nome
                    break
                else:
                    print("Nome inválido. Por favor, digite um nome com no mínimo 3 palavras, contendo apenas letras e espaços.")
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
                    print("Número de telefone inválido. Por favor, digite um número com 11 dígitos (DDD + número).")
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

        # Tratamento de exceção para o cpf/cnpj
        while True:
            try:
                if self.tipo == 'Cliente':
                    cpf = re.sub(r'\D', '', input("CPF (11 dígitos somente números.): "))
                    if re.fullmatch(self.padrao_cpf, cpf):
                        self._cpf_cnpj = int(cpf)
                        break
                    else:
                        print("Número de CPF inválido. Por favor, digite novamente.")
                else:
                    cnpj = re.sub(r'\D', '', input("CNPJ (10 dígitos somente números. O 0001 será adicionado automaticamente.): "))
                    if len(cnpj) == 10 and cnpj.isdigit():
                        # Insere '0001' entre o 8º e o 9º dígito
                        cnpj = cnpj[:8] + '0001' + cnpj[8:]
                        self._cpf_cnpj = int(cnpj)
                        break
                    else:
                        print("Número de CNPJ inválido. Por favor, digite novamente.")
            except:
                print("Número de CPF/CNPJ inválido. Por favor, digite novamente.")

        # Tratamento de exceção para a senha
        while True:
            try:
                senha = input("Digite sua senha: ")
                if len(senha) >= 6:
                    self._senha = senha
                    break
                else:
                    print("A senha deve ter pelo menos 6 dígitos. Por favor, digite novamente.")
            except:
                print("Senha inválida. Por favor, digite novamente.")

        # self.tipo = self.__class__.__name__
        os.system('cls')


if __name__ == "__main__":

    # Testando com Estabelecimento
    estabelecimento = Usuario()
    estabelecimento.cria_Usuario()
    print("\nEstabelecimento:")
    print(estabelecimento.get_nome())
    print(estabelecimento.get_endereco())
    print(estabelecimento.get_telefone())
    print(estabelecimento.get_email())
    print(estabelecimento.get_cpf_cnpj())
    print(estabelecimento.get_senha())
    print(estabelecimento.tipo)