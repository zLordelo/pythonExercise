from random import randint
from time import sleep

print('=' * 80)
print('\033[1;31mJOGO DA ADVINHAÇÃO v2.0\033[m'.center(90))
print('=' * 80)
sleep(0.5)
print('IREI PENSAR EM UM NÚMERO ENTRE 0 E 30 E VOCÊ TENTARÁ ADIVINHAR QUAL É.')
print('=' * 80)
sleep(0.5)

play = str(input('DESEJA JOGAR [S/N]? ')).strip().upper()[0]
while play not in ('SsNn'):
    play = str(input('\033[1;31mDIGITE S OU N\033[m. DESEJA JOGAR [S/N]? ')).strip().upper()[0]
if play in ('Ss'):
    sleep(1)
    print('\033[1;31mPENSANDO........\033[m')
    sleep(1)
    print('PRONTINHO!', end=' ')
    IA = randint(0, 30)
    cont = 1
    resp = int(input('Qual sua resposta? '))
    while resp != IA:
        if resp > IA:
            dica = 'MENOS'
        else:
            dica = 'MAIS'
        resp = int(input('\033[1;31m{}...\033[m\nQual sua resposta? '.format(dica)))
        cont += 1
    if cont == 1:
        print('Você acertou na {}ª tentativa. \033[1;31mPOXAAA NEM DEU PRA SE DIVERTIR, PARABÉNS!\033[m'.format(cont))
    elif cont <= 3:
        print('Você acertou na {}ª tentativa. \033[1;31mUAU QUE RÁPIDO, PARABÉNS!\033[m'.format(cont))
    elif cont <= 8:
        print('Você acertou na {}ª tentativa. \033[1;31mDEMOROU MAS CONSEGUIU NÉ HAHAHAHA.\033[m'.format(cont))
    else:
        print('Você acertou na {}ª tentativa. \033[1;31mNOSSA JÁ TAVA COM PENA KKKKKKKKKK!\033[m'.format(cont))
else:
    sleep(0.5)
    print('\033[1;31mCerto! Encerrando o GAME...\033[m')
    sleep(1)

print('\033[1;33mCRIADO POR JOÃO LORDELO\nESPERO QUE TENHA SE DIVERTIDO!\033[m')