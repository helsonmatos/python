salario = int(input('Qual o salário do funciónario? '))

if salario < 1250:
    salario_atual = salario * 15 / 100
    s = salario + salario_atual
else:
    salario_atual = salario * 10 / 100
    s = salario + salario_atual

print(f'\033[35mO funcionário recebeu {s} de aumento')