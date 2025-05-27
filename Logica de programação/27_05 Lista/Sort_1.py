# -------------- 1 Criar Lista e usar a função Sort ------------------------------------

# fruta = ['Banana', 'Laranja', 'Maça', 'Pera',]
# fruta.sort()
# print(fruta)


# -------------- 2 Adicionar novos itens ------------------------------------

# fruta.append('Goiaba', 'Lixia', 'Mamão', 'Uva')
# print(fruta)


# -------------- 3 mostrar apenas os elementos especificos ------------------------------------

numerosPares = []
contador = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22]
for x in numeros:
    if x % 2 == 0:
        numerosPares.append(x)
        contador += 1
    somaNumerosPares = (sum(numerosPares))
contador2 = len(numerosPares)
# media = somaNumerosPares / contador
media = somaNumerosPares / contador2
print(media)
    
    