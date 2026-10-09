class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None

class BST:
    def __init__(self):
        self.raiz = None

def inserir(self, dado):
    novo = No(dado)
    if self.raiz is None:
        self.raiz = novo
        return

    atual = self.raiz

    while True:
        if dado < atual.dado:
            if atual.esquerda is None:
                atual.esquerda = novo
                return
            atual = atual.esquerda
        elif dado > atual.dado:
            if atual.direita is None:
                atual.direita = novo
                return
            atual = atual.direita
        else:
            return # valor duplicado: não inserir

def buscar(self, dado):
    atual = self.raiz
    while atual is not None:
        if dado == atual.dado:
            return True
        if dado < atual.dado:
            atual = atual.esquerda
        else:
            atual = atual.direita
    return False

def minimo(self, no=None):
    atual = self.raiz if no is None else no
    if atual is None:
        return None
    while atual.esquerda is not None:
        atual = atual.esquerda
    
    return atual.dado

def maximo(self, no=None):
    atual = self.raiz if no is None else no
    if atual is None:
        return None
    while atual.direita is not None:
        atual = atual.direita
    return atual.dado

# # Conceitualmente:
# menor_da_subarvore = arvore.minimo(no_inicial)
# maior_da_subarvore = arvore.maximo(no_inicial)

def em_ordem(self, no):
    if no is not None:
        self.em_ordem(no.esquerda)
        print(no.dado, end=" ")
        self.em_ordem(no.direita)

# Exemplo 11 16 31 43 49 55 59 61 65 69 73 77 81 85 89
def pre_ordem(self, no):
    if no is not None:
        print(no.dado, end=" ")
        self.pre_ordem(no.esquerda)
        self.pre_ordem(no.direita)

def pos_ordem(self, no):
    if no is not None:
        self.pos_ordem(no.esquerda)
        self.pos_ordem(no.direita)
        print(no.dado, end=" ")

def remover(self, no, dado):
    if no is None:
        return None
            
    if dado < no.dado:
            no.esquerda = self.remover(no.esquerda, dado)
    elif dado > no.dado:
            no.direita = self.remover(no.direita, dado)
    else:
        # Caso 1 ou caso 2: Um filho ou nenhum
        if no.esquerda is None:
            return no.direita
        if no.direita is None:
            return no.esquerda
                
        # Caso 3: Dois filhos
        sucessor = no.direita
        while sucessor.esquerda is not None:
            sucessor = sucessor.esquerda
                
        no.dado = sucessor.dado
        no.direita = self.remover(no.direita, sucessor.dado)
            
    return no

def excluir(self, dado):
    self.raiz = self.remover(self.raiz, dado)
