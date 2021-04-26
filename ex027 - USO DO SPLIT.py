nome = str(input('Digite seu nome: ')).strip()
n = nome.split()

print('=' * 80)
print('Olá {}, muito prazer em te conhecer!'.format(n[0]))
print('O seu primeiro nome é {}.'.format(n[0]))
print('O seu último nome é {}.'.format(n[-1]))
print('=' * 80)
