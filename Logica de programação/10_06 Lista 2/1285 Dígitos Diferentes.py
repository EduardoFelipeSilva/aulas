finalizar = "N"
entrevistados = []



while finalizar.upper() != "S":
    sexo = input("Digite o sexo do entrevistado (F/M): ")
    opinia = input("Digite a opiniao do entrevistado: 1 para sim 2 para não ")
    pesquisa = {"sexo":sexo,"opiniao":opinia }
    entrevistados.append(pesquisa)
    finalizar = input("Deseja finalizar o programa? (S/N): ")


totalSim = 0
for x in entrevistados:
    print(entrevistados)
    if opiniao == 1:
        totalSim += 1
print(totalSim)

# def nao(pesquisa):
#     totalNao = 0
#     if pesquisa[1] == 2:
#         totalNao += 1

