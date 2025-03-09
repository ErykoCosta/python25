import csv

# Dados que serão gravados no CSV
dados = [
    ["nome", "idade", "cidade"],
    ["João", "30", "São Paulo"],
    ["Maria", "25", "Rio de Janeiro"],
    ["Carlos", "40", "Belo Horizonte"]
]

# Cria e escreve os dados no arquivo "exemplo.csv"
with open("exemplo.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)

print("Arquivo exemplo.csv criado com sucesso!")
