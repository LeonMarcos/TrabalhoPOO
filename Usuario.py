from abc import ABC, abstractmethod

class Usuario(ABC):
    """
    Classe abstrata que define a estrutura básica de um usuário genérico.
    """

    # Métodos getters abstratos

    @abstractmethod
    def get_nome(self) -> str:
        """ Método abstrato para obter o nome do usuário. """
        pass

    @abstractmethod
    def get_endereco(self) -> str:
        """ Método abstrato para obter o endereço do usuário. """
        pass

    @abstractmethod
    def get_telefone(self) -> int:
        """ Método abstrato para obter o telefone do usuário. """
        pass

    @abstractmethod
    def get_email(self) -> str:
        """ Método abstrato para obter o email do usuário. """
        pass

    @abstractmethod
    def get_cpf_cnpj(self) -> int:
        """ Método abstrato para obter o CPF ou CNPJ do usuário. """
        pass

    @abstractmethod
    def get_senha(self) -> str:
        """ Método abstrato para obter a senha do usuário. """
        pass

    # Métodos setters abstratos

    @abstractmethod
    def set_nome(self, nome: str) -> None:
        """ Método abstrato para definir o nome do usuário. """
        pass

    @abstractmethod
    def set_endereco(self, endereco: str) -> None:
        """ Método abstrato para definir o endereço do usuário. """
        pass

    @abstractmethod
    def set_telefone(self, telefone: int) -> None:
        """ Método abstrato para definir o telefone do usuário. """
        pass

    @abstractmethod
    def set_email(self, email: str) -> None:
        """ Método abstrato para definir o email do usuário. """
        pass

    @abstractmethod
    def set_cpf_cnpj(self, cpf_cnpj: int) -> None:
        """ Método abstrato para definir o CPF ou CNPJ do usuário. """
        pass

    @abstractmethod
    def set_senha(self, senha: str) -> None:
        """ Método abstrato para definir a senha do usuário. """
        pass

    # Método responsável por alterar dados do usuário

    @abstractmethod
    def alterar_dados(self) -> None:
        """
        Método abstrato para alterar os dados do usuário.
        Deve ser implementado nas subclasses para realizar a alteração específica.
        """
        pass
