#Básico: Crie uma lista com 5 frutas. Adicione mais 2 frutas, 
#remova a primeira e imprima a lista ordenada.

frutas = ['banana', 'melacia', 'uva','kiwi','pera']
novas_frutas = ['maca','mamao']

frutas.pop(0)

for fruta in frutas:
    novas_frutas.append(fruta)


print(novas_frutas)


