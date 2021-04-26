print('=' * 40)
print('SITUAÇÃO POR MÉDIA')
print('=' * 40)

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('Sua média foi de {} e você está REPROVADO.'.format(media))
elif media >= 7:
    print('Sua média foi de {} e você está APROVADO.'.format(media))
else:
    print('Sua média foi de {} e você está em RECUPERAÇÃO.'.format(media))