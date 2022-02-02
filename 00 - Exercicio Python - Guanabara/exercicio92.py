from datetime import date
data_atual = date.today().year
print(data_atual)
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if pessoa['ctps'] == 0:
    pessoa['idade'] = data_atual - pessoa['idade']
    print('-='*25)
    for k, v in pessoa.items():
        print(f'- {k} tem o valor {v}')
else:
    pessoa['idade'] = data_atual - pessoa['idade'] 
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = int(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + 35
    print('-='*25)
    for k, v in pessoa.items():
        print(f'- {k} tem o valor {v}')
        