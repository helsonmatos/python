import calendar, datetime

ano = int(input('Digite um ano ou 0 para pegar a data atual!'))
ano_bi = calendar.isleap(ano)
ano_comp = ano % 4

if ano == 0:
    ano = datetime.date.today().year
if ano_bi == True:
    print(f'\033[35m{ano} é BI')
else:
    print(f'\033[35m{ano} Não é BI')

if ano_comp == 0:
    print(f'{ano} é um ano BISEXTO!!!')

else:
    print(f'{ano} Nâo é um ano BISEXTO....')

