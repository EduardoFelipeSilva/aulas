numeroJogador1 = 1
encerrar = 0
while encerrar == 0:
    numeroJogador1 = int(input("Escolha um numero de 1 a 10: "))
    tentativas = 0
    numeroJogador2 = 0
    while numeroJogador1 != numeroJogador2:
        if numeroJogador1 >= 1 and numeroJogador1 <= 10:
            numeroJogador2 = int(input("Qual numero você gostaria de tentar? "))
            tentativas += 1
            if numeroJogador2 == numeroJogador1:
                print ("Parabens voce acerto, o numero escolhido pelo jogador 1 foi:",numeroJogador1,
                       "você levou:",tentativas, "tentativas")
                encerrar = 1
            else:
                print ("infelizmente voce erro ")
        else:
            numeroJogador1 = int(input("Numero incorreto escolha um numero de 1 a 10: "))


