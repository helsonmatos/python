#import random 

#def megasena():
    
#    n1 = random.sample(range(1,61),6)
#    return n1


#for c in range(0,):
#    print(f'jogo {megasena()}')

print('-'*20)
print('Sequência de Fibonacci')
print('-'*20)

termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
t3 = 0

while termos > t2:
    
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    
    print(t2, end=' - ')
    
    
    t1 += 1
    termos += 1