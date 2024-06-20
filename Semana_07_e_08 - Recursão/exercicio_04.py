# Opa sor, essa tive ajuda do Chat, pois não consegui entender
# Se era pra somar as funções e apresentrar, ou apenas o resultado
# da fração dessa soma total 

def s(n, d):
    if n == 1 and d == 1:
        return 1
    current_fraction = n / d
    if n < 1 or d < 1:
        return 0
    return current_fraction + s(n - 2, d - 1)

def main():
    n = 99
    d = 50
    result = s(n, d)
    print(f"Resultado da soma das frações: {result}")
main()