#num = int(input('Digite um número maior que 1: '))
#while n <= 9:
#    print(num)

from random import randint

num = int(input('Digite um numero inteiro entre 1 e 10: '))
soma = 0
numero_sorteado = randint(1,10)
print(numero_sorteado)
while num != numero_sorteado:
    soma = soma + numero_sorteado
    numero_sorteado = randint(1,10)
    print(numero_sorteado)
print('A soma é: ', soma)

