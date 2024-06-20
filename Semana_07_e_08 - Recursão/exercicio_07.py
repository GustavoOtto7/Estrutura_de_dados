def binario(x):
    if x == 0:
        return ""
    else:
        quociente = x // 2
        resto = x % 2
        return binario(quociente) + str(resto)

def main():
    numero = int(input("Digite o número desejado:  "))
    if numero == 0:
        print("0")
    else:
        representacao_binaria = binario(numero)
        print((f"Este é o número em forma binária: {representacao_binaria}"))
main()