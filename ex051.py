print('=' * 50)
print('''\033[1;31mPROGRESSÃO ARITMÉTICA - FOR\033[m'''.center(60))
print('''\033[1;31m10 TERMOS\033[m'''.center(60))
print('=' * 50)

first = int(input('Digite o primeiro termo da PA: '))
reason = int(input('Digite a razão da PA: '))
decimo = first + (10 - 1) * reason
print('=' * 10)
for c in range(first, decimo + reason, reason):
    print('{:2} ↓'.center(10).format(c))
print('=' * 10)