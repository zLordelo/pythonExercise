print('=' * 40)
print('CONVERSOR DE BASES NUMÉRICAS')
print('=' * 40)

num = int(input('Digite um número: '))
print('''Selecione em que base gostaria de converter o número digitado:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
op = int(input('Digite uma opção: '))

print('=' * 20)
print('RESULTADO')
print('=' * 20)

if op == 1:
    print('{} em BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} em OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} em HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')