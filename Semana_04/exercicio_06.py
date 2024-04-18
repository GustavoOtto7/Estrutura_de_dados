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

def concatena_pilhas(pilha1, pilha2):
    while True:
        if pilha_vazia(pilha2):
            return False
        else:
            valor = pilha_pop(pilha2)
            pilha1.vet.insert(pilha1.n, valor)
            pilha1.n += 1   
            
# Olá professor, minha saída dos valores foi um pouco diferente, 
# pois, usei o pop para retirar o último valor e adicionar a lista
# achei que assim fosse mais inteligente de utilizar a pilha
# último a entrar, primeiro a ser adicionado na outra


def pilha_imprime(pilha):
    for i in range(pilha.n):
        print(pilha.vet[i])
    return

def main():
    pilha1 = pilha_cria(10)   
    pilha2 = pilha_cria(5)   
    pilha_push(pilha1, 1.0)
    pilha_push(pilha1, 4.5)
    pilha_push(pilha1, 2.1)
    pilha_push(pilha2, 9.8)
    pilha_push(pilha2, 3.1)
    pilha_push(pilha2, 7.2)
    pilha_imprime(pilha1)
    print("----")
    pilha_imprime(pilha2)
    print("Concatenando!")
    concatena_pilhas(pilha1, pilha2)
    print("Essa é a nova pilha 1: ")
    pilha_imprime(pilha1)
    print("----")
    print("Essa é a nova pilha 2: ")
    pilha_imprime(pilha2)
main()