# idade = 15
while True:
    try:
        idade = int(input('Digite sua idade: '))
    except ValueError:
        print('Digite um número inteiro.')
        continue

    if idade >= 18:
        print ('Você pode beber cerveja.')
        break
    else:
        print ('Você não pode beber cerveja.')
        break