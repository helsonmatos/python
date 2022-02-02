from datetime import date

data_atual = date.today().year 
velho = 0
novo = 0
for p in range(1,8):
    pessoa = int(input(f'Em que ano a {p}° pessoa nasceu? '))
    pessoa_idade_atual = data_atual - pessoa
    if pessoa_idade_atual < 18:
        novo = novo + 1
    else:
        velho = velho + 1

print(f'Ao todo tivemos {velho} pessoa(s) maiores de idade')
print(f'E também tivemos {novo} pessoa(s) menores de idade')