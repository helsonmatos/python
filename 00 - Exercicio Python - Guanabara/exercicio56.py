mais_velho = 0
mulheres = 0
nome_homem = ''
media = 0
total_mulheres = 0

for p in range(1,5):
    print('-'*5, f'{p}° PESSOA', '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower()

    media = media + idade
    if sexo == 'm':
        if idade >= mais_velho:
            mais_velho = idade
            nome_homem = nome
    elif sexo == 'f':
        mulheres = idade
        if mulheres < 20:
            total_mulheres = total_mulheres + 1

print(f'A média de idade do grupo é de {media / 4} anos. ')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_homem}.')
print(f'Ao todo são {total_mulheres} mulher(es) com menos de 20 anos.')