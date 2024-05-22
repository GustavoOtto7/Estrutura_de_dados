class Node:
    def __init__(self, val, esq=None, dire=None):
        self.val = val
        self.esq = esq
        self.dire = dire

    def __str__(self):
        return self.val

def print_node(node):
    print(node.val)

def pre_ordem(arv):
    # (print node), esq, dire
    if arv:
        print_node(arv)
        pre_ordem(arv.esq)
        pre_ordem(arv.dire)


def em_ordem(arv):
    # esq, (print node), dire
    if arv:
        em_ordem(arv.esq)
        print_node(arv)
        em_ordem(arv.dire)
                  
def pos_ordem(arv):
    # esq, dire, (print mode)
    if arv:
        pos_ordem(arv.esq)
        pos_ordem(arv.dire)
        print_node(arv)

def inverter_arv(arv):
    if arv:
        arv.esq, arv.dire = arv.dire, arv.esq
        inverter_arv(arv.esq)
        inverter_arv(arv.dire)

def altura(arv):
    if not arv:
        return -1
    return 1 + max(altura(arv.esq), altura(arv.dire))

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

a.esq = b
a.dire = c
b.esq = d
b.dire = e
c.esq = f

print("Percurso em pré-ordem")
pre_ordem(a)
print("Percurso em ordem")
em_ordem(a)
print("Percurso em pós-ordem")
pos_ordem(a)
print("____")
inverter_arv(a)
pre_ordem(a)
print("____")
print(altura(a))
'''
print("{} <-- {} --> {} ".format(n1.esq, n1, n1.dire))
print("{} <-- {} --> {} ".format(n2.esq, n2, n2.dire))
print("{} <-- {} --> {} ".format(n3.esq, n3, n3.dire))'''