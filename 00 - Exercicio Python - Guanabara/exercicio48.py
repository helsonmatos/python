count = 0
soma = 0
for c in range(1,500,2):
    if c % 3 == 0:
        print(c, end=" ")
        soma = soma + c
        count = count + 1

print(f'\nA soma de todos os {count} valores solicitados é {soma}.')
