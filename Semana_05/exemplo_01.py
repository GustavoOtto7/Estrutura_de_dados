class Fila:
    def __init__(self, max):
        self.max = max
        self.n = 0
        self.ini = 0
        self.vet = []

def fila_cria(max):
    f = Fila(max)
    f.n = 0
    f.ini = 0 #Não são necessárias essas linhas se o construtor foi criado corretamente
    return f 

def fila_insere(f, v):
    if fila_cheia(f):
        print("Fila cheia!")
        return False
    fim = (f.ini + f.n) % f.max
    f.vet.insert(fim, v) #tem que usar insert e não append
    f.n = f.n + 1
    return f

def fila_cheia(f):
    return f.n == f.max #verifica se o número de elementos é o mesmo que o máximo

def fila_vazia(f):
    if f.n == 0:
        return False

def lista_imprime(f):
    for i in f.vet:
        print("- ", i)

def fila_retira(f):
    if fila_vazia(f):
        print("Fila vazia!")
        return False
    elemento = f.vet[f.ini]
    f.ini = (f.ini + 1) % f.max
    f.n = f.n - 1
    return elemento 

def main():
    f = fila_cria(10)
    f = fila_insere(f, 1)
    f = fila_insere(f, 2)
    f = fila_insere(f, 3)
    f = fila_insere(f, 4)
    f = fila_insere(f, 5)
    lista_imprime(f)
    f = fila_retira(2)
    f = fila_retira(4)
    lista_imprime(f)
main()