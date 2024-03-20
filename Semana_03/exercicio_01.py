class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def lista_cria():
    return None

def lista_insere(lst, valor):
    novo = Lista(valor)
    novo.prox = lst 
    return novo

def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox

def retira_n(lst, n):
    atual = lst
    anterior = None
    while atual is not None:
        if atual.info == n:
            if anterior is not None:
                anterior = atual.prox 
                print(f"O número {n} foi retirado!")
                return lst
        anterior = atual
        atual = atual.prox
    return lst


def main():
    lst = lista_cria()
    lst = lista_insere(lst, 10)
    lst = lista_insere(lst, 20)
    lst = lista_insere(lst, 30)
    lst = lista_insere(lst, 40)
    lst = lista_insere(lst, 30)
    lst = lista_insere(lst, 20)
    lst = lista_insere(lst, 10)
    lista_imprime(lst)
    retira_n(lst, 10)


main()    