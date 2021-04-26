print('=' * 50)
print('\033[1;31mGERENCIADOR DE PAGAMENTOS\033[m'.center(60))
print('=' * 50)

total = float(input('Preço total das compras: R$ '))

print('=' * 25)
print('\033[1;31mFORMAS DE PAGAMENTO\033[m'.center(15))
print('=' * 25)

print('''\033[1m[ 1 ] Á VISTA (DINHEIRO) / CHEQUE
[ 2 ] Á VISTA (CARTÃO)
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO\033[m''')
print('=' * 25)

opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    total1 = total - (total * (10/100))
    print('\nO total da sua compra é de R$ {:.2f}, pagando \033[1;31mÁ VISTA EM DINHEIRO\033[m receberá 10% de desconto e pagará somente \033[1;31mR$ {:.2f}\033[m.'.format(total, total1))
elif opcao == 2:
    total2 = total - (total * (5/100))
    print('\nO total da sua compra é de R$ {:.2f}, pagando \033[1;31mÁ VISTA NO CARTÃO\033[m receberá 5% de desconto e pagará somente \033[1;31mR$ {:.2f}\033[m.'.format(total, total2))
elif opcao == 3:
    parc = total / 2
    print('\nO total da sua compra é de R$ {:.2f}, pagando em \033[1;31m2X NO CARTÃO\033[m você pagará 2 parcelas de \033[1;31mR$ {:.2f} SEM JUROS\033[m.'.format(total, parc))
elif opcao == 4:
    parc = int(input('Quantas parcelas? '))
    if parc < 3:
        print('\033[1;31m[ERRO]\033[m A quantidade de parcelar deve ser 3 ou mais. Tente novamente!')
    else:
        total4 = total + (total * (20/100))
        v_parc = total4 / parc
        print('\nO total da sua compra é de R$ {:.2f}, pagando em \033[1;31m3X OU MAIS NO CARTÃO\033[m é cobrado \033[1m20% DE JUROS\033[m.'
              '\nVocê pagará em \033[1;31m{} PARCELAS de R${:.2f}\033[m totalizando \033[1;31mR$ {:.2f}\033[m.'.format(total, parc, v_parc, total4))
else:
    print('\033[1;31m[ERRO]\033[m Opção inválida. Tente novamente!')