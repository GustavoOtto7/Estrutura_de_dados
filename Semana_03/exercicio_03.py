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

def merge(l1, l2):
    resultado = Lista()
    atual = resultado
    while l1 is not None and l2 is not None:
        atual.prox = Lista(l1.info)
        atual = atual.prox
        l1 = l1.prox

        atual.prox = Lista(l2.info)
        atual = atual.prox
        l2 = l2.prox
    return resultado.prox

def main():
    l1 = lista_cria()
    l2 = lista_cria()

    l1 = lista_insere(l1, 1.0)
    l1 = lista_insere(l1, 4.5)
    l1 = lista_insere(l1, 2.1)

    l2 = lista_insere(l2, 9.8)
    l2 = lista_insere(l2, 3.1)
    l2 = lista_insere(l2, 7.2)

    lista_imprime(l1)
    print("----")
    lista_imprime(l2)
    l3 = merge(l1, l2)
    print("----")
    lista_imprime(l3)    
main()