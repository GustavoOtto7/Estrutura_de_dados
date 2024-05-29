class Node:
    def __init__(self, val, esq=None, dire=None):
        self.val = val
        self.esq = esq
        self.dire = dire

    def __str__(self):
        return self.val

def print_node(node):
    print(node.val)

def pre_ordem(arv):
    # (print node), esq, dire
    if arv:
        print_node(arv)
        pre_ordem(arv.esq)
        pre_ordem(arv.dire)


def em_ordem(arv):
    # esq, (print node), dire
    if arv:
        em_ordem(arv.esq)
        print_node(arv)
        em_ordem(arv.dire)
                  
def pos_ordem(arv):
    # esq, dire, (print mode)
    if arv:
        pos_ordem(arv.esq)
        pos_ordem(arv.dire)
        print_node(arv)

def insere(arv, key):
    if arv is None:
        return Node(key)
    #Se key for Menor que o nodo vai pra esquerda    
    if key < arv.val:
        arv.esq = insere(arv.esq, key)
    #Se key for Maior que o nodo vai pra direita    
    else: 
        arv.dire = insere(arv.dire, key)
    return arv
