print('=' * 50)
print(f'\033[1;31m{"MAIS SOBRE MATRIZ EM PYTHON":^50}\033[m')
print('=' * 50)
'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados. 
B) A soma dos valores da terceira coluna. 
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacolunatres = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    for v in matriz[1]:
        if v == 0:
            maior = v
        elif v > maior:
                maior = v
print('=' * 50)
print('\033[1mAQUI ESTA SUA MATRIZ\033[m')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=' * 50)
print(f'A SOMA dos valores PAR digitados é: {somapar}')
for l in range(0, 3):
    somacolunatres += matriz[l][2]
print(f'A SOMA dos valores da TERCEIRA COLUNA é: {somacolunatres}')
print(f'A MAIOR valor da SEGUNDA LINHA é: {maior}')