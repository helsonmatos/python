soma = 0
valores = 0
while True:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor == 999:
        break
    valores += 1
    soma += valor

print(f'A soma dos {valores} valores foi {soma}.')