num = int(input('Digite um número: '))
print('\033[35mEscolha uma das bases para conversão:\033[m')
print('[ 1 ] converter para BINÀRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
sua_opcao = int(input('Sua opção: '))

if sua_opcao == 1:
   print(f'{num} convertido para BINÀRIO é {bin(num)[2:]}')
elif sua_opcao == 2:
   print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif sua_opcao == 3:
   print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('\033[31mOpção inválida.Tente novamente\033[m')

