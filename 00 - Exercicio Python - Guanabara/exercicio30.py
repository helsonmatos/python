numero = int(input('Digite um número: '))
r = numero % 2
if r == 0:
    print('\033[36mÈ par!')
else:
    print('\033[35mÈ impar!')