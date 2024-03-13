class Aluno:   
    def __init__(self, nome, cpf, turma, sala):
        self.nome = nome
        self.cpf = cpf
        self.turma = turma
        self.sala = sala
    
    def imprime(self):
        print("{} - {} - {} - {}".format(self.nome, self.cpf, self.turma, self.sala))


a1 = Aluno("Gustavo", "047.411.980-73", "Sala_12", "3Sem") 
a2 = Aluno("Priscila", "047.876.980-43", "3Per", "Seg_10")
print(a1.nome)
print(a1.cpf)
print(a1.sala + "  " + a1.turma)
a1.imprime()