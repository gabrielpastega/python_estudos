# função que não queremos importar com 'from meu_modulo import *'
def _funcao_privada():
    print("Tentando me importar né?")

# função que queremos tornar acessível através de 'from meu_modulo import *'
def funcao_publica():
    print("Esta função pode ser importada com '*'")
