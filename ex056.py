print('=' * 50)
print('\033[1;31mGRUPO DA MAIORIDADE\033[m'.center(60))
print('=' * 50)

#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media_idade = 0
maior = 0
menor = 0
for p in range(1, 5):
    print('======\033[1;31m {}º PESSOA \033[m======'.format(p))
    nome = str(input('Digite seu nome: ')).strip().upper()
    idade = int(input('Digite sua idade: '))
    media_idade += idade
    sexo = str(input('Digite seu sexo (F/M): ')).upper()
    if p == 1 and sexo == 'M':
        maior = idade
        nome_m = nome
    if idade > maior and sexo == 'M':
        maior = idade
        nome_m = nome
    if idade < 20 and sexo == 'F':
        menor += 1

media = media_idade / 4
print('A \033[1;31mMÉDIA\033[m entre as idades analisadas é \033[1;31m{}\033[m.'.format(media))
print('O homem mais velho é \033[1;31m{}\033[m com \033[1;31m{} ANOS\033[m.'.format(nome_m, maior))
print('Existe(m) \033[1;31m{} MULHER(ES)\033[m com \033[1;31mMENOS\033[m de \033[1;31m20 anos\033[m.'.format(menor))