from calculadora import *

def main():
    p_num = pilha_cria()
    p_ope = pilha_cria()
    valor = input("Digite a sua operação matemática: ")
    verificar_valor(valor, p_num, p_ope)
main()