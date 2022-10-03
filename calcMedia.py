n1 = int(input('Digite a 1º Nota: '))
n2 = int(input('Digite a 2º Nota: '))
n3 = int(input('Digite a 3º Nota: '))

nota = (n1 + n2 + n3) / 3

if nota >= 7 and nota < 10:
    print('O aluno está aprovado!!!')
elif nota >= 10:
    print('Aluno aprovado com Distinção!!')
else:
    print('O aluno está reprovado!')