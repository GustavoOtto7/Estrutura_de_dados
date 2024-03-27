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

def inverte(lst):
    resultado = Lista() 
    atual = lst
    print("Esse é o primeiro atual: ", atual.info)
    while atual is not None:
        print(atual.info)
        resultado.prox = Lista(atual.info)
        atual = atual.prox
    return resultado.prox


def main():
    lst = lista_cria()
    lst = lista_insere(lst, 9.8)
    lst = lista_insere(lst, 7.2)
    lst = lista_insere(lst, 1.0)
    lst = lista_insere(lst, 4.5)
    lst = lista_insere(lst, 2.1)
    lista_imprime(lst)
    print("-----")
    resultado = inverte(lst)
    print("-----")
    lista_imprime(resultado)
main()