def produto(n):
    if n == 1:
        return 1
    return n * produto(n - 1)

def main():
    n = int(input("Digite o número desejado:"))
    print(produto(n))
main()