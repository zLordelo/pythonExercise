print('=' * 50)
print('\033[1;31mVÁRIOS NÚMEROS COM FLAG\033[m'.center(60))
print('=' * 50)

cont = soma = 0

while True:
    num = int(input('Digite um número \033[1;31m[999 PARA PARAR]\033[m: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números e a soma é igual a {soma}.')