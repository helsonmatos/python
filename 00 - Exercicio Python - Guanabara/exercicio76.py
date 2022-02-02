print('-'*42)
print('         LISTAGEM DE PREÇOS')
print('-'*42)

produtos = ('Lápis', 1.75, 'Borracha', 2.00,'Caderno', 15.90,
'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
'Mochila', 120.00, 'Canetas', 22.30, 'Livro', 34.90)

print()
print('-'*42)
for p in produtos:
    if type(p) is str:
        print(f'{p:.<32}',end=' ')
    else:
        print(f'R$ {p:>5.2f}')
print('-'*42)
print()