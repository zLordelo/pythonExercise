from time import sleep
times = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Santos',
         'Fluminense', 'Fortaleza', 'Palmeiras', 'Atlético-GO', 'Corinthians',
         'Grêmio', 'Sport Recife', 'Bahia', 'Ceará SC', 'Botafogo', 'Vasco da Gama',
         'Athletico-PR', 'Coritiba', 'Bragantino-SP', 'Goiás')

while True:
    print('=' * 50)
    print('\033[1;31mCLASSIFICAÇÃO BRASILEIRÃO OUT/2020\033[m'.center(60))
    print('=' * 50)
    print('''\033[1m[ 1 ] TOP 5 TIMES
[ 2 ] ÚLTIMOS 4 TIMES
[ 3 ] TIMES EM ORDEM ALFABÉTICA
[ 4 ] PESQUISAR POR TIME
[ 5 ] SAIR\033[m''')
    opção = int(input('Digite uma opção: '))
    print('=' * 50)
    if opção == 1:
        print('\033[1mOs 5 primeiros colocados são:\033[m')
        for pos in range(0, 5):
            print(f'{pos+1}ª posição → {times[pos]}')
    if opção == 2:
        print('\033[1mOs 4 últimos colocados são:\033[m')
        for pos in range(-4, 0):
            print(f'{pos+len(times)+1}ª Posição → {times[pos]}')
    if opção == 3:
        times = sorted(times)
        print('\033[1mOs times em ordem alfabética:\033[m')
        for ordem in range(0, len(times)):
            print(f'{times[ordem]}',end=' → ')
            if ordem in (4, 9, 14):
                print('')
            if ordem == 19:
                print('\033[1;31mFIM\033[m')
    if opção == 4:
        pesquisa = str(input('Qual time deseja saber a posição? ')).capitalize()
        if pesquisa not in times:
            print('O TIME PESQUISADO NÃO ESTA NA CLASSIFICAÇÃO ATUAL.')
        else:
            pos = times.index(pesquisa)+1
            print(f'O time pesquisado está na {pos}ª posição')
    if opção == 5:
        break
    sleep(2)
print('Espero que sua experiência tenha sido agradável.')
sleep(1)
print('\033[1;31mFINALIZANDO O PROGRAMA...\033[m')
sleep(0.5)