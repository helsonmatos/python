continuar = 's'
total_numeros = 0
media = 0
media_total = 0
valores = []
while continuar == 's':
    num = int(input('Digite um número: '))
    total_numeros += 1
    media += num 
    media_total = media / total_numeros
    valores.append(num)
    
    continuar = str(input('Quer continuar? ')).strip().lower()

print(f'Você digitou {total_numeros} e a média foi {media_total}')
print(f'O maior valor foi {max(valores)} e o menor {min(valores)}')
