peso_atual = float(input('Qual o seu peso? (Kg) '))
altura_atual = float(input('Qual é sua altura? (m) '))

imc = peso_atual / (altura_atual ** 2)
print(imc)
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc > 18.5 and imc < 25:
    print('Parabêns! Você está no peso ideal.')
elif imc > 25 and imc < 30:
    print('Você está sobrepeso.')
elif imc > 30 and imc < 40:
    print('Você está OBESO')
else:
    print('Você está OBESO MÓRBIDO.')

