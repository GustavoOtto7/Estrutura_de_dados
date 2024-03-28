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

def copia(lst):
    resultado = None
    ultima_copia = None
    atual = lst
    while atual is not None:
        novo_no = Lista(atual.info)
        if resultado is None:
            resultado = novo_no
        else:
            ultima_copia.prox = novo_no
        ultima_copia = novo_no
        atual = atual.prox
    return resultado

def main():
    lst = lista_cria()
    lst = lista_insere(lst, "u")
    lst = lista_insere(lst, "g")
    lst = lista_insere(lst, "&")
    lst = lista_insere(lst, "i")
    lst = lista_insere(lst, "r")
    lst = lista_insere(lst, "p")
    lista_imprime(lst)
    resultado = copia(lst)
    print("-----")
    lista_imprime(resultado)
main()