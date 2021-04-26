print('=' * 50)
print('\033[1;31mESTATÍSTICAS EM PRODUTOS\033[m'.center(60))
print('=' * 50)

total = mais_mil = menor_preço = cont = 0
barato = ' '

while True:
    produto = str(input('Produto: ')).strip().upper()
    preço = float(input('Preço: R$ '))
    cont += 1
    if cont == 1 or preço < menor_preço:
        menor_preço = preço
        barato = produto
    total += preço
    if preço > 1000:
        mais_mil += 1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar [S/N]: ')).strip().upper()
    print('=' * 50)
    if opção == 'N':
        break
print(f'''Total da compra: R$ {total:.2f}
Produtos que custam mais que R$ 1000: {mais_mil}
Produto mais barato: {barato} [R$ {menor_preço:.2f}]''')