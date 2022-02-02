quer_continuar = 's'
maior_idade = 0
homem_tot = 0
mulher_tot = 0
while quer_continuar.lower() == 's':
    print('-'*30)
    print('    CADASTRE UMA PESSOA')
    print('-'*30)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower()
    quer_continuar = str(input('Quer continuar? [S/N] ')).lower()

    if idade > 18:
        maior_idade += 1
    if sexo in 'm':
        homem_tot += 1
    if sexo in 'f' and idade <= 20:
        mulher_tot += 1

print('='*30)
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo temos {homem_tot} homem(s) cadastrados.')
print(f'E temos {mulher_tot} mulher(es) com menos de 20 anos.')

