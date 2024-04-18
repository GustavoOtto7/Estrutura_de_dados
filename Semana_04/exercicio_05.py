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
    palavra = ''.join(pilha.vet).lower().replace(" ", "")  # Convertendo para minúsculas e removendo espaços em branco
    n = 0
    n2 = len(palavra) - 1
    while n < n2:
        if palavra[n] != palavra[n2]:
            return False
        n += 1
        n2 -= 1
    return True

def pilha_imprime(pilha):
    for i in range(pilha.n):
        print(pilha.vet[i])
    return

def main():
    pilha = pilha_cria(15)   
    palavra = input("Digite uma palavra: ")
    pilha_push(pilha, palavra)
    resultado = verifica_palavra(pilha)
    if resultado:
        print("A palavra é um palíndromo.")
    else:
        print("A palavra não é um palíndromo.")
    pilha_imprime(pilha)
main()