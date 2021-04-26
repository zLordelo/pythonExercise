from random import randint
print('=' * 50)
print('\033[1;31mMAIOR E MENOR VALOR EM TUPLAS\033[m'.center(60))
print('=' * 50)

num = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print('Os números sorteados são: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO menor número é: {max(num)}')
print(f'O maior número é: {min(num)}')
