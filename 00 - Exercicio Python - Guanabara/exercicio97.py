def printEspecial(texto):
    print('^' * len(texto))
    print(f'{texto}')
    print('^' * len(texto))

printEspecial(input('Digite um texto: '))