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
    
if opcao == '1':
    print('Você escolheu água mineral. Sua conta deu R$ 2,50.')
elif opcao == '2':
    print('Você escolheu água com gás. Sua conta deu R$ 3,00.')