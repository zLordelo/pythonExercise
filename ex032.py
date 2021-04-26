from datetime import date
print('=' * 80)
ano = int(input('Para analisar o ano atual digite 0, caso contrario, digite um ano qualquer: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é um ano bissexto.'.format(ano))
else:
    print('O ano de {} não é um ano bissexto.'.format(ano))
print('=' * 80)