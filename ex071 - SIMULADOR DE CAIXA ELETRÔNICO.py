print('=' * 50)
print('\033[1;31mSIMULADOR DE CAIXA ELETRÔNICO\033[m'.center(60))
print('=' * 50)
valor = int(input('Quanto deseja sacar? '))
total = valor
cédula = 50
total_cédula = 0
while True:
    if total >= cédula:
        total -= cédula
        total_cédula += 1
    else:
        if total_cédula > 0:
            print(f'Total de {total_cédula} cédulas de R$ {cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_cédula = 0
        if total == 0:
            break