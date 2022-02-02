numero = int(input('Digite um número para ver sua tabuada: '))
count = 1
for count in range(1,11):
    print(f'{numero} X {count} = {numero * count}')
    count = count + 1