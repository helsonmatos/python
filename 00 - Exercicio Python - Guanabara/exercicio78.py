seq = list(range(0,5))
lista_numeros = []
maior = menor = 0
for i in seq:
    valor = int(input(f'Digite um valor para a Posição {i}: '))
    lista_numeros.append(valor)
    if i == 0:
        maior = menor = lista_numeros[i]
    else:
        if lista_numeros[i] > maior:
            maior =  lista_numeros[i]
        elif lista_numeros[i] < menor:
            menor = lista_numeros[i]
    
print('=-'*20)
print(f'Você digitou os valores {lista_numeros}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(lista_numeros):
    if v == maior:
        print(f'{maior}...', end=' ')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(lista_numeros):
    if v == menor:
        print(f'{menor}...', end=' ')