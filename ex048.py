print('=' * 50)
print('\033[1;31mSOMA DE ÍMPARES MULTIPLOS DE 3\033[m'.center(60))
print('=' * 50)
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c
print('A soma entre os \033[1;31m{}\033[m valores solicitados é igual a \033[1;31m{}\033[m.'.format(contador, soma))