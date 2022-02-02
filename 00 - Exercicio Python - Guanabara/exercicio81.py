print('+='*25)
lista_num = []
while True:
    valor = int(input('Digite um valor: '))
    quer_continuar = str(input('Quer continuar? [S/N] '))
    lista_num.append(valor)
    if quer_continuar in 'nN':
        break

print('+='*25)
print(f'Você digitou {len(lista_num)} elementos.')
lista_num.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista_num}')
if 5 in lista_num:
    print(f'Valor 5 faz parte da lista!')
else:
    print(f'Valor 5 não faz parte da lista!')