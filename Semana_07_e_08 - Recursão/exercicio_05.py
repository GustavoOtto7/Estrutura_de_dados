def calcula_soma(x, y):
    if y == 0:
        return x
    x += 1
    return calcula_soma(x, y - 1)

def main():
    x = int(input("Digite o número: "))
    y = int(input("Digite outro número: "))
    print(calcula_soma(x, y))
main()