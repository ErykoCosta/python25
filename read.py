# %%
import csv

# %%
nome_arq = "texto.txt"

with open(nome_arq, 'r') as arq:
    texto = arq.read()
    
print(texto)

# %%
nome_arquivo = "historia.txt"
texto = '''Era uma vez um reino muito distante, onde viviam um rei, uma rainha e um príncipe.
O rei era muito sábio e justo, e o povo o adorava.'''

with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(texto)
    
# %%
arquivo1 = "exemplo.csv"

with open(arquivo1, 'r') as arq:
    leitor = csv.reader(arq)
    for linha in leitor:
        print(linha)

# %%
