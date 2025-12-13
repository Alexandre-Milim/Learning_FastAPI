#Dada a lista numeros = [10, 25, 8, 42, 15, 30], crie uma
#nova lista apenas com os números maiores que 20.

lista = [10,25,8,42,15,30]
maiores_que_20 = []

for numeros in lista:
    if numeros > 20:
        maiores_que_20.append(numeros)
        print(numeros)
