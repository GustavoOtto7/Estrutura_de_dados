class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def cria_lista():
    return None

def insere_lista(lst, valor):
    novo = Lista(valor)
    novo.prox = lst 
    return novo

def lista_vazia(lst):
    if lst is None:
        return False
    else:
        return True
    #return lst is none

def lista_busca(lst, valor):
    atual = lst
    while atual is not None:
        if atual.info == valor:
            return atual
        atual = atual.prox
    return False

def lista_retira(lst, valor):
    atual = lst
    while atual is not None:
        if atual.prox.info == valor:
            aux = atual.prox 
            atual.prox.prox.info = None
            aux.info = None
    return lst

def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox


def main():
    lst = cria_lista()
    print(lista_vazia(lst))
    lst = insere_lista(lst, 50)
    lst = insere_lista(lst, 60)
    lst = insere_lista(lst, 70)
    lst = insere_lista(lst, 80)
    lista_imprime(lst)
    busca = lista_busca(lst, 50)
    if busca:
        print("Achei: ", busca.info)
    else:
        print("Não achei!")
    lst = lista_retira(lst, 60)
    lista_imprime(lst)
main()