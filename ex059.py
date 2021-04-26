from time import sleep

print('=' * 50)
print('\033[1;31mOPÇÕES COM NÚMEROS\033[m'.center(60))
print('=' * 50)

primeiro = int(input('Digite o 1º valor: '))
segundo = int(input('Digite o 2º valor: '))
opcao = 0
maior = 0
while opcao != 5:
    print('=========   \033[1;33mMENU\033[m   =========')
    print('''\033[1;33m[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA\033[m''')
    print('=' * 27)
    opcao = int(input('O que deseja fazer com os números? Digite uma opção: '))
    if opcao == 1:
        soma = primeiro + segundo
        print('A \033[1;31mSOMA\033[m entre {} e {} é igual a \033[1;31m{}\033[m.'.format(primeiro, segundo, soma))
    elif opcao == 2:
        multiplicar = primeiro * segundo
        print('A \033[1;31mMULTIPLICAÇÃO\033[m entre {} e {} é igual a \033[1;31m{}\033[m.'.format(primeiro, segundo, multiplicar))
    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print('Entre {} e {} o \033[1;31mMAIOR É {}\033[m.'.format(primeiro, segundo, maior))
    elif opcao == 4:
        print('=' * 27)
        print('Informe os números novamente.')
        primeiro = int(input('Digite o 1º valor: '))
        segundo = int(input('Digite o 2º valor: '))
    elif opcao == 5:
        print('\033[1;33mAgradeçemos pela sua atenção \033[1;31m\U0001F5A4\033[m')
        sleep(1)
    else:
        print('\033[1;31m[ERRO]\033[m OPÇÃO INVÁLIDA. TENTE NOVAMENTE')
    sleep(2.5)
print('\033[1;31mSAINDO DO PROGRAMA....\033[m ')
sleep(1)
print('\033[1;31m\nProcesso finalizado com sucesso\033[m ')