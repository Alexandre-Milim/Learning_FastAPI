#Crie uma função que retorne 3 valores usando tupla: o menor número, o maior e a média de uma lista.

def retornandoValores (tuplinha):

    quantidade = len(tuplinha)

    minimo = min(tuplinha)
    media = sum(tuplinha) / len(tuplinha)
    maior =  max(tuplinha)


    return (minimo, media, maior)


resultado = retornandoValores((7,8,9))
print(resultado)
