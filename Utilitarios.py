import os
import unicodedata
from IPython import get_ipython

def limpar_tela() -> None:
    
    ipython = get_ipython()
    if ipython is not None:
        ipython.run_line_magic('clear', '')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        
def limpar_texto(texto:str) -> str:
    
    texto_sem_acentos = ''.join(ch for ch in unicodedata.normalize('NFD', texto) if not unicodedata.combining(ch))
    texto_sem_espacos = texto_sem_acentos.replace(" ", "")
    texto_minusculo = texto_sem_espacos.lower()
    return texto_minusculo