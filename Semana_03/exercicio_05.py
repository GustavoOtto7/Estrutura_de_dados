class Lista():
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

def igual(l1, l2):
    atual1 = l1
    atual2 = l2
    while atual1 is not None and atual2 is not None:
        if atual1.info == atual2.info:
            print("Caracteres iguais!")
            atual1 = atual1.prox
            atual2 = atual2.prox
        else:
            print("Carateres distintos!")
            return
    print("A sua lista de caracteres era idêntica!")

def main():
    l1 = lista_cria()
    l2 = lista_cria()

    l1 = lista_insere(l1, "i")
    l1 = lista_insere(l1, "r")
    l1 = lista_insere(l1, "p")

    l2 = lista_insere(l2, "i")
    l2 = lista_insere(l2, "r")
    l2 = lista_insere(l2, "p")

    print("Lista 1:")
    lista_imprime(l1)
    print("\nLista 2:")
    lista_imprime(l2)
    print("-----")
    igual(l1, l2)
main()