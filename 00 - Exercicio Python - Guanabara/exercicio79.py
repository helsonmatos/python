lista_num = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista_num:
        lista_num.append(valor)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar.')
       
    quer_continuar = str(input('Quer continuar? [S/N] '))
    if quer_continuar in 'Nn':
        break 
print('-'*30)
lista_num.sort()
print(f'Você digitou os valores {lista_num}.')