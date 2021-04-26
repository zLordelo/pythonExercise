txt = str(input('Digite uma frase ou palavra: ')).upper().strip()

print('A letra A aparece {} vezes.'.format(txt.count('A'))) #COUNT - CONTARÁ QUANTAS X TEM A LETRA.
print('A primeira aparição é na {}ª posição.'.format(txt.find('A')+1)) # PROCURA A LETRA
print('A última aparição é na {}ª posição.'.format(txt.rfind('A')+1)) # PROCURAR A LETRA COMEÇANDO DA DIREITA

# ADICIONA + 1 A PESQUISA POIS COMEÇAMOS A CONTAR DE 1 E O PC DE 0.