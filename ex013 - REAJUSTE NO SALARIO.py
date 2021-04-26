sal = float(input('Digite o seu salário: R$ '))
reajuste = float(input('Digite o percentual de reajuste: '))

novo = sal + (sal * (reajuste/100))

print("Seu salário é de R$ {:.2f}, com o reajuste de {}% o seu salário"
      " passará a ser de R$ {:.2f}".format(sal, reajuste, novo))