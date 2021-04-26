print('=' * 80)
print('BEM VINDO AO SUPORTE DE EXISTÊNCIA DE UM TRIÂNGULO'.center(80))
print('=' * 80)
a = float(input('Digite o comprimento da reta 1: '))
b = float(input('Digite o comprimento da reta 2: '))
c = float(input('Digite o comprimento da reta 3: '))

if a < b + c and b < a + c and c < a + b:
    print('Essas retas PODEM formar um triângulo.')
else:
    print('Essas retas NÃO PODEM formar um triângulo.')
print('=' * 80)