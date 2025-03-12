idade = int(input("Entre com sua idade : "))
if(idade >= 1 or idade <= 120):
    if(idade < 16):
        print("Não pode votar")
    elif(idade < 18 or idade > 65):
        print("Voto não obrigatório")
    else:
        print("Voto obrigatório")
else:
    print("Idade inválida")
