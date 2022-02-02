velo_carro = int(input('Qual a velocidade que você está? '))
calculo = (velo_carro - 80) * 7
if velo_carro > 80:
    print(f'MULTADO!Você excedeu o limite permitido que é de 80km \n você deve pagar uma multa de R${calculo}.00 ')

print('\033[35mTenha um Bom dia, diriga com cuidado!')