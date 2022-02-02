valor_casa = int(input('Qual o valor da casa: R$'))
salario_comprador = int(input('Salário do comprador: R$'))
financia = float(input('Quantos anos de financiamento? '))

anos = 12 * financia
valor_final = valor_casa / anos

print(f'Para pagar uma casa de R${valor_casa} em {int(financia)} anos\n a prestação será de R${round(valor_final)}.')

if salario_comprador <= 3000:
    print('\033[30mEmpréstimo NEGADO!')
elif salario_comprador <= 4500:
    print('\033[34mEmpréstimo EM ANALISE!')
else:
    print('\033[32mEmpréstimo APROVADO')