print('='*30)
print('         BANCO HM')
print('='*30)

valor = int(input('Qual valor você quer sacar? '))
total = valor
ced = 50
ced_total = 0

while True:
    if total >= ced:
        total -= ced
        ced_total += 1 
    else:
        if ced_total > 0:
            print(f'Total de {ced_total} cedulas de R${ced}') 
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        ced_total = 0
        if total == 0:
            break

print('='*30)