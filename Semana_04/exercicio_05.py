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

def verifica_palavra(pilha):
    palavra = pilha.vet[0]
    '''palavra = palavra.split(" ")
    words = palavra.split(" ")'''
    while palavra is True:
        n = 0
        n2 = 0
        if palavra[n] == palavra[n2 - 1]:
            n += 1
            n2 -= 1
        else:
            return print(False)
    return print(True)

def pilha_imprime(pilha):
    for i in range(pilha.n):
        print(pilha.vet[i])
    return

def main():
    pilha = pilha_cria(5)   
    palavra = input("Digite uma palavra: ")
    pilha_push(pilha, palavra)
    verifica_palavra(pilha)
    pilha_imprime(pilha)
main()