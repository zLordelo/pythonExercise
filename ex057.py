print('=' * 50)
print('\033[1;31mValidação de dados\033[m'.upper().center(60))
print('=' * 50)


sexo = str(input('Digite seu sexo [M / F]: ')).strip().upper()[0]
while sexo not in ('MmFf'):
    sexo = str(input('\033[1;31m[ERRO] Sexo inválido, digite apenas opções sugeridas!\033[m\nDigite seu sexo [M / F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))