num = int(input('Digite um número para\ncalcular seu Fatorial: '))
print(f'Calculando {num}!')
tot = 0

for c in range(num,-1,-1):
    mult = num * c
    tot += mult 
    print(f'{num} X {c} => {mult}', end=' ')
    print(tot)