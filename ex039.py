import datetime
# para data é necessário importar o datetime e
# usar o datetime.datetime.now() e o .year caso queira o ano
year = datetime.datetime.now().year

print('=' * 40)
print('ALISTAMENTO MILITAR')
print('=' * 40)

sex = input('Informe seu sexo (M/F): ')
if sex == 'F':
    print('Não é necessário o alistamento militar obrigatório.')
elif sex == 'M':
    nasc = int(input('Ano de nascimento: '))
    age = year - nasc
    print('Você nasceu em {} e tem {} anos.'.format(nasc, age))
    if age < 18:
        print('Ainda NÃO é preciso se alistar, faltam {} anos. Seu alistamento será em {}.'.format(18-age, year+(18-age)))
    elif age > 18:
        print('Seu alistamento está ATRASADO há {} anos. Seu alistamento deveria ser feito em {}.'.format(age-18, year-(age-18)))
    elif age == 18:
        print('ESTE É O ANO PARA SEU ALISTAMENTO!')
