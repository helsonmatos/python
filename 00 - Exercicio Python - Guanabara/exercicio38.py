num = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num > num2:
    print('\033[32mO primeiro valor é maior!\033[m')
elif num < num2:
    print('\033[33mO segundo valor é maior!\033[m')
else:
    print('\033[31mNão existe valor maior, os dois são iguais!\033[m')