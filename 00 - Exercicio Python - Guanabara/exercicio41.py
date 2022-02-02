from datetime import date
data_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
sua_idade = data_atual - ano_nascimento

print(f'O atleta tem {sua_idade} anos.')
if sua_idade <= 9:
    print('Classificação: MIRIM')
elif sua_idade <= 14:
    print('Classificação: INFANTIL')
elif sua_idade <= 19:
    print('Classificação: JÙNIOR')
elif sua_idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('MASTER')