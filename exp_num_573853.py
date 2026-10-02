import re

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


expressao = input("Digite a expressão numérica: ")
operadores = ("+", "-", "*", "/", "()")

def tokenizer(expressao_alg):
    padrao = r'\d+\.\d+|\d+|[+\-*/()]'

    return re.findall(padrao, expressao_alg)
# 6
def precedencia(operador):
    if operador in ('*', '/'):
        return 2
    if operador in ('+', '-'):
        return 1
    return 0

print(tokenizer(expressao))

def infixa(expressao_alg):
    saida = []
    pilha = []