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
            print(f"O valor {valor} existe!")
            return
        atual = atual.prox
    print(f"O valor {valor} não pertence à lista!")

def lista_retira(lst, valor):
    anterior = None
    atual = lst 
    while atual is not None:
        if atual.info == valor:
            if anterior is not None:
                anterior.prox = atual.prox 
            else:
                lst = atual.prox
            print(f"O número {valor} foi retirado com sucesso!")            
            return lst 
        anterior = atual
        atual = atual.prox
    print(f"O número {valor} não existe para retirar!")
    return lst

def list_comprimento(lst):
    atual = lst
    soma = 0 
    while atual is not None:
        soma += 1
        atual = atual.prox
    print(f"Tamanho da lista: {soma}")

def maiores(lst, n):
    atual = lst
    list_maiores = []
    while atual is not None:
        if atual.info > n:
            list_maiores.append(atual.info)
        atual = atual.prox
    print(f"Números maiores que n - ({n}) -> {list_maiores}")

def ultimo(lst):
    atual = lst
    while atual is not None:
        if atual.prox == None:
            print(f"Este é o último elemento da lista -> {atual.info}")
        atual = atual.prox

def concatena(l1, l2): 
    atual = l1 
    while atual.prox is not None:
        atual = atual.prox
    atual.prox = l2
    atual = l1 
    print("Lista concatenada: ")
    while atual is not None:
        print(atual.info, end= " -> ")
        atual = atual.prox
    print()

def lista_insere_final(lst, valor):
    novo_num = Lista(valor)
    atual = lst
    while atual is not None:
        if atual.prox == None:
            atual.prox = novo_num
            return lst
        else:
            atual = atual.prox
    return lst

def lista_calcula_media(lst): 
    atual = lst
    soma_total = 0
    soma_len = 0
    while atual is not None:
        soma_total += atual.info
        soma_len += 1
        atual = atual.prox
    media = soma_total / soma_len
    print(f"A média dos valores foi: {media}")

def lista_altera(lst):
    atual = lst
    while atual is not None:
        atual.info = atual.info * -1
        atual = atual.prox
    return lst

def lista_retira_ant(lst, v):
    ant_ant = None
    anterior = None
    atual = lst 
    while atual is not None:
        if atual.info == v:
            if ant_ant is not None:
                ant_ant.prox = atual
                print(f"O número anterior ao {v} foi retirado com sucesso!")            
                return lst
            else:
                print("Não há número anterior para retirar")
        ant_ant = anterior
        anterior = atual
        atual = atual.prox
    return lst
 
def main():
    lst = lista_cria()
    l1 = lista_cria()
    l2 = lista_cria()
    print(lista_vazia(lst))
    lst = lista_insere(lst, 10)
    lst = lista_insere(lst, 20)
    lst = lista_insere(lst, 30)
    lst = lista_insere(lst, 40)
    lst = lista_insere(lst, 50)
    lst = lista_insere(lst, 60)
    lst = lista_insere(lst, 70)
    l1 = lista_insere(l1, 5)
    l1 = lista_insere(l1, 7)
    l1 = lista_insere(l1, 9)
    l2 = lista_insere(l2, 2)
    l2 = lista_insere(l2, 6)
    l2 = lista_insere(l2, 10)
    lista_imprime(lst)
    print(lista_vazia(lst))
    lista_busca(lst, 20)
    lista_busca(lst, 22)
    list_comprimento(lst)
    lst = lista_retira(lst, 20)
    lst = lista_retira(lst, 25)
    list_comprimento(lst)
    maiores(lst, 5)
    maiores(lst, 40)
    ultimo(lst)
    concatena(l1, l2)
    lst = lista_insere_final(lst, 1)
    lista_calcula_media(lst)
    #lst = lista_altera(lst)
    lst = lista_retira_ant(lst, 10)
    lista_imprime(lst)
main()