import os
from IPython import get_ipython

def limpar_tela():
    
    ipython = get_ipython()
    if ipython is not None:
        ipython.run_line_magic('clear', '')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')