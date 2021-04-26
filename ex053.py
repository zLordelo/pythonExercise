print('=' * 50)
print('\033[1;31mDETECTOR DE PALÍNDROMOS\033[m'.center(60))
print('=' * 50)

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]
print('Você digitou a frase \033[1;31m{}\033[m o inverso dela é \033[1;31m{}\033[m'.format(frase, inverso), end=' ')
if inverso == juntar:
    print('ou seja, TEMOS um PALÍNDROMO.')
else:
    print('ou seja, NÃO temos um PALÍNDROMO.')
