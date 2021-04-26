print('=' * 80)
salario = float(input('Digite seu salário atual: '))

print('=' * 80)
if salario > 1250.00:
    aumento = salario * (10/100)
    print('O aumento do seu salário será de 10%, ou seja R$ {:.2f}, totalizando R$ {:.2f}.'.format(aumento, salario + aumento))
else:
    aumento = salario * (15/100)
    print('O aumento do seu salário será de 15%, ou seja R$ {:.2f}, totalizando R$ {:.2f}.'.format(aumento, salario + aumento))
print('=' * 80)