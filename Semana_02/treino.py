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

def lista_imprimi(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox


def main():
    lst = lista_cria()
    lst = lista_insere(lst, 10)
    lst = lista_insere(lst, 20)
    lst = lista_insere(lst, 30)

    lista_imprimi(lst)
main()