print('=' * 50)
print('CALCULADORA DO ÍNDICE DE MASSA CORPORAL'.center(50))
print('=' * 50)

peso = float(input('\nDigite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura ** 2)

print('=' * 30)
print('RESULTADO'.center(30))
print('=' * 30)

print('\nSeu peso é {:.1f} Kg e sua altura {:.2f} m. Seu Índice de Massa Corporal é {:.1f}.'.format(peso, altura, imc))
if imc <= 18.5:
    print('Seu peso está ABAIXO DO NORMAL!')
elif imc <= 24.9:
    print('Seu peso é NORMAL!')
elif imc <= 29.9:
    print('Você está ACIMA DO PESO!')
elif imc <= 34.9:
    print('OBESIDADE GRAU I')
elif imc <= 39.9:
    print('OBESIDADE GRAU II')
else:
    print('OBESIDADE GRAU III')

print('\nLEMBRE-SE: Independente do seu desejo saiba que com força de vontade conseguira tudo!\n'
      'Se alimente bem e beba bastante água!')

