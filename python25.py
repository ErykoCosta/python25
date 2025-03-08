# idade = 15
# while True:
#     try:
#         idade = int(input('Digite sua idade: '))
#     except ValueError:
#         print('Digite um número inteiro.')
#         continue

#     if idade >= 18:
#         print ('Você pode beber cerveja.')
#         break
#     else:
#         print ('Você não pode beber cerveja.')
#         break

texto = '''Escolha sua água para comprar:
(1) Água mineral
(2) Água com gás'''

opcao = input(texto + '\nDigite sua escolha (1/2): ')
while opcao not in ['1', '2']:
    print('Opção inválida! Tente novamente.')
    opcao = input(texto + '\nDigite sua escolha (1/2): ')

mineral = 2.50
gas = 3.00 
qtdade = ''
valor_total = 0

if opcao == '1':
    print('Você escolheu água mineral. O valor é R$', mineral)
    while not qtdade.isdigit():
        qtdade = input('Quantas garrafas deseja comprar? ')
        if not qtdade.isdigit():
            print('Digite um número inteiro.')
    qtdade = int(qtdade)
    valor_total = qtdade * mineral
    print('O valor total da sua compra é R$', valor_total)
    
elif opcao == '2':
    print('Você escolheu água com gás. O valor é R$', gas)
    while not qtdade.isdigit():
        qtdade = input('Quantas garrafas deseja comprar? ')
        if not qtdade.isdigit():
            print('Digite um número inteiro.')
    qtdade = int(qtdade)
    valor_total = qtdade * gas
    print('O valor total da sua compra é R$', valor_total)
