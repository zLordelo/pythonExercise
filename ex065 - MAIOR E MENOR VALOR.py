print('=' * 50)
print('\033[1;31mMAIOR E MENOR VALOR\033[m'.center(60))
print('=' * 50)

opcao = 'S'
digitados = soma_total = maior = menor = 0
while opcao not in '(Nn)':
    num = int(input('Digite um número: '))
    soma_total += num
    digitados += 1
    media = soma_total / digitados
    if digitados == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
print('''Você digitou \033[1;31m{} NÚMEROS\033[m. 
A \033[1;31mSOMA\033[m é igual a \033[1;31m{}\033[m. 
A \033[1;31mMÉDIA\033[m é igual a \033[1;31m{:.2f}\033[m.
O \033[1;31mMAIOR\033[m valor foi \033[1;31m{}\033[m e o \033[1;31mMENOR\033[m foi \033[1;31m{}\033[m.'''
.format(digitados, soma_total, media, maior, menor))
