print('=' * 55)
print(f'\033[1;31m{"LISTA DE PREÇOS COM TUPLA":^55}\033[m')
print('=' * 55)

listagem = ('Lápis', 1.50,
            'Borracha', 1.00,
            'Caneta', 2.00,
            'Corretivo', 2.50,
            'Cola bastão', 3.00,
            'Caderno 10MAT', 15.00,
            'Agenda', 8.00,
            'Estojo', 5.00,
            'Classificador', 2.00)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<40}', end='')
    else:
        print(f' R$ {listagem[pos]:>7.2f}')
print('=' * 55)
