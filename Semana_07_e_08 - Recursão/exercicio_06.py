def busca_binaria(vet, v, inf, sup):
    if inf > sup:
        return False
    meio = (inf + sup) // 2
    if vet[meio] == v:
        return meio
    elif vet[meio] > v:
        return busca_binaria(vet, v, inf, meio - 1)
    else:
        return busca_binaria(vet, v, meio + 1, sup)

def main():
    vet = [1,2,3,4,5,6,7,8,9,10]
    v = int(input("Digite um número: "))   
    resultado = busca_binaria(vet, v, 0, len(vet) - 1)
    if resultado is not False:
        print(f"Elemento {v} encontrado na posição {resultado}.")
    else:
        print(f"Elemento {v} não encontrado no vetor.")
main()