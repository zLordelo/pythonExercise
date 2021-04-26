prod = float(input('Digite o valor do produto: '))

desc = prod - (prod * 0.05)
econ = prod * 0.05

print('O valor do seu produto é R$ {:.2f}, com o desconto de 5% o preço do seu produto será de R$ {:.2f}.\n'
      'Você economizou o valor de R$ {}'.format(prod, desc, econ))