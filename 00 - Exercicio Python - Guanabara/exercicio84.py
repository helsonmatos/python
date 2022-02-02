print('=+'*30)
nome_peso = []
princ = []
maior_peso = 0
menor_peso = 0
pessoa = []
while True:
    nome_peso.append(str(input('Nome: ')))
    nome_peso.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior_peso = menor_peso = nome_peso[1]
    else:
        if nome_peso[1] > maior_peso:
            maior_peso = nome_peso[1]
        elif nome_peso[1] < menor_peso:
            menor_peso = nome_peso[1]
    princ.append(nome_peso[:])
    nome_peso.clear()
    quer_continuar = str(input('Quer continuar? [S/N] '))
    if quer_continuar in 'nN':
        break

print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg. ', end=' ')
for p in princ:
    if p[1] == maior_peso:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor_peso}Kg. ', end=' ')
for p in princ:
    if p[1] == menor_peso:
        print(f'{p[0]}')
print('=+'*30)
