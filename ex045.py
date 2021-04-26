from random import randint
from time import sleep

print('=' * 50)
print('\033[1;31mGAME: PEDRA, PAPEL E TESOURA\033[m'.center(60))
print('=' * 50)
print('''\033[1mACHA QUE PODE ME VENCER?
Escolha uma das opções abaixo e tente a sorte.\033[m
\033[1;31m[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
print('=' * 50)

opcao = int(input('FAÇA SEU JOGO: '))

list = ['PEDRA', 'PAPEL', 'TESOURA']
ia = randint(0, 2)
print('=' * 50)
if opcao > 2:
    print('\033[1;31m[ERRO]\033[m Jogada inválida, tente novamente!')
else:
    print('PEDRA')
    sleep(1)
    print('PAPEL')
    sleep(1)
    print('TESOURA!!')
    sleep(1)
    player = list[opcao]
    print('''\nO COMPUTADOR JOGOU \033[1;31m{}\033[m
VOCÊ JOGOU \033[1;31m{}'''.format(list[ia], player))
    if opcao == ia:
        print('\033[1;31mEMPATE!\033[m')
    elif player == 0 and ia == 2 or player == 1 and ia == 0 \
            or player == 2 and ia == 1:
        print('\033[1mVOCÊ GANHOU!\033[m')
    else:
        print('\033[1;31mHAHA EU GANHEI!\033[m')
