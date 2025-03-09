# %%
numero_sorteio = 7

while True:
    try:
        numero_usuario = int(input('Digite um número de 1 a 10: '))
        if numero_usuario in range(1, 11):
            break
        else:           
            print('Número errado! Digite um númeor de 1 a 10: ')
    
    except ValueError:
        print('Entrada inválida! Por favor, digite um número inteiro entre "1" e "10".')
        

if numero_usuario == numero_sorteio:
    print('Parabéns! Você acertou o número sorteado!')
else:
    print('Que pena! Você errou o número sorteado!')
