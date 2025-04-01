jogo = "V"
while jogo.upper() == "S":
    tentativa = 0
    print ( "Bem vindo ao jogo da Memoria","\n", "jogador 1 qual numero voce gostaria de escolher para ser adivinhado Escolha um numero entre 1 a 10?  ")
    j1 = int(input())
    acerto = 0
    while acerto == 0:
        if j1 >= 1 and j1 <=10:
            print("Jogador 2 Qual numero voce gostaria de tentar?")
            j2 = int(input())
            if j2 >= 1 and j2 <= 10:
                tentativa += 1
                if j2 == j1:
                    print("Parabens você acerto o numero que o jogador 1 escolheu", "\n", "O numero de tentativas foi: ",tentativa)
                    acerto += 1
                else:
                    acerto = 0
                    print("Infelizmente voce escolheu errado ")
            else:
                print("Numero incorreto escolha um numero de 1 a 10")
                j2 = int(input())
        else:
            print("Numero incorreto escolha um numero de 1 a 10")
            j1 = int(input())
    print("gostaria de continuar jogando? S/N")
    jogo = input()

    
