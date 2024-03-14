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

def lista_vazia(lst):
    if lst is None:
      #  print("A lista está vazia!")
        return False
    else:
      #  print("A lista possui elementos!")
        return True
    
def lista_busca(lst, valor):
    atual = lst 
    while atual is not None:
        if atual.info == valor:
            print("O valor existe!")
            return
        atual = atual.prox
    print("O valor não pertence à lista!")

def lista_retira(lst, valor):
    atual = lst
    while atual is not None:
        if atual.info == valor:
            aux = atual.prox
            atual = None
            aux.prox = None
            print("Deu bom!")
            print(lst)
            return
        atual = atual.prox
    print("O número não existe para retirar!")



def main():
    lst = lista_cria()
    #print(lista_vazia(lst))
    lst = lista_insere(lst, 10)
    lst = lista_insere(lst, 20)
    lst = lista_insere(lst, 30)
    lista_imprime(lst)
    #print(lista_vazia(lst))
    #lista_busca(lst, 20)
    #lista_busca(lst, 22)
    lst = lista_retira(lst, 20)
    #lst = lista_retira(lst, 25)
    lista_imprime(lst)

main()