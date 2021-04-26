print('=' * 50)
print('\033[1;31mSOMA DOS PARES\033[m'.center(50))
print('=' * 50)
soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0 and num != 0:
        soma += num
        cont += 1
print('Encontrei \033[1;31m{}\033[m número(s) PARES e a soma é de \033[1;31m{}\033[m'.format(cont, soma))
