import random

NUM_LINHAS = 5
NUM_COLUNAS = 5
NUM_MINAS = 5

def criar_tabuleiro():
    return [[' ' for _ in range(NUM_COLUNAS)] for _ in range(NUM_LINHAS)]

def posicionar_minas(tabuleiro):
    total_minas_colocadas = 0
    while total_minas_colocadas < NUM_MINAS:
        linha = random.randint(0, NUM_LINHAS - 1)
        coluna = random.randint(0, NUM_COLUNAS - 1)
        if tabuleiro[linha][coluna] != 'X':
            tabuleiro[linha][coluna] = 'X'
            total_minas_colocadas += 1

def exibir_tabuleiro(tabuleiro, celulas_reveladas):
    print("   " + " ".join(str(coluna) for coluna in range(NUM_COLUNAS)))
    for linha in range(NUM_LINHAS):
        linha_visual = []
        for coluna in range(NUM_COLUNAS):
            if celulas_reveladas[linha][coluna]:
                if tabuleiro[linha][coluna] == 'X':
                    linha_visual.append('X')
                else:
                    linha_visual.append(' ')
            else:
                linha_visual.append('.')
        print(f"{linha}  " + " ".join(linha_visual))

def jogar():
    tabuleiro = criar_tabuleiro()
    posicionar_minas(tabuleiro)
    celulas_reveladas = [[False for _ in range(NUM_COLUNAS)] for _ in range(NUM_LINHAS)]

    while True:
        exibir_tabuleiro(tabuleiro, celulas_reveladas)
        try:
            escolha_linha = int(input("Escolha a linha: "))
            escolha_coluna = int(input("Escolha a coluna: "))
            if not (0 <= escolha_linha < NUM_LINHAS and 0 <= escolha_coluna < NUM_COLUNAS):
                print("Lugar errado, tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida. Digite números inteiros.")
            continue

        if tabuleiro[escolha_linha][escolha_coluna] == 'X':
            print("\n💥 Você perdeu! Acertou uma mina!")
            for linha in range(NUM_LINHAS):
                for coluna in range(NUM_COLUNAS):
                    celulas_reveladas[linha][coluna] = True
            exibir_tabuleiro(tabuleiro, celulas_reveladas)
            break
        else:
            celulas_reveladas[escolha_linha][escolha_coluna] = True


        total_celulas_seguras_reveladas = sum(
            1 for linha in range(NUM_LINHAS) for coluna in range(NUM_COLUNAS)
            if celulas_reveladas[linha][coluna] and tabuleiro[linha][coluna] != 'X'
        )
        total_celulas_seguras = NUM_LINHAS * NUM_COLUNAS - NUM_MINAS

        if total_celulas_seguras_reveladas == total_celulas_seguras:
            exibir_tabuleiro(tabuleiro, celulas_reveladas)
            print("\n🎉 Parabéns! Você venceu o jogo!")
            break
jogar()
