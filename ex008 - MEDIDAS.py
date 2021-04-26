num = float(input('Digite um valor em metros: '))

cm = num * 100
mm = num * 1000

print('O valor de {}m é igual a {:.2f}cm e {:.2f}mm.'.format(num, cm, mm))
