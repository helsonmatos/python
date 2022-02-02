produto = float(input('Valor do produto: '))
desconto = (produto * 15) / 100
valor_final =  produto - desconto
print(f'\033[38mVocê recebeu um desconto de R${valor_final}0 na sua compra.') 
