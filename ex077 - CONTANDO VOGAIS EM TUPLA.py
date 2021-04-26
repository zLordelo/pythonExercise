print('=' * 50)
print(f'\033[1;31m{"CONTANDO VOGAIS EM TUPLA":^50}\033[m')
print('=' * 50)
palavras = ('PYTHON', 'MELHOR', 'LINGUAGEM', 'PARA', 'PROGRAMAR', 'ACREDITE', 'EMVOCE')

for palavra in palavras:
    print(f'\nNa palavras {palavra} temos ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end=' ')
