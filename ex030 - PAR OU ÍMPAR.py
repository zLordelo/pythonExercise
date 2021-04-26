print('=' * 80)

num = int(input('Digite um número: '))
resultado = num % 2 #TODO NUM PAR DIVIDIDO POR 2 É IGUAL A ZERO E IMPAR IGUAL A 1.

if resultado == 0:
    print('O número digitado foi {} e ele é par.'.format(num))
else:
    print('O número digitado foi {} e ele é ímpar.'.format(num))

print('=' * 80)