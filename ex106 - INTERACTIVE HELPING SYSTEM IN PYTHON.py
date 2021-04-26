print('=' * 50)
print(f'\033[1;31m{"INTERACTIVE HELPING SYSTEM IN PYTHON":^50}\033[m')
print('=' * 50)
'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar 
a palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''


def helping(txt):
    return help(txt)

while True:
    resp = str(input('\033[1;33mBuscar ajuda\033[m [FIM para interromper]: '))
    if resp.strip().upper() == 'FIM':

        break
    helping(resp)
print('\033[1;34mEsse foi o nosso SISTEMA DE AJUDA INTERATIVA')
print('Obrigado por utilizar, espero que tenha tido uma ótima experiência\033[m')