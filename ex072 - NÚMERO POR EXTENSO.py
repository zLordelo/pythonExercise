print('=' * 50)
print('\033[1;31mNÚMERO POR EXTENSO\033[m'.center(60))
print('=' * 50)

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
            'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
            'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if num <= 20 and num >= 0:
            break
    print(f'Você digitou o NÚMERO \033[1;31m{contagem[num].upper()}\033[m')
    while True:
        opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('\033[1;31mObrigado por utilizar!\033[m')