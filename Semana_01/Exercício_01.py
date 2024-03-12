vetor = [12,2,3,4,5, 0]
mai = vetor[0]
men = vetor[0]

for i in range(len(vetor)):
    if vetor[i] > mai:
        mai = vetor[i]
    if vetor[i] < men:
        men = vetor[i]

print(f"Maior: {mai} --- Menor: {men}")