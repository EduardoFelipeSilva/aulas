n1 = float(input("Digite o primeiro numero para a operação "))
n2 = float(input("Digite o segundo numero para a operaçao "))
operacao = int(input("selecione a operação que deseja realizar sendo \n 1: soma \n 2: multiplicação, \n 3: subtração, \n 4: divisão \n"))

match operacao:
    case 1:
        resultado = n1+n2
        print("O resultado é: ", resultado)
    case 2:
        resultado = n1*n2
        print("O resultado é: ", resultado)
    case 3:
        resultado = n1-n2
        print("O resultado é: ", resultado)
    case 4:
        if(n2 == 0):
            print("0 nao é valido para divisão")
        else:
            resultado = n1/n2
            print("O resultado é: ", resultado)
    case _:
        print("Operação invalida")
