soma = 0
for c in range(0,6):
    num = int(input('Digite 6 números: '))
    if num % 2 == 0:
      soma = soma + num  
    else:
        pass
print(f'A soma dos números pares é {soma}')