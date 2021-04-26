print('=' * 80)
km = float(input('Digite a distância da sua viagem em Km: '))

if km <= 200:
    print('A taxa cobrada é de R$ 0.50/Km, o valor total da sua viagem será de R$ {:.2f}.'.format(km * 0.50))
else:
    print('A taxa cobrada é de R$ 0.45/Km, o valor total da sua viagem será de R$ {:.2f}.'.format(km * 0.45))
print('=' * 80)