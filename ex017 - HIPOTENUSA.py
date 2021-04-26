import math

oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))

hip = math.hypot(oposto, adjacente)

print('O cateto oposto é {}, o cateto adjacente é {}, logo o '
      'comprimento da hipotenusa é igual a {:.2f}'.format(oposto, adjacente, hip))