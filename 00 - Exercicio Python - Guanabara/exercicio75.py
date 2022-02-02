numeros = ((
int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: '))))

print(f'Você digitou os números: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} ')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}° posição.')
else:
    print('O valor 3 não foi digitado.')

for n in numeros:
    if n % 2 == 0:
        print(f'Os números par(es) foram {n}')