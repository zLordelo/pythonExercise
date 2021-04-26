print('=' * 50)
print('\033[1;31mTRATANDO VÁRIOS NÚMEROS V1.0\033[m'.center(60))
print('=' * 50)

num = int(input('Digite um número [999 PARA SAIR]: '))
digitados = 0
soma = 0
while num != 999:
    digitados += 1
    soma += num
    num = int(input('Digite um número [999 PARA SAIR]: '))
print('Foram digitados {} números e a soma dos \nnúmeros digitados é igual a {}'.format(digitados, soma))
print('''Programa finalizado com sucesso!
Obridado pela atenção! \033[1;31m\U0001F5A4\033[m''')