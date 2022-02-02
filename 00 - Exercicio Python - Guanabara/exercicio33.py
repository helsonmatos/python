valor_1 = int(input('Primeiro valor: '))
valor_2 = int(input('Segundo valor: '))
valor_3 = int(input('Terceiro valor: '))

lista = [valor_1,valor_2,valor_3]

if lista[0] < lista[1] and lista[0] < lista[2]:
    menor_valor = lista[0] 
else:
    maior_valor = lista[0]

if lista[1] < lista[2] and lista[1] < lista[0]:
    menor_valor = lista[1] 
else:
    maior_valor = lista[1]

if lista[2] < lista[1] and lista[2] < lista[0]:
    menor_valor = lista[1]
else:
    maior_valor = lista[1]

print(f'\033[35mO menor valor é {menor_valor}')
print(f'\033[35mO maior valor é {maior_valor}')
    