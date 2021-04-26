print('=' * 80)
vel = float(input('Digite sua velocidade: '))

if vel > 80:
    multa = (vel-80) * 7
    print('Você foi multado!')
    print('Você excedeu o limite que é de 80Km/h. \n'
          'O valor da sua multa é de R$ {:.2f}.'.format(multa))
print('Exerça a cidadania, respeite as leis de transito!')
print('=' * 80)