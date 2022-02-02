matriz = [[],[],[]]
maior = 0
soma_pares = []
soma_colunas = []
maior_s_linha = []
for i in range(0,3):
    for c in range(0,3):
        matriz[i].append(int(input(f'Digite um valor para [{i},{c}]:  ')))
        if matriz[i][c] % 2 == 0:
            soma_pares.append(matriz[i][c])
    soma_colunas.append(matriz[i][2])
for i in range(0,3):
    maior_s_linha.append(matriz[1][i])
print('=*'*30)
for i in range(0,3):
    print(f'[ {matriz[i][0]:^5} ] [ {matriz[i][1]:^5} ] [ {matriz[i][2]:^5} ]')
print('=*'*30)
print(f'A soma dos valores pares é {sum(soma_pares)}')
print(f'A soma da terceira coluna é {sum(soma_colunas)}')
print(f'O maior valor na segunda linha é {max(maior_s_linha)}')
