def reverso(n):
    return str(n[::-1])

n = str(input('Digite um número: ')).strip()
print(f'Reverso: {reverso(n)}')