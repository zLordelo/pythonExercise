print('=' * 50)
print(f'\033[1;31m{"APRIMORANDO OS DICIONÁRIOS":^50}\033[m')
print('=' * 50)
'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
time = list()
player = dict()
gols = list()

while True:
    gols.clear()
    player['nome'] = str(input('Nome do jogador: ')).upper()
    player['partidas'] = int(input('Partidas jogadas: '))
    if player['partidas'] > 0:
        for p in range(0, player['partidas']):
            gols.append(int(input(f'   Gols na {p+1}ª partida: ')))
    player['gols'] = gols[:]
    player['tot_gols'] = sum(gols)
    time.append(player.copy())
    print(f'Aproveitamento de {player["nome"]} cadastrado com sucesso!')
    while True:
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Digite apenas S ou N.')
    if resp == 'N':
        break

print('=' * 60)
print(f'\033[1;31m{"APROVEITAMENTO DOS JOGADORES":^50}\033[m')
print('=' * 60)
print(f'{"MAT.|":>5} {"NOME":<15} {"|GOLS":<30} {"|TOTAL":<5}')
for k, v in enumerate(time):
    print(f'{k:>5} {v["nome"]:<15} {str(v["gols"]):<30} {v["tot_gols"]:<5}')

while True:
    mostrar = int(input('Aproveitamento de qual jogador (-1 PARA CANCELAR): '))
    if mostrar < 0:
        break
    if mostrar >= len(time):
        print(f'ERRO. Não foi encontrado o jogador \033[1;31m{mostrar}\033[m')
    else:
        print('=' * 50)
        print(f'APROVEITAMENTO DO JOGADOR \033[1;31m{time[mostrar]["nome"]}\033[m: ')
        print(f'     {time[mostrar]["nome"]} jogou {time[mostrar]["partidas"]} partidas.')
        for p in range(0, time[mostrar]['partidas']):
            print(f'      Na {p+1}ª partida fez {time[mostrar]["gols"][p]} gols.')
        print(f'      Totalizando {time[mostrar]["tot_gols"]} gols.')
    print('=' * 50)
