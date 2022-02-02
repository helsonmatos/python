numero = int(input('Quer ver a tabuada de qual valor? '))
print('-'*35)
digito = 0
while digito == 0:
    for c in range(0,11):
        print(f'{numero} X {c} = {numero * c}')
    
    print('-'*35)
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break

print('FIM do Laço')