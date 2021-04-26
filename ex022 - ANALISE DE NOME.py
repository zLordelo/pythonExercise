nome = str(input('Digite seu nome completo: ')).strip()
#jun = ''.join(div)

print('='*80)
print('LOADING...')
print('Seu nome é: {}.'.format(nome))
print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu nome tem {} letras.'.format(len(jun))

div = nome.split()
print('Seu primeiro nome é {} e contém {} letras.'.format(div[0], len(div[0])))
print('='*80)