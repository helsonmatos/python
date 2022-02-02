from datetime import date
atual = date.today().year
ano_de_nascimento = int(input('\033[36mAno de nascimento: \033[m'))

quantos_anos_hoje = atual - ano_de_nascimento 
alistamento_ha = quantos_anos_hoje - 18
alistamento_ano_dever = atual - alistamento_ha

print(f'Quem nasceu em {ano_de_nascimento} tem {quantos_anos_hoje} anos em {atual}.')
if quantos_anos_hoje < 18:
    alistamento_ha = 18 - quantos_anos_hoje
    print(f'Ainda faltam {alistamento_ha} anos para o seu alistamento.')
    print(f'Seu alistamento será em {alistamento_ano_dever}.')
elif quantos_anos_hoje > 18:
    alistamento_ha = quantos_anos_hoje - 18
    print(f'Você já deveria ter se alistado há {alistamento_ha} anos.')
    print(f'Seu alistamento foi em {alistamento_ano_dever}.')
elif quantos_anos_hoje == 18:
    print('Você tem que se alistar imediatamente.')
