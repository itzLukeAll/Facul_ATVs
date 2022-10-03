idades = []
alturas = []
for i in range(1,6):
    print('%dº Pessoa' %i)
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))
    idades.append(idade)
    alturas.append(altura)

print('-----Ordem inversa-----')
print('Alturas')
print(alturas[::-1])
print('Idades')
print(idades[::-1])


