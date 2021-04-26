n = int(input('Digite um número de 0 a 9999: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10


print('O seu número tem \n'
      '{} unidades \n'
      '{} dezenas \n'
      '{} centenas \n'
      '{} milhares.'.format(u, d, c, m))