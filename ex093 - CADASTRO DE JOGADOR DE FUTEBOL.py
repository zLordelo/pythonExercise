print('=' * 50)
print(f'\033[1;31m{"CADASTRO DE JOGADOR DE FUTEBOL":^50}\033[m')
print('=' * 50)
'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
player = {} #dict()
partidas = [] #list()
player['nome'] = str(input('Nome do jogador: '))
player['partidas'] = int(input(f'Quantas partidas {player["nome"]} jogou: '))
for p in range(0, player['partidas']):
    gols = int(input(f'Quantos gols {player["nome"]} fez na {p+1}ª partida: '))
    partidas.append(gols)
player['gols'] = partidas[:]
player['total_gols'] = sum(partidas)
print('=' * 50)
print(player)
print('=' * 50)
for k, v in player.items():
    print(f'{k}: {v}')
print('=' * 50)
print('\033[1;31mAPROVEITAMENTO DO JOGADOR\033[m')
print()
print(f'\033[1mJogador:\033[m {player["nome"]}')
print(f'\033[1mPartidas jogadas\033[m: {player["partidas"]}')
print(f'\033[1mGols por partidas\033[m: {player["gols"]}')
print(f'\033[1mTotal de gols\033[m: {player["total_gols"]}')
print('=' * 50)
