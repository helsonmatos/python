valor = int(input('Digite um número [999 para parar]: '))
soma = 0
while valor != 999:
    soma += valor
    valor = int(input('Digite um vnúmero [999 para parar]: '))

print(f'Você digitou 4 números e a soma entre eles foi {soma}. ')