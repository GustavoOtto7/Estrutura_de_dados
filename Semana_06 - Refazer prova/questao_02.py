class Lista:
    def __init__(self, id, preco, qtd):
        self.id = id
        self.preco = preco
        self.qtd = qtd
        self.prox = None

class Fila:
    def __init__(self, max):
        self.max = max
        self.n = 0
        self.ini = 0
        self.produtos = []

def Lista_cria():
    return None

def Fila_cria(max):
    fila = Fila(max)
    return fila

def Lista_insere(lst, id, preco, qtd):
    novo = Lista(id, preco, qtd)
    novo.prox = lst 
    return novo

def fila_cheia(fila):
    return fila.n == fila.max

def fila_insere(fila, v):
    if fila_cheia(fila):
        print("Fila cheia!")
        return False
    fila.produtos.insert(fila.n, v)
    fila.n = fila.n + 1
    return fila

def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.preco)
        atual = atual.prox

def fila_imprime(fila):
    if not fila.produtos:
        return
    for item in fila.produtos:
        print("- ", item.preco)

def cria_fila_produtos(l1, l2):
    f1 = Fila_cria(100)
    atual1 = l1
    atual2 = l2
    while atual1 and atual2:
        if atual1.preco <= atual2.preco:
            fila_insere(f1, atual1)
            atual1 = atual1.prox
        else:
            fila_insere(f1, atual2)
            atual2 = atual2.prox
    while atual1:
        fila_insere(f1, atual1)
        atual1 = atual1.prox
    while atual2:
        fila_insere(f1, atual2)
        atual2 = atual2.prox
    return f1

def main():
    l1 = Lista_cria()
    l2 = Lista_cria()
    l1 = Lista_insere(l1, 1, 7, 1)
    l1 = Lista_insere(l1, 2, 6, 1)
    l1 = Lista_insere(l1, 3, 5, 1)
    l2 = Lista_insere(l2, 4, 4, 1)
    l2 = Lista_insere(l2, 5, 3, 1)
    l2 = Lista_insere(l2, 6, 2, 1)
    fila_produtos = cria_fila_produtos(l1, l2)
    print("Fila de produtos!")
    fila_imprime(fila_produtos)
main()