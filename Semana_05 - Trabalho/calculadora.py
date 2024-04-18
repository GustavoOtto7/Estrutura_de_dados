class Pilha:
    def __init__(self):
        self.n = 0
        self.prio = 0
        self.info = None
        self.vet = []

def pilha_cria():
    pilha = Pilha()
    pilha.n = 0
    return pilha

def pilha_vazia(pilha):
    return pilha.n == 0

def verificar_valor(valor, p1, p2):
    prioridade = {')': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    valor = valor.replace(" ", "")
    for elemento in valor:
        print(elemento)
        if elemento.isdigit():
            p1.vet.insert(p1.n, elemento)
            p1.info = elemento
            p1.n += 1 #Fazer verificação de quantos dígitos 
        else:
            if pilha_vazia(p2):
                p2.vet.insert(p2.n, elemento)
                p2.prio = prioridade
                p2.info = elemento
                p2.n += 1
            elif elemento in prioridade:
                while p2 and p2.prio[-1] >= prioridade[elemento]:
                    operador = pilha_pop(p2)
                    num2 = pilha_pop(p1)
                    num1 = pilha_pop(p1)
                    if operador == "+":
                        resultado = (num1 + num2) 
                    elif operador == "-":
                        resultado = (num1 - num2) 
                    elif operador == "*":
                        resultado = (num1 * num2) 
                    elif operador == "/":
                        resultado = (num1 / num2)
                    p1.vet.insert(p1.n, resultado) 

                p2.vet.insert(p2.n, elemento)
                p2.prio = prioridade
                p2.info = elemento
                p2.n += 1

        print("p1 ", p1.info, "p2 ",p2.info)
    while p2:
        operador = pilha_pop(p2)
        num2 = pilha_pop(p1)
        num1 = pilha_pop(p1)
        if operador == "+":
            p1.vet.append(num1 + num2) 
        elif operador == "-":
            p1.vet.append(num1 - num2) 
        elif operador == "*":
            p1.vet.append(num1 * num2) 
        elif operador == "/":
            p1.vet.append(num1 / num2) 
    print("Resultado:  ", p1.info)

def pilha_pop(p):
    if pilha_vazia(p):
        print("A pilha está vazia!")
        return False
    else:
        topo = p.vet[p.n - 1]
        p.n -= 1
        return topo


def main():
    p_num = pilha_cria()
    p_ope = pilha_cria()
    valor = input("Digite a sua operação matemática: ")
    print(valor.replace(" ", ""))
    verificar_valor(valor, p_num, p_ope)





main()