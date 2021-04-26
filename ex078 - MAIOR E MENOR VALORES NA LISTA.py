print('=' * 50)
print(f'\033[1;31m{"MAIOR E MENOR VALORES NA LISTA":^50}\033[m')
print('=' * 50)

valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input('Digite um número: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Os valores digitados foram: {valores}')
print(f'O MAIOR valor é {maior} nas posições: ', end='')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos+1}...', end='')
print()
print(f'O MENOR é {menor} nas posições: ', end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(f'{pos+1}...', end='')
print()
