
# %%

import random
def get_input():
    while True:
        try:
            numero = int(input('Digite um número de 1 a 10: '))
            if numero in range(1, 11):
                break
            else:           
                print('Número errado! Digite um númeor de 1 a 10: ')
        
        except ValueError:
            print('Entrada inválida! Por favor, digite um número inteiro entre "1" e "10".')
    return numero

for i in range(3):
    numero_sorteio = random.randint(1, 10)
    numero_usuario = get_input()
    
    if numero_usuario == numero_sorteio:
        print('Parabéns! Você acertou o número sorteado!')
        break
    else:
        print('Que pena! Você errou o número sorteado!')
        
else:
    print('Suas chances acabaram! Tente novamente mais tarde.')