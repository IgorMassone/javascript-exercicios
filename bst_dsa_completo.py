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
                return

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
            atual = depth = atual.direita
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

arvore = BST()
valores = [
61, 43, 77,
16, 55, 69, 85,
11, 31, 49, 59,
65, 73, 81, 89
]
for valor in valores:
    arvore.inserir(valor)

print("Em ordem:")
arvore.em_ordem(arvore.raiz)

print("\nMínimo:", arvore.minimo())
print("Máximo:", arvore.maximo())

print("Buscar 73:", arvore.buscar(73))
print("Buscar 100:", arvore.buscar(100))


# TAREFA

print("--- Árvore Iniciada com Sucesso ")

while True:
    print("\n=== MENU BST ===")
    print("1 - Inserir valor")
    print("2 - Buscar valor")
    print("3 - Mostrar em ordem")
    print("4 - Mostrar menor valor")
    print("5 - Mostrar maior valor")
    print("6 - Remover valor")
    print("7 - Encerrar")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        val = int(input("Digite um número: "))
        arvore.inserir(val)
        print(f"Valor {val} inserido")

    if opcao == "2":
        val = int(input("Digite o valor para buscar: "))
        if arvore.buscar(val):
            print(f"Valor {val} já existe na árvore")
        else:
            print(f"O valor {val} não existe na árvore")

    if opcao == "3":
        print("Elementos em ordem:  ")
        arvore.em_ordem(arvore.raiz)

    if opcao == "4":
        menor = arvore.minimo()
        print(f"Menor valor: {menor if menor is not None else 'Árvore vazia'}")

    if opcao == "5":
        maior = arvore.maximo()
        print(f"Maior valor: {maior if maior is not None else 'Árvore vazia'}")

    if opcao == "6":
        val = int(input("Digite o valor a ser removido"))
        if arvore.buscar(val):
            arvore.raiz = arvore.remover(arvore.raiz, val)
            print(f"Valor {val} removido")
        else:
            print(f"Valor {val} não foi encontrado para remoção")
    
    elif opcao == "7":
        print("Encerrando o programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")

