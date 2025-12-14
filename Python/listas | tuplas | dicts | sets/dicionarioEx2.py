# Dado o texto "python é legal python é poderoso", conte quantas
# vezes cada palavra aparece usando dicionário.

texto = "python é legal python é poderoso"
palavras = texto.split()  

contagem = {}  

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1 
    else:
        contagem[palavra] = 1  

print(contagem)
