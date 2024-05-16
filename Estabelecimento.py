# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:04:34 2024

@author: lmfel
"""

from Usuario import Usuario
from Cliente import Cliente

class Estabelecimento(Usuario):
    
    def __init__(self):
        super().__init__()
        self.__horario_funcio = [None, None]  # Inicializando com None para indicar horários indefinidos
        
    def define_horario(self, abertura: float, fechamento: float) -> None:
        # Tratamento de exceção para o horário
        if not (0 <= abertura < 24 and 0 <= fechamento < 24):
            raise ValueError("Horários devem estar entre 0 e 24")
        if abertura >= fechamento:
            raise ValueError("O horário de abertura deve ser menor que o de fechamento")
        self.__horario_funcio[0] = abertura
        self.__horario_funcio[1] = fechamento
        
    def get_horario(self) -> list:
        return self.__horario_funcio
    
'''def main():
    estabelecimentoum = Estabelecimento()
    estabelecimentoum.cria_Usuario()
    print("\n")
    print(estabelecimentoum.get_nome())
    print(estabelecimentoum.get_endereco())
    print(estabelecimentoum.get_telefone())
    print(estabelecimentoum.get_email())
    print(estabelecimentoum.get_cpf_cnpj())
    print(estabelecimentoum.get_senha())
    
    estabelecimentoum.define_horario(16, 23)
    print(estabelecimentoum.get_horario())
        
main()'''