import random
jogo = random.randint(0, 5)

print('=' * 80)
print('ESTOU PENSANDO EM UM NUMÉRO ENTRE 0 E 5. TENTE DESCOBRIR QUAL É!')
print('=' * 80)

chute = int(input('Em qual número eu pensei? '))
if jogo == chute:
    print('YOU WIN!')
    print('PARABÉNS, VOCÊ ME VENCEU!')
else:
    print("GAME OVER!")
    print('PENSEI NO NÚMERO {}.\n'
          'NÃO FOI DESSA VEZ, TENTE NOVAMENTE!'.format(jogo))
print('=' * 80)