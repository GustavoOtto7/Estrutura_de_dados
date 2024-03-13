class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def cria_lista():
    return Lista()

def insere_lista(lst, valor):
    novo = Lista(valor)
    novo.prox = lst 
    return novo

def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox

lst = cria_lista()
lst = insere_lista(lst, 50)
lst = insere_lista(lst, 60)
lst = insere_lista(lst, 70)
lst = insere_lista(lst, 80)

lista_imprime(lst)