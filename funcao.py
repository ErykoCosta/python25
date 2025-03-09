# %%
def fun(x):
    resultado = 1 + x
    return resultado

# %%
fun(10)
# %%
def juros_compostos(aporte: int, taxa: float,anos: int) -> float:
    return aporte * (1 + taxa) ** anos
# %%
juros_compostos(aporte=1000, taxa=1.5, anos=4)
# %%
def par_impar(numero: int):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'
    
numero = int(input('Digite um número: '))
resultado = par_impar(numero)
print(f'O número {numero} é {resultado}.')

# %%
def soma(a: float, b: float, *args) -> float:
    valores = [a, b] + list(args)
    return sum(valores)

def media(a: float, b: float, *args) -> float:
    return soma(a, b, *args) / (len(args)+2)

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
d = float(input('Digite o quarto número: '))

print(f'A média dos números é = {media(a, b, c, d)}.')   

