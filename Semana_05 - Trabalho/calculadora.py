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
    pilha.n = pilha.n + 1
    pilha.info = valor
    print("Push: ", valor)
    return pilha

def pilha_pop(pilha):
    if pilha_vazia(pilha):
        print("A pilha está vazia!")
        return False
    else:
        topo = pilha.vet[pilha.n -1]
        pilha.n = pilha.n - 1
        print("Pop: ", topo)
        return topo

def calcular(operador, num2, num1):
    if operador == "+":
        resultado = (num1 + num2) 
    elif operador == "-":
        resultado = (num1 - num2) 
    elif operador == "*":
        resultado = (num1 * num2) 
    elif operador == "/":
        if num2 == 0:
            raise ValueError("Erro - Divisão por zero!")
        else:
            resultado = (num1 / num2)
    return resultado            

def verificar_valor(valor, p1, p2):
    prioridade = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3, ')': 3}
    numero = ""
    valor = valor.replace(" ", "")
    i = 0
    while i < len(valor):
        elemento = valor[i]
        if elemento.isdigit():
            numero = elemento
            while i + 1 < len(valor) and valor[i + 1].isdigit():
                numero += valor[i + 1]
                i += 1
            pilha_push(p1, int(numero))
        else:
            if pilha_vazia(p2) or elemento == "(":
                pilha_push(p2, elemento)
                p2.prio = prioridade[elemento]
            
            
            elif elemento in ['*', '/', '+', '-']:
                while (not pilha_vazia(p2) and prioridade[p2.vet[-1]] > prioridade[elemento]):
                    print("Primeiro While")
                    print("111", p2.info)
                    if p2.info == "(":
                        break
                    else:
                        operador = pilha_pop(p2)
                        num2 = pilha_pop(p1)
                        num1 = pilha_pop(p1)
                        resultado = calcular(operador, num2, num1)
                        pilha_push(p1, resultado)    
                pilha_push(p2, elemento)
                p2.prio = prioridade[elemento] 
            elif elemento == ")":
                print("Parenteses While")
                while not pilha_vazia(p2) and p2.info != "(":
                    operador = pilha_pop(p2)
                    num2 = pilha_pop(p1)
                    num1 = pilha_pop(p1)
                    resultado = calcular(operador, num2, num1)
                    pilha_push(p1, resultado)
                    if pilha_pop(p2) == "(":
                        break
        print("p1 ", p1.info, "p2 ",p2.info)
        i += 1
    
    while not pilha_vazia(p2):
        print("Segundo While")
        num2 = pilha_pop(p1)
        num1 = pilha_pop(p1)
        operador = pilha_pop(p2)
        resultado = calcular(operador, num2, num1) 
        print("Resultado:  ", resultado)
        pilha_push(p1, resultado)
    print("Resultado final: ", p1.info)
    

def main():
    p_num = pilha_cria()
    p_ope = pilha_cria()
    valor = input("Digite a sua operação matemática: ")
    print(valor.replace(" ", ""))
    verificar_valor(valor, p_num, p_ope)





main()