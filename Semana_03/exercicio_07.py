class Lista():
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def lista_cria():
    return None

def lista_insere(lst, valor):
    novo = Lista(valor)    
    if lst is None:
        novo.prox = novo
        return novo
    else:
        novo.prox = lst.prox
        lst.prox = novo
        return lst

def lista_imprime(lst):
    if lst is None:
        print("Lista vazia")
        return
    atual = lst
    while True:
        print(atual.info)
        atual = atual.prox
        if atual == lst:
            break

def lista_remove(lst, valor):
    if lst is None:
        return None
    anterior = None
    atual = lst
    while True:
        if atual.info == valor:
            if anterior is None: 
                if atual.prox == atual: 
                    return None
                else:  
                    lst = atual.prox
                    temp = atual
                    while temp.prox != atual:
                        temp = temp.prox
                    temp.prox = lst
            else:  
                anterior.prox = atual.prox
            return lst
        anterior = atual
        atual = atual.prox
        if atual == lst:  
            break
    return lst

def main():
    lst = lista_cria()
    lst = lista_insere(lst, 3)
    lst = lista_insere(lst, 2)
    lst = lista_insere(lst, 1)
    lst = lista_insere(lst, 10)
    lst = lista_insere(lst, 12)
    lst = lista_insere(lst, 13)
    lst = lista_remove(lst, 2)
    lst = lista_remove(lst, 1)
    lista_imprime(lst)
main()
