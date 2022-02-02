print('='*30)
print('      LOJA SUPER COMEDOR')
print('='*30)
count = 0
mais_de_mil = 0
menor_produto_valor = 0
total_compra = 0
quer_continuar = ' '
produto_barato = ' '
while True:
    nome_produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total_compra += preco
    count += 1
    quer_continuar = str(input('Quer continuar? [S/N] ')).lower()
    
    if preco > 1000:
        mais_de_mil += 1
    if count == 1:
        menor_produto_valor = preco
        produto_barato = nome_produto
    else:
        if preco < menor_produto_valor:
            menor_produto_valor = preco
            produto_barato = nome_produto

    if quer_continuar == 'n':
        break

print('='*30)
print(f'O total da compra foi R${total_compra}0.')
print(f'Temos {mais_de_mil} produto(s) custando mais de R$1000')
print(f'O produto mais barato foi {produto_barato} que custa R${menor_produto_valor}')