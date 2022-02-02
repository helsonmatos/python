from random import sample

a = tuple(sample(range(10),5))
print(f'Os numeros sorteados foram: {a}')
print(f'O maior valor sorteado foi {max(a)}')
print(f'O menor valor sorteado foi {min(a)}')
