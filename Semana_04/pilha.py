class Pilha:
    def __init__(self, max):
        self.max = max
        self.n = 0
        self.vet = []

def pilha_cria(tam):
    p = Pilha(tam)
    p.n = 0
    return p

def pilha_push(p, v):
    if p.n == p.max:
        print("Error - Pilha cheia!")
        return False
    p.vet.insert(p.n, v)
    p.n = p.n + 1

def pilha_vazia(p):
    return p.n == 0

def pilha_pop(p):
    if pilha_vazia(p):
        print("Error: Pilha vazia!")
        return False
    topo = p.vet[p.n - 1]
    p.n = p.n - 1 
    return topo

def pilha_imprime(p):
    for i in p.vet:
        print(p[i])
    return 