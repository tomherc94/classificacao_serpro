import csv

# Abre o arquivo de texto para leitura
with open('classificacao_editado2.txt', 'r') as arquivo_texto:
    linhas = arquivo_texto.readlines()

# Processa as linhas e separa os campos (por exemplo, usando split())
dados_csv = []
for linha in linhas:
    campos = linha.strip().split(",")  # Aqui, você pode ajustar o separador
    dados_csv.append(campos)

# Abre o arquivo CSV para escrita usando a biblioteca csv
with open('classificacaoSerpro.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    for linha in dados_csv:
        escritor_csv.writerow(linha)