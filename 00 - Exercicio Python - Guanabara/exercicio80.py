lista_num = []
cont = 0
valor_dois = 0
for i in range(5):
    valor = int(input('Digite um valor: '))
    cont += 1
    if cont == 1 :
        lista_num.append(valor)
        print('Adicionado ao final da lista...')
        valor_dois = valor
    elif valor <= valor_dois:
        lista_num.insert(i,valor)
        lista_num.sort()
        print(f'Adicionado na posição {lista_num.index(valor)} da lista')
    elif valor >= valor_dois:
        lista_num.append(valor)
        lista_num.sort()
        print('Adicionado ao final da lista...')
    else:
        lista_num.append(valor)
        

print(f'Os valores digitados em ordem foram {lista_num}')