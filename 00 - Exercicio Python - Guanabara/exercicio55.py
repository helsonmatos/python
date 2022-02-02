maior_peso = 0
menor_peso = 0

for p in range(1,6):
    pessoa_peso = float(input(f'Peso da {p}° pessoa: '))
    if p == 1:
        maior_peso = pessoa_peso
        menor_peso = pessoa_peso

    else:
        if pessoa_peso > maior_peso:
            maior_peso = pessoa_peso
        elif pessoa_peso < menor_peso:
            menor_peso = pessoa_peso


print(f'O Maior peso lido foi de {maior_peso}Kg')
print(f'O Menor peso lido foi de {menor_peso}Kg')


