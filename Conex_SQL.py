

import pyodbc

# Lista de strings de conexão para os diferentes servidores
servers = [
    r"Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=UFMGFood;",
    r"Driver={SQL Server};LAPTOP-AISSTUU7\SQLEXPRESS;Database=UFMGFood;",
    r"Driver={SQL Server};Server=LEON;Database=UFMGFood;"
]

# Função para tentar conectar aos servidores
def connect_to_server(servers):
    connection = None
    for server in servers:
        try:
            connection = pyodbc.connect(server)
            print(f"Conectado com sucesso ao servidor: {server}")
            break  # Conexão bem-sucedida, sair do loop
        except pyodbc.Error as ex:
            print(f"Falha ao conectar ao servidor: {server}")
            print("Erro:", ex)
    return connection

# Tentar conectar aos servidores
connection = connect_to_server(servers)

