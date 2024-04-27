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

def combina_filas(f_res, f1, f2):
    while not fila_vazia(f1) and not fila_vazia(f2):
        v = fila_retira(f1)
        fila_insere(f_res, v)
        v = fila_retira(f2)
        fila_insere(f_res, v)
    return f_res
    
def fila_imprime(f):
    for i in range(f.n):
        print("- ", f.vet[(f.ini + i) % f.max])


def main():
    f1 = fila_cria(3)
    f2 = fila_cria(3)
    f_res = fila_cria(6)
    fila_insere(f1, 2.1)
    fila_insere(f1, 4.5)
    fila_insere(f1, 1.0)
    fila_insere(f2, 7.2)
    fila_insere(f2, 3.1)
    fila_insere(f2, 9.8)
    f_res = combina_filas(f_res, f1, f2)
    fila_imprime(f_res)
main()