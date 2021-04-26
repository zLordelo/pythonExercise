print('='*60)
print('AVALIADOR DE EMPRÉSTIMO')
print('='*60)

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Digite o tempo que gostaria de pagar pelo emprestimo: '))
meses = anos*12
prestacao = casa / (anos * 12)
min = salario * 0.3

print('='*60)
print('RESULTADO')
print('='*60)
print('Para comprar uma casa de R$ {:.2f} em {} anos, é necessário pagar {} prestações de R$ {:.2f}.'.format(casa, anos, meses, prestacao))
if prestacao <= min:
    print('Empréstimo pode ser APROVADO!')
else:
    print('Empréstimo NEGADO!')
print('='*60)