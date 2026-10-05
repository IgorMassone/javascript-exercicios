import re

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


expressao = input("Digite a expressão numérica: ")
operadores = ("+", "-", "*", "/")

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

def to_posfixa(tokens):
    saida = []
    pilha = []

    for t in tokens:
        if t == "(":
            pilha.append(t)
        elif t == ")":
            while pilha and pilha[-1] != "(":
                saida.append(pilha.pop())
            pilha.pop()
        elif t in operadores:
            while pilha and pilha[-1] != "(" and precedencia(pilha[-1]) >= precedencia(t):
                saida.append(pilha.pop())
            pilha.append(t)
        else:
            saida.append(t)
    while pilha:
        saida.append(pilha.pop())
 
    return saida