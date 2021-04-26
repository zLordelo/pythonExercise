print('=' * 50)
print(f'\033[1;31m{"UM PRINT ESPECIAL":^50}\033[m')
print('=' * 50)
'''Exercício Python 097: Faça um programa que tenha uma função chamada 
escreva(), que receba um texto qualquer como parâmetro e mostre 
uma mensagem com tamanho adaptável.         '''

def escreva(texto):
    tam = len(texto) + 6
    print('=' * tam)
    print(f'{texto:^{tam}}')
    print('=' * tam)

txt = str(input('Digite uma frase: '))
escreva(txt)
