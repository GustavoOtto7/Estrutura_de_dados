class Pilha:
    def __init__(self, max):
        self.max = max
        self.n = 0
        self.vet = []

def pilha_cria(tam):
    pilha = Pilha(tam)
    pilha.n = 0
    return pilha

def pilha_push(pilha, valor):
    if pilha.n == pilha.max:
        print("Error - Pilha cheia!")
        return False
    pilha.vet.insert(pilha.n, valor)
    pilha.n = pilha.n + 1

def pilha_vazia(pilha):
    return pilha.n == 0

def pilha_pop(pilha):
    if pilha_vazia(pilha):
        print("Error - Pilha vazia!")
        return False
    top = pilha.vet[pilha.n - 1]
    pilha.n = pilha.n - 1
    return top

def pilha_imprime(pilha):
    for i in range(pilha.n):
        print(pilha.vet[i])
    return

def main():
    pilha = pilha_cria(5)
    """ Letra a)
    pilha_push(pilha, 4)
    pilha_push(pilha, 3)
    pilha_pop(pilha)
    pilha_push(pilha, 8)
    pilha_pop(pilha)"""

    """ letra b) 1.
    pilha_push(pilha, 3)
    pilha_pop(pilha)
    pilha_pop(pilha)
    pilha_push(pilha, 4)"""

    """ Letra b) 2.
    pilha_push(pilha, 1)
    pilha_pop(pilha)
    pilha_push(pilha, 2)
    pilha_push(pilha, 3)
    pilha_push(pilha, 4)
    pilha_push(pilha, 5)
    pilha_push(pilha, 6)
    pilha_push(pilha, 7)
    pilha_push(pilha, 8)"""
    pilha_imprime(pilha)
main()