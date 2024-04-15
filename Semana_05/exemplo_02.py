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

def fila_cheia(f):
    return f.n == f.max #verifica se o número de elementos é o mesmo que o máximo

def fila_vazia(f):
    return f.n == 0

def lista_imprime(f):
    for i in f.vet:
        print("- ", i)

def fila_insere_inicio(f, v):
    if fila_cheia(f):
        print("Fila cheia!")
        return False
    novo_inicio = (f.ini - 1 + f.max) % f.max
    f.vet.insert(novo_inicio, v)
    f.ini = novo_inicio
    f.n = f.n + 1

def fila_insere_fim(f, v):
    if fila_cheia(f):
        print("Fila cheia!")
        return False
    fim = (f.ini + f.n) % f.max
    f.vet.insert(fim, v) #tem que usar insert e não append
    f.n = f.n + 1

def fila_retira_inicio(f):
    if fila_vazia(f):
        print('Fila vazia!')
        return False
    elemento = f.vet[f.ini]
    f.ini = (f.ini + 1) % f.max
    f.n = f.n -1
    return elemento

def fila_retira_fim(f):
    if fila_vazia(f):
        print("Fila vazia!")
        return False
    fim = (f.ini + f.n) % f.max
    elemento = f.vet[fim]
    f.n = f.n - 1
    return elemento

def main():
    f = fila_cria(5)
    fila_insere_inicio(f, 0)
    fila_insere_fim(f, 1)
    fila_insere_fim(f, 2)
    fila_insere_fim(f, 3)
    fila_insere_inicio(f, 4)
    elemento = fila_retira_inicio(f)
    elemento = fila_retira_fim(f)
    elemento = fila_retira_inicio(f)
    elemento = fila_retira_fim(f)
    elemento = fila_retira_fim(f)
    lista_imprime(f)
main()