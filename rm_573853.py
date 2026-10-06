import re
 
 
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
 
 
operadores = ("+", "-", "*", "/")
 
 
# Exercício 5
def tokenizer(expressao_alg):
    padrao = r'\d+\.\d+|\d+|[+\-*/()]'
 
    return re.findall(padrao, expressao_alg)
 
 
# Exercício 6
def precedencia(operador):
    if operador in ('*', '/'):
        return 2
    if operador in ('+', '-'):
        return 1
    return 0
 
 
# Exercício 7
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
 
 
# Exercício 8
def construir_arvore(posfixa):
    pilha = []
 
    for t in posfixa:
        no = No(t)
 
        if t in operadores:
            direita = pilha.pop()      # primeiro pop = filho direito
            esquerda = pilha.pop()     # segundo pop = filho esquerdo
            no.direita = direita
            no.esquerda = esquerda
        pilha.append(no)
 
    return pilha.pop()
 
 
# Exercício 9 - Percursos
# Relação com as notações:
# - pré-ordem (raiz, esquerda, direita) mostra a notação PREFIXA: + 8 * 4 2
# - em ordem (esquerda, raiz, direita) mostra a notação INFIXA: 8 + 4 * 2
#   (sem parênteses, por isso pode perder o agrupamento)
# - pós-ordem (esquerda, direita, raiz) mostra a notação PÓS-FIXA: 8 4 2 * +
def pre_ordem(no):
    if no is None:
        return
    print(no.valor, end=" ")
    pre_ordem(no.esquerda)
    pre_ordem(no.direita)
 
 
def em_ordem(no):
    if no is None:
        return
    em_ordem(no.esquerda)
    print(no.valor, end=" ")
    em_ordem(no.direita)
 
 
def pos_ordem(no):
    if no is None:
        return
    pos_ordem(no.esquerda)
    pos_ordem(no.direita)
    print(no.valor, end=" ")
 
 
# Exercício 10 - Reconstruir a expressão a partir da árvore
def gerar_expressao(no):
    # folha: é só um número
    if no.esquerda is None and no.direita is None:
        return no.valor
 
    esquerda = gerar_expressao(no.esquerda)
    direita = gerar_expressao(no.direita)
    return "(" + esquerda + " " + no.valor + " " + direita + ")"
 
 
# Exercício 11 - Calcular pela árvore
def calcular(no):
    # folha: devolve o número
    if no.esquerda is None and no.direita is None:
        return float(no.valor)
 
    esquerda = calcular(no.esquerda)
    direita = calcular(no.direita)
 
    if no.valor == "+":
        return esquerda + direita
    if no.valor == "-":
        return esquerda - direita
    if no.valor == "*":
        return esquerda * direita
    if no.valor == "/":
        if direita == 0:
            raise ZeroDivisionError("divisão por zero")
        return esquerda / direita
 
 
# Exercício 14 - Validação
def eh_numero(t):
    return t not in operadores and t != "(" and t != ")"
 
 
def validar(tokens, expressao):
    # devolve uma mensagem de erro, ou "" se estiver tudo certo
 
    # expressão vazia
    if expressao.strip() == "":
        return "Expressão vazia."
 
    # caractere não aceito: se juntar os tokens e não der a expressão
    # (sem espaços), alguma coisa foi ignorada pela regex
    if "".join(tokens) != "".join(expressao.split()):
        return "Caractere não aceito na expressão."
 
    # parênteses incompatíveis
    abertos = 0
    for t in tokens:
        if t == "(":
            abertos += 1
        elif t == ")":
            abertos -= 1
            if abertos < 0:
                return "Parênteses incompatíveis: ')' sem '('."
    if abertos != 0:
        return "Parênteses incompatíveis: '(' sem ')'."
 
    # começo e fim
    if tokens[0] in operadores or tokens[0] == ")":
        return "A expressão começa errado."
    if tokens[-1] in operadores or tokens[-1] == "(":
        return "A expressão termina errado."
 
    # ordem dos tokens (ex.: "8 + * 2" ou "8 4")
    for i in range(len(tokens) - 1):
        atual = tokens[i]
        proximo = tokens[i + 1]
 
        if eh_numero(atual) or atual == ")":
            # depois de número ou ")" tem que vir operador ou ")"
            if eh_numero(proximo) or proximo == "(":
                return "Falta um operador entre '" + atual + "' e '" + proximo + "'."
        else:
            # depois de operador ou "(" tem que vir número ou "("
            if proximo in operadores or proximo == ")":
                return "Operador ou parêntese no lugar errado perto de '" + atual + "'."
 
    return ""
 

 
def mostrar_arvore(no, nivel=0):
    # a árvore aparece "deitada": a raiz fica na esquerda
    if no is None:
        return
    mostrar_arvore(no.direita, nivel + 1)
    print("    " * nivel + no.valor)
    mostrar_arvore(no.esquerda, nivel + 1)
 
 
def formatar(numero):
    numero = round(numero, 10)
    if numero == int(numero):
        return str(int(numero))
    return str(numero)
 
 
# Exercício 12 - Saída do programa
def executar(expressao):
    tokens = tokenizer(expressao)
 
    erro = validar(tokens, expressao)
    if erro != "":
        print("Erro:", erro)
        return
 
    posfixa = to_posfixa(tokens)
    raiz = construir_arvore(posfixa)
 
    try:
        resultado = calcular(raiz)
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
        return
 
    print("\nTokens:", tokens)
    print("Pós-fixa:", " ".join(posfixa))
 
    print("Pré-ordem: ", end="")
    pre_ordem(raiz)
    print()
 
    print("Em ordem: ", end="")
    em_ordem(raiz)
    print()
 
    print("Pós-ordem: ", end="")
    pos_ordem(raiz)
    print()
 
    print("Expressão reconstruída:", gerar_expressao(raiz))
 
 
    print("Resultado:", formatar(resultado))
 
 
# Exercício 13 - Testes obrigatórios
def testar():
    testes = [
        ("8 + 4 * 2", 16),
        ("(8 + 4) * 2", 24),
        ("((15 - 3) / 4) + (2 * 5)", 13),
        ("((20 / 5) + 3) * (9 - (2 + 1))", 42),
        ("12.5 + 2.5 * 4", 22.5),
    ]
 
    print("--- Testes de cálculo ---")
    for expressao, esperado in testes:
        tokens = tokenizer(expressao)
        raiz = construir_arvore(to_posfixa(tokens))
        resultado = calcular(raiz)
        if resultado == esperado:
            print("OK    ", expressao, "=", formatar(resultado))
        else:
            print("ERRO  ", expressao, "deu", resultado, "esperado", esperado)
 
    print("--- Testes de validação (todos devem dar erro) ---")
    invalidas = ["", "(8 + 4", "8 + 4)", "8 + a", "8 + * 2", "8 4", "()", "8 +"]
    for expressao in invalidas:
        erro = validar(tokenizer(expressao), expressao)
        if erro != "":
            print("OK    '" + expressao + "' ->", erro)
        else:
            print("ERRO  '" + expressao + "' passou na validação")
 
    print("--- Divisão por zero ---")
    executar("8 / (4 - 4)")
 
 
# Programa principal
while True:
    expressao = input("\nDigite uma expressão (ou 'testes' / 'sair'): ")
 
    if expressao == "sair":
        break
    elif expressao == "testes":
        testar()
    else:
        executar(expressao)