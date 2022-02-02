print('=' * 15, 'LOJAS ACACIOS', '=' * 15 )
preco_das_compras = int(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] á vista dinheiro/cheque')
print('[ 2 ] á vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))


if opcao == 1:
    a_vista = preco_das_compras * 1.10
    print(f'Sua compra de R${preco_das_compras} vai custar R${a_vista}0')
elif opcao == 2:
    a_vista = preco_das_compras - (preco_das_compras * 1.05 - preco_das_compras)
    print(f'Sua compra de R${preco_das_compras} vai custar R${a_vista}0')
elif opcao == 3 or opcao == 4 :  
    if opcao == 3: 
        total = preco_das_compras
        preco_parcelado = total / 2
        print(f'Sua compra de R${total} ficou parcelada em R${preco_parcelado}')
        print(f'Sua compra de R${preco_das_compras} vai custar R${preco_das_compras}')
    else:
        parcelado = preco_das_compras * 1.20
        totparc = int(input('Quantas parcelas? '))
        parcelas = parcelado / totparc
        print(f'Sua compra será parcelada em {totparc} de R${parcelas:.2f}')
        print(f'Sua compra de R${preco_das_compras} vai custar R${parcelado}0')
else:
    print('Operação inválida. Tente Novamente')
