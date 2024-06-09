from abc import ABC, abstractmethod
import re
from Utilitarios import limpar_tela


class Usuario:
    # Métodos getters
    @abstractmethod
    def get_nome(self) -> str:
        pass

    @abstractmethod
    def get_endereco(self) -> str:
        pass

    @abstractmethod
    def get_telefone(self) -> int:
        pass

    @abstractmethod
    def get_email(self) -> str:
        pass

    @abstractmethod
    def get_cpf_cnpj(self) -> int:
        pass

    @abstractmethod
    def get_senha(self) -> str:
        pass

    # Método responsável por criar o usuário
    @abstractmethod
    def cria_Usuario(self) -> None:
        pass

# Método responsável por atualizar algum parametro
    @abstractmethod
    def atualiza_Usuario(self) -> None:
        pass
