def potencia(x, n):
    if n == 1:
        return x
    return x * potencia(x, n - 1)

def main():
    x = int(input("Digite o valor da base: "))
    n = int(input("Digite o valor da potência: "))
    print(potencia(x, n))
main()