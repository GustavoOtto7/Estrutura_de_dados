class Fila:
    def __init__(self, max):
        self.max = max
        self.n = 0
        self.ini = 0
        self.info = None
        self.vet = []

def fila_cria(max):
    f = Fila(max)
    f.n = 0
    f.ini = 0
    f.vet = []
    return f

def fila_cheia(f):
    return f.n == f.max

def fila_vazia(f):
    return f.n <= 0

def fila_insere(f, v):
    if fila_cheia(f):
        print("Fila cheia!")
        return False
    f.vet.insert(f.n, v)
    f.n = f.n + 1
    f.info = v
    return f

def fila_retira(f):
    if fila_vazia(f):
        print("Fila vazia!")
        return False
    v = f.vet[f.ini]
    f.vet = f.vet[1:]
    f.n -= 1
    return v 

def fila_frente(f):
    v = f.vet[f.ini]
    return v


def ordena_filas(f_res, f1, f2):
    while not fila_vazia(f1) and not fila_vazia(f2):
        if fila_frente(f1) <= fila_frente(f2):
            v = fila_retira(f1)
            fila_insere(f_res, v)
        elif fila_frente(f2) <= fila_frente(f1): 
            v = fila_retira(f2)
            fila_insere(f_res, v)
    while not fila_vazia(f1):
        v = fila_retira(f1)
        fila_insere(f_res, v)
    while not fila_vazia(f2):
        v = fila_retira(f2)
        fila_insere(f_res, v)
    return f_res
    
def fila_imprime(f):
    for i in range(f.n):
        print("- ", f.vet[(f.ini + i) % f.max])


def main():
    f1 = fila_cria(10)
    f2 = fila_cria(20)
    f_res = fila_cria(30)
    fila_insere(f1, 2)
    fila_insere(f1, 4)
    fila_insere(f1, 6)
    fila_insere(f1, 8)
    fila_insere(f1, 10)
    fila_insere(f2, 1)
    fila_insere(f2, 3)
    fila_insere(f2, 5)
    fila_insere(f2, 7)
    fila_insere(f2, 9)
    fila_insere(f2, 11)
    fila_insere(f2, 12)
    fila_insere(f2, 14)
    fila_insere(f2, 18)
    fila_insere(f2, 20)
    f_res = ordena_filas(f_res, f1, f2)
    fila_imprime(f_res)
main()