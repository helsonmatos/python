lista_num = []
lista_par = []
lista_impar = []

while True:
    lista_num.append(int(input('Digite um número: ')))

    quer_continuar = str(input('Quer continuar? [S/N] '))
    
    if quer_continuar in 'nN':
        break
for i, v in enumerate(lista_num):
        if v % 2 == 0:
            lista_par.append(v)
        else:
            lista_impar.append(v)

print(f'A lista completa é {lista_num}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_impar}')