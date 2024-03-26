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

def separa(lst, n):
    atual = lst
    while atual is not None:
        if atual.info == n:
            lst2 = atual.prox 
            atual.prox = None
            #return lst, lst2
        atual = atual.prox 
    return lst, lst2        

def main():
    lst = lista_cria()
    lst = lista_insere(lst, 1)
    lst = lista_insere(lst, 12)
    lst = lista_insere(lst, 5)
    lst = lista_insere(lst, 17)
    lst = lista_insere(lst, 3)
    lista_imprime(lst)
    lst, lst2 = separa(lst, 5)
    print("------")
    lista_imprime(lst)
    print("------")
    lista_imprime(lst2)
main()