class Pilha: #Classe da Pilha utilizada com suas características
    def __init__(self):
        self.n = 0 
        self.prio = 0
        self.info = None
        self.vet = []

def pilha_cria(): #Função que cria e retorna uma pilha
    pilha = Pilha()
    return pilha

def pilha_vazia(pilha): #Função que faz a verificação se a pilha está vazia
    return pilha.n == 0

def pilha_push(pilha, valor): #Função que faz a inserção do valor na pilha
    pilha.vet.insert(pilha.n, valor)
    pilha.n = pilha.n + 1
    pilha.info = valor
    return pilha

def pilha_pop(pilha): #Função que retira o último elemento da pilha
    if pilha_vazia(pilha):
        print("A pilha está vazia!")
        return False
    else:
        topo = pilha.vet[pilha.n -1]
        pilha.n = pilha.n - 1
        return topo