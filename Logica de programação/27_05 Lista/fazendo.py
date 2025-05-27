bois = "S"
todosbois = []
maisPesado = 0
maisLeve = 10000000
maisGordo = {"Identificação":"identificação", "Peso": 0}
maisMagro = {"Identificação":"identificação", "Peso": 0}

while bois.upper() == "S":
    boi = {"Identificação":"identificação", "Peso": 0}
    boi["Identificação"] = input("Entre com a identificação do boi: ")
    boi["Peso"] = int(input("Entre com o peso do boi: "))
    todosbois.append(boi)
    
    peso = boi["Peso"]
    identificação = boi["Identificação"]
    if peso > maisPesado:
        maisPesado = peso
        maisGordo["Identificação"] = identificação
        maisGordo["Peso"] = peso
    
    if peso < maisLeve:
        maisLeve = peso
        maisMagro["Identificação"] = identificação
        maisMagro["Peso"] = peso    

    bois = input("Tem mais boi para cadastrar se sim Digite S caso contrario qualquer outra tecla: ")
    
print("O boi mais Gordo é", maisGordo)
print("O boi mais Magro é", maisMagro)