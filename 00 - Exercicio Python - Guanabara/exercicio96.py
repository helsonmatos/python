print('  Controle de terreno')
print('-'*25)

def area(largura, comprimento):
    result = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {result}m²')

largura = float(input('LARGURA: '))
comprimento = float(input('COMPRIMENTO: '))

area(largura,comprimento)