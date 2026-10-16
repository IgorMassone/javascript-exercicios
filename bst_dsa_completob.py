class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
        self.altura = 1  # Etapa 1: Acrescentar a altura aos nós (inicia em 1 para folhas)


class BST:
    def __init__(self):
        self.raiz = None

    # Etapa 2: Consultar e atualizar a altura
    def altura(self, no):
        if no is None:
            return 0
        return no.altura

    def atualizar_altura(self, no):
        altura_esquerda = self.altura(no.esquerda)
        altura_direita = self.altura(no.direita)
        no.altura = 1 + max(altura_esquerda, altura_direita)

    # Etapa 3: Calcular o fator de balanceamento
    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    # Etapa 5: Rotação à direita
    def rotacao_direita(self, y):
        x = y.esquerda
        temp = x.direita
        x.direita = y
        y.esquerda = temp
        self.atualizar_altura(y)
        self.atualizar_altura(x)
        return x

    # Etapa 6: Rotação à esquerda
    def rotacao_esquerda(self, x):
        y = x.direita
        temp = y.esquerda
        y.esquerda = x
        x.direita = temp
        self.atualizar_altura(x)
        self.atualizar_altura(y)
        return y

    # Etapas 7, 8, 9 e 10: Inserção Recursiva com Balanceamento Automático (LL, RR, LR, RL)
    def inserir_recursivo(self, no, dado):
        # Inserção convencional da BST
        if no is None:
            return No(dado)
        if dado < no.dado:
            no.esquerda = self.inserir_recursivo(no.esquerda, dado)
        elif dado > no.dado:
            no.direita = self.inserir_recursivo(no.direita, dado)
        else:
            return no  # Duplicatas não são inseridas

        # Atualizar altura e verificar balanceamento (na volta da recursão)
        self.atualizar_altura(no)
        fb = self.fator_balanceamento(no)

        # Caso LL (Esquerda-Esquerda)
        if fb > 1 and dado < no.esquerda.dado:
            return self.rotacao_direita(no)
        
        # Caso RR (Direita-Direita)
        if fb < -1 and dado > no.direita.dado:
            return self.rotacao_esquerda(no)
        
        # Caso LR (Esquerda-Direita)
        if fb > 1 and dado > no.esquerda.dado:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)
        
        # Caso RL (Direita-Esquerda)
        if fb < -1 and dado < no.direita.dado:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def inserir(self, dado):
        self.raiz = self.inserir_recursivo(self.raiz, dado)

    # Métodos fundamentais mantidos da BST original (Etapa 15)
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
            atual = atual.direita  # Corrigido o erro de digitação do código base
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

    # Etapa 10: Visualizar a árvore estruturada com Altura e Fator de Balanceamento
    def mostrar(self, no, nivel=0):
        if no is None:
            return
        self.mostrar(no.direita, nivel + 1)
        print("    " * nivel + str(no.dado) + f" (h={no.altura}, FB={self.fator_balanceamento(no)})")
        self.mostrar(no.esquerda, nivel + 1)

    # Etapa 12: Validar toda a árvore
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
# EXECUÇÃO DAS ETAPAS DE TESTES E COMPARAÇÕES
# ==========================================

print("=== ETAPA 11: TESTES OBRIGATÓRIOS DOS 4 CASOS ===")

# Caso LL
arvore_ll = BST()
for v in [30, 20, 10]:
    arvore_ll.inserir(v)
print(f"Caso LL [30, 20, 10] -> Raiz: {arvore_ll.raiz.dado} (Esperado: 20)")

# Caso RR
arvore_rr = BST()
for v in [10, 20, 30]:
    arvore_rr.inserir(v)
print(f"Caso RR [10, 20, 30] -> Raiz: {arvore_rr.raiz.dado} (Esperado: 20)")

# Caso LR
arvore_lr = BST()
for v in [30, 10, 20]:
    arvore_lr.inserir(v)
print(f"Caso LR [30, 10, 20] -> Raiz: {arvore_lr.raiz.dado} (Esperado: 20)")

# Caso RL
arvore_rl = BST()
for v in [10, 30, 20]:
    arvore_rl.inserir(v)
print(f"Caso RL [10, 30, 20] -> Raiz: {arvore_rl.raiz.dado} (Esperado: 20)")

print("\n--- Teste da Estrutura Completa [10, 20, 30, 40, 50, 25] ---")
arvore_teste = BST()
for valor in [10, 20, 30, 40, 50, 25]:
    arvore_teste.inserir(valor)
print(f"Raiz esperada: 30 | Raiz atual: {arvore_teste.raiz.dado}")
print(f"Altura total: {arvore_teste.raiz.altura} (Esperado: 3)")
print("Percurso em ordem: ", end="")
arvore_teste.em_ordem(arvore_teste.raiz)
print("\n")


# Etapa 13 — Comparar BST Convencional e AVL (Sequência 1 a 100)
print("--- ETAPA 13: Comparação BST Convencional vs AVL (1 a 100) ---")

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

print(f"Altura da BST Convencional (Degenerada): {bst_ruim.raiz.altura if bst_ruim.raiz else 0}")
print(f"Altura da Árvore AVL (Auto-balanceada): {avl_perfeita.raiz.altura if avl_perfeita.raiz else 0}")
print("--------------------------------------------------\n")


# ==========================================
# ÁRVORE PRINCIPAL E MENU INTERATIVO (TAREFA)
# ==========================================

arvore = BST()
valores_iniciais = [
    61, 43, 77,
    16, 55, 69, 85,
    11, 31, 49, 59,
    65, 73, 81, 89
]
for valor in valores_iniciais:
    arvore.inserir(valor)

print("--- Árvore Principal Iniciada com Sucesso ---")

while True:
    print("\n=== MENU AVL ===")
    print("1 - Inserir valor")
    print("2 - Buscar valor")
    print("3 - Mostrar em ordem")
    print("4 - Mostrar menor valor")
    print("5 - Mostrar maior valor")
    print("6 - Remover valor")
    print("7 - Mostrar árvore visualmente (Alturas e FB)")
    print("8 - Verificar balanceamento global")
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
        valida = arvore.verificar_balanceamento(arvore.raiz)
        print(f"Árvore 100% balanceada e válida? {valida}")

    elif opcao == "9":
        print("Encerrando o programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")