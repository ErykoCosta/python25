count = 1
numero = 2

while count <= 10:
    print(numero,"x", count, "=", numero * count)
    count += 1
# %%   
#números divisíveis por 4
count = 4
while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count)
        
    count += 1
# %%
# soma de alturas com while
soma = 0 #valor final
count = 4

while count > 0:
    try:
        altura = float(input('Digite a altura da pessoa: '))
        soma += altura
        count -= 1
    except ValueError:
        print('Por favor, digite um número válido.')

print('A soma das alturas é:', soma)
# %%
