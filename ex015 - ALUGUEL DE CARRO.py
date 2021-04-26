dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Digite a quantidade de quilometros (Km) rodados? '))

total = (dias * 60) + (km * 0.15)

print('O carro foi alugado por {} dias e rodou {:.2f}Km. O valor total a pagar é de R$ {:.2f}.'.format(dias, km, total))