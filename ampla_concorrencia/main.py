import csv, sys

class Candidato:
    def __init__(self, inscricao, nome, notaPortugues, acertosPortugues,
                 notaIngles, acertosIngles, notaEstatistica, acertosEstatistica,
                 notaLRM, acertosLRM, notaLegislacao, acertosLegislacao,
                 notaBasicos, acertosBasicos, notaTI, acertosTI, notaFinal):
        self.inscricao = inscricao
        self.nome = nome
        self.notaPortugues = notaPortugues
        self.acertosPortugues = acertosPortugues
        self.notaIngles = notaIngles
        self.acertosIngles = acertosIngles
        self.notaEstatistica = notaEstatistica
        self.acertosEstatistica = acertosEstatistica
        self.notaLRM = notaLRM
        self.acertosLRM = acertosLRM
        self.notaLegislacao = notaLegislacao
        self.acertosLegislacao = acertosLegislacao
        self.notaBasicos = notaBasicos
        self.acertosBasicos = acertosBasicos
        self.notaTI = notaTI
        self.acertosTI = acertosTI
        self.notaFinal = notaFinal
        if self.notaBasicos and self.notaTI != None:
            self.notaCalculada = self.notaBasicos + (2*self.notaTI)
    
    def __str__(self):
        return f"\nNome: {self.nome}\nNota Basicos: {self.notaBasicos}\nAcertos Básicos: {self.acertosBasicos}\nNota TI: {self.notaTI}\nAcertos TI: {self.acertosTI}\nNota Final: {self.notaFinal}\nNota Calculada: {self.notaCalculada}"

# Lista para armazenar os candidatos
lista_de_candidatos = []

# Abre o arquivo CSV e lê os dados
with open('classificacaoSerpro.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    cabecalho = next(leitor_csv)  # Pula a linha de cabeçalho

    for linha in leitor_csv:
        inscricao, nome, notaPortugues, acertosPortugues, notaIngles, acertosIngles, \
        notaEstatistica, acertosEstatistica, notaLRM, acertosLRM, notaLegislacao, \
        acertosLegislacao, notaBasicos, acertosBasicos, notaTI, acertosTI, notaFinal = linha
        
        candidato = Candidato(inscricao, nome.upper(), float(notaPortugues), int(acertosPortugues),
                              float(notaIngles), int(acertosIngles), float(notaEstatistica),
                              int(acertosEstatistica), float(notaLRM), int(acertosLRM),
                              float(notaLegislacao), int(acertosLegislacao), float(notaBasicos),
                              int(acertosBasicos), float(notaTI), int(acertosTI), float(notaFinal))
        
        lista_de_candidatos.append(candidato)



# Exemplo de acesso às informações do primeiro candidato na lista
quantidade = len(lista_de_candidatos)
print(f"Quantidade de aprovados: {quantidade}\n")

lista_de_candidatos_ordenada = sorted(lista_de_candidatos, key=lambda candidato: (candidato.notaCalculada, candidato.notaTI, candidato.acertosTI, candidato.acertosBasicos), reverse=True)


# Exibe as informações dos candidatos na lista ordenada
for index, candidato in enumerate(lista_de_candidatos_ordenada):
    if candidato.nome == sys.argv[1]:
        print(candidato)
        print(f"Classificação: {index+1}")
        print("")
    
#print(lista_de_candidatos_ordenada[-1])
