print('=' * 50)
print('\033[1;31mMAIOR E MENOR PESO\033[m'.center(60))
print('=' * 50)

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite peso(Kg) da {}º pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('''O \033[1mMAIOR\033[m peso registrado foi \033[1m{}Kg\033[m
e o \033[1mMENOR\033[m peso \033[1m{}Kg\033[m'''.format(maior, menor))