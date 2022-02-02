print('-'*25)
from datetime import datetime
ano = datetime.now().year
ano_nasci = int(input('Em que ano você nasceu? '))
idade = ano - ano_nasci

def ano_vote(ano):
    if idade <= 15:
        return 'NÂO VOTA'
    elif idade >= 16 and idade < 18 or idade > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÒRIO'

print(f'Com {idade} anos: {ano_vote(ano_nasci)}')