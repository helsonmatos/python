frase = str(input('Digite uma frase: ')).upper().strip()
frase_separada = frase.split()
frase_junta = "".join(frase_separada)
inverso_frase = frase_junta[::-1]


if frase_junta == inverso_frase:
    print('è PALINDROMO!')
else:
    print('Não é um PALINDROMO')

print(f'O inverso de {frase} é {inverso_frase}')

