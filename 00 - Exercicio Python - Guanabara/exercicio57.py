sexo = str(input('Informe o seu sexo [M/F]: ')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos.Por favor, informe seu sexo: ').upper()

print('Sexo registrado com sucesso.')