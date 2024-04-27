from ferramentas_pilha import *

def calcular(operador, num2, num1): #Função que faz a operação matemática e dá return no resultado
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

def verificar_valor(valor, p1, p2): #Função que faz a verificação do valor, analisando as precedências e prioridades, e, calculando se necessário.
    prioridade = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3, ')': 3}
    numero = ""
    valor = valor.replace(" ", "")
    i = 0
    while i < len(valor):
        elemento = valor[i]
        if elemento.isdigit():
            numero = elemento
            while i + 1 < len(valor) and valor[i + 1].isdigit(): #Verificação para números com mais de um dígito serem inseridos corretamente.
                numero += valor[i + 1]
                i += 1
            pilha_push(p1, int(numero))
        else:
            if pilha_vazia(p2) or elemento == "(": #Apenas insere o operador na pilha de operadores
                pilha_push(p2, elemento)
                p2.prio = prioridade[elemento]
            elif elemento in ['*', '/', '+', '-']: #Faz a verificação de prioridades
                while (not pilha_vazia(p2) and prioridade[p2.vet[-1]] > prioridade[elemento]):
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
            elif elemento == ")": #Quando encontrado o ")" é resolvido as operações até se encontrar o "("
                while not pilha_vazia(p2) and p2.info != "(":
                    operador = pilha_pop(p2)
                    num2 = pilha_pop(p1)
                    num1 = pilha_pop(p1)
                    resultado = calcular(operador, num2, num1)
                    pilha_push(p1, resultado)
                    if pilha_pop(p2) == "(":
                        break
        i += 1
    while not pilha_vazia(p2): #Por fim, realiza as operações que ainda restaram.
        num2 = pilha_pop(p1)
        num1 = pilha_pop(p1)
        operador = pilha_pop(p2)
        resultado = calcular(operador, num2, num1) 
        pilha_push(p1, resultado)
    print("Resultado final: ", p1.info)