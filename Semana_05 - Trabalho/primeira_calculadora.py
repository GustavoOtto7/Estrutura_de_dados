class Pilha:
    def __init__(self):
        self.n = 0
        self.prio = 0
        self.info = None
        self.vet = []

def pilha_cria():
    pilha = Pilha()
    return pilha

def pilha_vazia(pilha):
    return pilha.n == 0

def pilha_push(pilha, valor):
    pilha.vet.insert(pilha.n, valor)
    pilha.n += 1
    print("Push: ", valor)
    return pilha

def pilha_pop(pilha):
    if pilha_vazia(pilha):
        print("A pilha está vazia!")
        return False
    else:
        topo = pilha.vet[-1]
        pilha.n -= 1
        print("Pop: ", topo)
        return topo

def verificar_valor(valor, p1, p2):
    prioridade = {')': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    valor = valor.replace(" ", "")
    for elemento in valor:
        print(elemento)
        if elemento.isdigit():
            pilha_push(p1, elemento)
            p1.info = elemento
            p1.prio = 0
            #Fazer verificação de quantos dígitos 
        else:
            if pilha_vazia(p2) or elemento == "(":
                pilha_push(p2, elemento)
                p2.prio = prioridade[elemento]
                p2.info = elemento
            elif elemento in prioridade:
                while prioridade[p2.vet[-1]] >= prioridade[elemento]:
                    print("Primeiro While")
                    operador = pilha_pop(p2)
                    num2 = int(pilha_pop(p1))
                    num1 = int(pilha_pop(p1))
                    if operador == "+":
                        resultado = (num1 + num2) 
                    elif operador == "-":
                        resultado = (num1 - num2) 
                    elif operador == "*":
                        resultado = (num1 * num2) 
                    elif operador == "/":
                        resultado = (num1 / num2)
                    pilha_push(p1, resultado)
                    p1.info = resultado
                    p1.prio = 0
                    break
                pilha_push(p2, elemento)
                p2.prio = prioridade[elemento]
                p2.info = elemento

        print("p1 ", p1.info, "p2 ",p2.info)
        
    
    while not pilha_vazia(p2):
        print("Segundo While")
        num2 = int(pilha_pop(p1))
        num1 = int(pilha_pop(p1))
        operador = pilha_pop(p2)
        if operador == "+":
            resultado = (num1 + num2) 
        elif operador == "-":
            resultado = (num1 - num2) 
        elif operador == "*":
            resultado = (num1 * num2) 
        elif operador == "/":
            resultado = (num1 / num2) 
        print("Resultado:  ", resultado)
        pilha_push(p1, resultado)

    

def main():
    p_num = pilha_cria()
    p_ope = pilha_cria()
    valor = input("Digite a sua operação matemática: ")
    print(valor.replace(" ", ""))
    verificar_valor(valor, p_num, p_ope)





main()