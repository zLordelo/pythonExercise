import datetime
year = datetime.datetime.now().year

print('=' * 40)
print('CLASSIFICAÇÃO DE ATLETAS')
print('=' * 40)

nasc = int(input('Ano de nascimento: '))
age = year - nasc
print('Seu ano de nascimento é {} e sua idade é {}.'.format(nasc, age))
if age <= 9:
    print('Categoria MIRIM')
elif age <= 14:
    print('Categoria INFANTIL')
elif age <= 19:
    print('Categoria JÚNIOR')
elif age <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')