class Fila:
    def __init__(self, max):
        self.max = max
        self.n = 0
        self.ini = 0
        self.vet = []

class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def fila_cria(max):
    f = Fila(max)
    f.n = 0
    f.ini = 0
    f.vet = []
    return f

def lista_cria():
    return None

def fila_insere(f, v):
    if fila_cheia(f):
        print("Fila cheia!")
        return False
    fim = (f.ini + f.n) % f.max
    f.vet.insert(fim, v)
    f.n = f.n + 1
    return f

def lista_insere(l, v):
    novo = Lista(v)
    if l is None:
        return novo
    else:
        atual = l
        while atual.prox is not None:
            atual = atual.prox 
        atual.prox = novo    
    return l if l is not None else novo

def fila_cheia(f):
    return f.n == f.max

def fila_imprime(f):
    for i in f.vet:
        print("- ", i)

def lista_imprime(l):
    atual = l
    while atual is not None:
        print("- ", atual.info)
        atual = atual.prox 

def main():
    f = fila_cria(10)
    fila_insere(f, 1)
    fila_insere(f, 2)
    fila_insere(f, 3)
    fila_insere(f, 4)
    fila_insere(f, 5)
    fila_imprime(f)
########
    print("++++++")
    l = lista_cria()
    l = lista_insere(l, 10)
    l = lista_insere(l, 20)
    l = lista_insere(l, 30)
    l = lista_insere(l, 40)
    lista_imprime(l)
main()