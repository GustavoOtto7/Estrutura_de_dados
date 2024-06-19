def imprimir(min, max):
    if max - 1 == min:
        return min
    print(max - 1)
    return imprimir(min, max - 1)

def main():
    min =  int(input("Digite o valor mínimo: "))
    max =  int(input("Digite o valor máximo: "))
    imprimir(min, max)
main()