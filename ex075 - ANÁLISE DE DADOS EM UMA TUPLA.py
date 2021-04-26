print('=' * 50)
print('\033[1;31mANÁLISE DE DADOS EM UMA TUPLA\033[m'.center(60))
print('=' * 50)

par = 0
valores = (int(input('Digite um número: ')), int(input('Digite um número: ')),
int(input('Digite um número: ')), int(input('Digite um número: ')))

print(f'O número 9 apareceu \033[1m{valores.count(9)} VEZE(S)\033[m.')
if 3 in valores:
    print(f'O número 3 apareceu na \033[1m{valores.index(3)+1}ª POSIÇÃO.\033[m')
else:
    print('O número 3 não foi digitado.')
for n in valores:
    if n % 2 == 0:
        par += 1
if par == 0:
    print('\033[1mNão foi digitado nenhum número PAR.\033[m')
elif par == 1:
    print(f'\033[1m{par} NÚMERO É PAR.\033[m')
else:
    print(f'\033[1m{par} NÚMERO SÃO PAR.\033[m')
