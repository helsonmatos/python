numeros = [[],[]]
valor = 0

for i in range(1,9):
    valor = int(input(f'Digite o {i}o. valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
print(f'Os valores pares são {numeros[0]}')
numeros[1].sort()
print(f'Os valores ímpares são {numeros[1]}')
