print('=' * 40)
print('COMPARADOR DE NÚMEROS')
print('=' * 40)

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O PRIMEIRO número digitado é o maior.')
elif num2 > num1:
    print('O SEGUNDO número digitado é o maior.')
else:
    print('Não existe valor maior, pois os números são IGUAIS')