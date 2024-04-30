class Pilha:
    def __init__(self, max):
        self.max = max
        self.n = 0
        self.palavras = []

def pilha_cria(max):
    pilha = Pilha(max)
    return pilha

def pilha_vazia(pilha):
    return pilha.n == 0

def pilha_pop(pilha):
    if pilha_vazia(pilha):
        print("Error - Pilha vazia!")
        return False
    top = pilha.palavras[pilha.n - 1]
    pilha.n = pilha.n - 1
    return top

def pilha_cheia(pilha):
    return pilha.n == pilha.max

def pilha_insere(pilha, v):
    if pilha_cheia(pilha):
        print("Pilha cheia!")
        return False
    pilha.palavras.insert(pilha.n, v)
    pilha.n = pilha.n + 1
    return pilha

def pilha_imprime(pilha):
    if not pilha.palavras:
        return
    for item in pilha.palavras:
        print("- ", item)

def verifica_pilha_palindromos(pilha):
    lista_palindromo = []
    while not pilha_vazia(pilha):
        palavra = pilha_pop(pilha)
        if palavra == palavra[::-1]:  # Verifica se a palavra é igual à sua inversa
            lista_palindromo.append(palavra)
    return lista_palindromo

def imprime_vetor(vetor):
    for palavra in vetor:
        print("Palavra: ", palavra, " é um políndromo!")

def main():
    p_palavra = pilha_cria(100)
    pilha_insere(p_palavra, "arara")
    pilha_insere(p_palavra, "cachorro")
    pilha_insere(p_palavra, "radar")
    pilha_insere(p_palavra, "areia")
    pilha_insere(p_palavra, "osso")
    pilha_imprime(p_palavra)
    lista_palindromo = verifica_pilha_palindromos(p_palavra)
    imprime_vetor(lista_palindromo)
main()