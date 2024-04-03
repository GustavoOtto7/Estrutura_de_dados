from pilha import *

if __name__ == "__main__":
    print("Criando pilha!")
    p = pilha_cria(4)
    print("Pilha vazia? ", pilha_vazia(p))
    pilha_push(p, 1)
    print("Pilha vazia? ", pilha_vazia(p))
    pilha_push(p, 2)
    pilha_push(p, 3)
    pilha_push(p, 4)
    pilha_push(p, 5)
    pilha_vazia(p)
    print("Pop: ", pilha_pop(p))
    print("Pop: ", pilha_pop(p))
    print("Pop: ", pilha_pop(p))
    print("Pop: ", pilha_pop(p))
    print("Pilha vazia? ", pilha_vazia(p))
    print("Pop: ", pilha_pop(p))
