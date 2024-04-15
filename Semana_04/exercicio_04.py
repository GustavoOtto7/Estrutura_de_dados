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

def esvazia(pilha):
    pilha.n = 0
    pilha.vet = []

def pilha_imprime(pilha):
    for i in range(pilha.n):
        print(pilha.vet[i])
    return

def main():
    pilha = pilha_cria(5)   
    pilha_push(pilha, 4)
    pilha_push(pilha, 3)
    pilha_push(pilha, 8)
    pilha_push(pilha, 14)
    pilha_imprime(pilha)
    print("----")
    esvazia(pilha)
    pilha_imprime(pilha)
    print("----")
main()