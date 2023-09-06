import re

with open("classificacao_editado.txt", "r") as arquivo:
    conteudo = arquivo.read()

#conteudo_sem_espacos = re.sub(r'\s+', '', conteudo)
conteudo_final = conteudo.replace('/','\n') 

with open("classificacao_editado2.txt", "w") as arquivo:
    arquivo.write(conteudo_final)