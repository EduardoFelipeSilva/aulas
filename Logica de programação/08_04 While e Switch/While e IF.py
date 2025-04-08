continuar = "S"
while continuar.upper() == "S":
    idade = int(input("Entre com a idade: "))
    if idade > 4:
        if idade >= 5 and idade <= 7:
            print ("Você esta na categoria infantil A")
        elif idade <= 10:
            print ("Você esta na categoria infantil B")
        elif idade <= 13:
            print ("Você esta na categoria juvenil A")
        elif idade <= 17:
            print ("Você esta na categoria juvenil B")
        else:
            print ("Adulto")
    else:
        print("Idade invalida")
    continuar = input("Cadastrar mais pessoa? ")