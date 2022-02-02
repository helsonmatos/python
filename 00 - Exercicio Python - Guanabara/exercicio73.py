times = (
'Bahia','Vitória','Grêmio','Vasco','Corinthians','Palmeiras',
'Fluminense','Chapecoense','Flamengo','Botafogo','Cruzeiro','Coritiba',
'RB Bragantino','Fortaleza','Goiás','São Paulo','Santos','Atletico MG','Atletico PR',
'America MG')

print('-'*40)
print(f'Os 5 primeiros times são\n {times[:5]}')
print('-'*40)
print(f'Os últimos 4 colocados são\n {times[-4:]}')
print('-'*40)
print(f'Times em ordem alfabética:\n {sorted(times)}')
print('-'*40)
print(f'Em qual posição está o time da Chapecoense?\n {times.index("Chapecoense")}')
print('-'*40)