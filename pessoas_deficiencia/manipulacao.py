import re

with open("pcd2.txt", "r") as arquivo:
    conteudo = arquivo.read()

#conteudo_sem_espacos = re.sub(r'\s+', '', conteudo)
conteudo_final = conteudo.replace('/','\n') 

with open("pcd3.txt", "w") as arquivo:
    arquivo.write(conteudo_final)