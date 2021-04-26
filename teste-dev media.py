'''Enunciado da questão:
Faça um algoritmo para ler um número que é um código de usuário.
Caso este código seja diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a mensagem "Usuário inválido!" e o sistema será encerrado.
Caso o código seja correto, deve ser lido outro valor que é a senha.
Se a senha estiver correta (a certa é 9999), deve ser exibida a mensagem "Acesso permitido".
Se a senha estiver incorreta deve ser exibida a mensagem "Senha incorreta", e também uma mensagem com as seguintes opções:
1 - tentar novamente
0 - encerrar sistema'''

user = 1234
password = 9999

while True:
    print('=' * 15)
    print(f'{"LOGIN":^15}')
    print('=' * 15)
    usuario = int(input('\033[1;34mUsuário:\033[m '))
    if usuario != user:
        print('\033[1;31mUsuário inválido!\033[m')
        break
    senha = int(input('\033[1;34mSenha:\033[m '))
    if senha == password:
        print('\033[1;32mAcesso permitido!\033[m')
        break
    else:
        print('\033[1;31mSenha incorreta!\033[m')
        while True:
            print('[ 1 ] tentar novamente'
                  '\n[ 0 ] encerrar sistema')
            opc = int(input('Digite uma opção: '))
            if opc == 1:
                senha = int(input('\033[1;34mSenha:\033[m '))
                if senha == password:
                    print('\033[1;32mAcesso permitido!\033[m')
                    break
                if senha != password:
                    print('\033[1;31mSenha incorreta!\033[m')
            if opc not in (1, 0):
                print('\033[1;31mOpção inválida!\033[m')
            if opc == 0:
                break
    if opc == 0 or senha == password:
        break