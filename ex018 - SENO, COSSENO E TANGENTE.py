from math import (sin, cos, tan, radians )

angulo = float(input('Digite um ângulo qualquer: '))

sen = sin(radians(angulo))
cosseno = cos(radians(angulo))
tg = tan(radians(angulo))

print('O ângulo digitado foi {} seu seno é {:.2f}, seu\n '
      'cosseno é {:.2f} e a tangente é {:.2f}.'.format(angulo, sen, cosseno, tg))