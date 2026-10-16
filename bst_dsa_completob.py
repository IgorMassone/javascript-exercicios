class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
        self.altura = 1  # Etapa 1

class BST:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if no is None:
            return 0
        return no.altura

    def atualizar_altura(self, no):
        altura_esquerda = self.altura(no.esquerda)
        altura_direita = self.altura(no.direita)
        no.altura = 1 + max(altura_esquerda, altura_direita)

    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, y):
        x = y.esquerda
        temp = x.direita
        x.direita = y
        y.esquerda = temp
        self.atualizar_altura(y)
        self.atualizar_altura(x)
        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        temp = y.esquerda
        y.esquerda = x
        x.direita = temp
        self.atualizar_altura(x)
        self.atualizar_altura(y)
        return y

    def inserir_recursivo(self, no, dado):
        if no is None:
            return No(dado)
        if dado < no.dado:
            no.esquerda = self.inserir_recursivo(no.esquerda, dado)
        elif dado > no.dado:
            no.direita = self.inserir_recursivo(no.direita, dado)
        else:
            return no  # Duplicatas não são inseridas

        self.atualizar_altura(no)
        fb = self.fator_balanceamento(no)

        # Caso LL
        if fb > 1 and dado < no.esquerda.dado:
            return self.rotacao_direita(no)
        # Caso RR
        if fb < -1 and dado > no.direita.dado:
            return self.rotacao_esquerda(no)
        # Caso LR
        if fb > 1 and dado > no.esquerda.dado:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)
        # Caso RL
        if fb < -1 and dado < no.direita.dado:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def inserir(self, dado):
        self.raiz = self.inserir_recursivo(self.raiz, dado)

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

    def minimo(self):
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.dado

    def maximo(self):
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.direita is not None:
            atual = atual.direita  
        return atual.dado

    def em_ordem(self, no):
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.dado, end=" ")
            self.em_ordem(no.direita)

    def remover(self, no, dado):
        if no is None:
            return None
            
        if dado < no.dado:
            no.esquerda = self.remover(no.esquerda, dado)
        elif dado > no.dado:
            no.direita = self.remover(no.direita, dado)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
                
            sucessor = no.direita
            while sucessor.esquerda is not None:
                sucessor = sucessor.esquerda
            
            no.dado = sucessor.dado
            no.direita = self.remover(no.direita, sucessor.dado)
            
        return no

    def mostrar(self, no, nivel=0):
        if no is None:
            return
        self.mostrar(no.direita, nivel + 1)
        print("    " * nivel + str(no.dado) + f" (h={no.altura}, FB={self.fator_balanceamento(no)})")
        self.mostrar(no.esquerda, nivel + 1)

    # ==========================================
    # ETAPA 12 — Validar toda a árvore
    # ==========================================
    def verificar_balanceamento(self, no):
        if no is None:
            return True
        fb = self.fator_balanceamento(no)
        if abs(fb) > 1:
            return False
        return (
            self.verificar_balanceamento(no.esquerda)
            and self.verificar_balanceamento(no.direita)
        )


# ==========================================
# TESTES, ETAPA 13 (Comparação BST vs AVL) E MENU
# ==========================================

# 1. Teste inicial com os valores propostos no tutorial
arvore = BST()
valores_iniciais = [
    61, 43, 77,
    16, 55, 69, 85,
    11, 31, 49, 59,
    65, 73, 81, 89
]
for valor in valores_iniciais:
    arvore.inserir(valor)

print("Em ordem (Árvore Principal):")
arvore.em_ordem(arvore.raiz)
print(f"\nA árvore está balanceada? {arvore.verificar_balanceamento(arvore.raiz)}")

# 2. ETAPA 13 — Comparar BST Convencional e AVL (Sequência de 1 a 100)
print("\n--- ETAPA 13: Comparação BST vs AVL (1 a 100) ---")

# Criando uma BST convencional puramente iterativa para simular o pior caso (degenerada em linha reta)
class BSTConvencional:
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
                return

bst_ruim = BSTConvencional()
avl_perfeita = BST()

for i in range(1, 101):
    bst_ruim.inserir(i)
    avl_perfeita.inserir(i)

print(f"Altura da BST Convencional com 100 elementos ordenados: {bst_ruim.raiz.altura if bst_ruim.raiz else 0} (vira uma lista ligada!)")
print(f"Altura da Árvore AVL com 100 elementos ordenados: {avl_perfeita.raiz.altura if avl_perfeita.raiz else 0} (garante log(n))")
print("--------------------------------------------------\n")


# --- MENU INTERATIVO ---
while True:
    print("\n=== MENU AVL ===")
    print("1 - Inserir valor")
    print("2 - Buscar valor")
    print("3 - Mostrar em ordem")
    print("4 - Mostrar menor valor")
    print("5 - Mostrar maior valor")
    print("6 - Remover valor")
    print("7 - Mostrar árvore visualmente (com Altura e FB)")
    print("8 - Verificar se a árvore está balanceada")
    print("9 - Encerrar")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        val = int(input("Digite um número: "))
        arvore.inserir(val)
        print(f"Valor {val} inserido e balanceado.")

    elif opcao == "2":
        val = int(input("Digite o valor para buscar: "))
        if arvore.buscar(val):
            print(f"Valor {val} existe na árvore.")
        else:
            print(f"O valor {val} não existe na árvore.")

    elif opcao == "3":
        print("Elementos em ordem: ")
        arvore.em_ordem(arvore.raiz)
        print()

    elif opcao == "4":
        menor = arvore.minimo()
        print(f"Menor valor: {menor if menor is not None else 'Árvore vazia'}")

    elif opcao == "5":
        maior = arvore.maximo()
        print(f"Maior valor: {maior if maior is not None else 'Árvore vazia'}")

    elif opcao == "6":
        val = int(input("Digite o valor a ser removido: "))
        if arvore.buscar(val):
            arvore.raiz = arvore.remover(arvore.raiz, val)
            print(f"Valor {val} removido.")
        else:
            print(f"Valor {val} não foi encontrado para remoção.")

    elif opcao == "7":
        print("\nVisualização da Árvore:")
        arvore.mostrar(arvore.raiz)

    elif opcao == "8":
        balanceada = arvore.verificar_balanceamento(arvore.raiz)
        print(f"Status de balanceamento da árvore: {'Válida (Balanceada)' if balanceada else 'Inválida (Desbalanceada)'}")

    elif opcao == "9":
        print("Encerrando o programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")