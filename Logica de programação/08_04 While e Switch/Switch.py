codigo = int(input("Informe o codigo do produto: "))
match codigo:
    case 1:
        quantidade = int(input("Informe a quantidade total dos produtos: "))
        total = 8,10 * quantidade
        print("O valor do pedido foi: ", total)
    case 2:
        quantidade = int(input("Informe a quantidade total dos produtos: "))
        total = 11,30 * quantidade
        print("O valor do pedido foi: ", total)
    case 3:
        quantidade = int(input("Informe a quantidade total dos produtos: "))
        total = 15,50 * quantidade
        print("O valor do pedido foi: ", total)
    case 4:
        quantidade = int(input("Informe a quantidade total dos produtos: "))
        total = 13,10 * quantidade
        print("O valor do pedido foi: ", total)
    case 5:
        quantidade = int(input("Informe a quantidade total dos produtos: "))
        total = 14,30 * quantidade
        print("O valor do pedido foi: ", total)
    case 6:
        quantidade = int(input("Informe a quantidade total dos produtos: "))
        total = 5 * quantidade
        print("O valor do pedido foi: ", total)
    case _:
        print("Codigo invalido")


        