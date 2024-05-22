
def fibo(n1, n2, valor):
    if n1 == (valor - 1):
        return n1 + n2
    else:
        temp = n2
        n2 = n1 + n2
        n1 = temp
        return fibo(n1 + 1, n2, valor)

print(fibo(0, 1, 10))