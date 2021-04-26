x = int(input("Digite um número inteiro: "))
y = int(input('Digite outro número inteiro: '))

s = x + y
sub = x - y
m = x * y
d = x / y
e = x ** y
di = x // y
r = x % y

print("Olá, os valores digitados foram {} e {}.".format(x, y))
print('A soma é {}, a subtração é {}, o produto é {} e a divisão é {} e a pontência tem resultado igual a {}.'.format(s, sub, m, d, e))
print('A divisão inteira é {} e o resto da divisão é {}.'.format(di, r))