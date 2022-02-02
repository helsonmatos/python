matriz = [[],[],[]]
for i in range(0,3):
    for c in range(0,3):
        matriz[i].append(int(input(f'Digite um valor para [{i},{c}]:  ')))
print('=*'*30)
for i in range(0,3):
    print(f'[ {matriz[i][0]:^5} ] [ {matriz[i][1]:^5} ] [ {matriz[i][2]:^5} ]')
