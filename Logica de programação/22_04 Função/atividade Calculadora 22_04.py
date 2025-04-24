    #Definindo as variasveis para usar na função calcular
N1 =int(input('Digite o 1º Numero:'))
N2 =int(input('Digite o 2º Numero:'))
  
     #Soma
def calculoSoma(N1,N2):
    'Função para somar'
    resultado = N1 + N2
    return resultado


    #Subtrair

def calculoSubtrair(N1,N2):
    'função para subtrair'
    resultado = N1 - N2
    return resultado


    #Divisao

def calculoDividir(N1,N2):
    'Função para dividir'
    if N2 != 0:
        resultado = N1 / N2
        return resultado

    #Multiplicar

def calculoMultiplicar(N1,N2):
    'Função para multiplicar'
    resultado = N1 * N2
    return resultado


    #Case para escolher a operação
operacao = int(input("digite a operação que você quer fazer 1 Soma, 2 Subtrair, 3 Dividir e 4 Multplicar "))
match operacao:
    case 1:
        print(calculoSoma(N1,N2))

    case 2:
        print(calculoSubtrair(N1,N2))

    case 3:
        print(calculoDividir(N1,N2))

    case 4:

        print(calculoMultiplicar(N1,N2))





