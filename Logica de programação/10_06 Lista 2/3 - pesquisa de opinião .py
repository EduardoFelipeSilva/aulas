def main():
    finalizar = "N"
    entrevistados = []
    while finalizar.upper() != "S":
        sexo = input("Digite o sexo do entrevistado (F/M): ")
        opinia = int(input("Digite a opiniao do entrevistado: 1 para sim 2 para não "))
        pesquisa = {"sexo":sexo,"opiniao":opinia }
        entrevistados.append(pesquisa)
        finalizar = input("Deseja finalizar o programa? (S/N): ")

    sim(entrevistados)
    nao(entrevistados)
    mulherSim(entrevistados)
    homemNao(entrevistados)

def sim(entrevistados):
    totalSim = 0
    for x in entrevistados:
        if x["opiniao"] == 1:
            totalSim += 1
    print(f"Total que responderam 'Sim': {totalSim}")

def nao(entrevistado):
    totalNao = 0
    for x in entrevistado:
        if x["opiniao"] == 2:
            totalNao += 1
    print(f"Total que responderam 'Não': {totalNao}")

def mulherSim(entrevistado):
    totalMulheres = sum(1 for x in entrevistado if x["sexo"].upper() == "F")
    mulherSim = sum(1 for x in entrevistado if x["sexo"].upper() == "F" and x["opiniao"] == 1)
    percentual = (mulherSim / totalMulheres * 100) if totalMulheres > 0 else 0
    print(f"Total de mulheres que responderam 'Sim': {mulherSim}")
    print(f"Porcentagem de mulheres que disseram 'Sim': {percentual:.2f}%")

def homemNao(entrevistado):
    totalHomens = sum(1 for x in entrevistado if x["sexo"].upper() == "M")
    homemNao = sum(1 for x in entrevistado if x["sexo"].upper() == "M" and x["opiniao"] == 2)
    percentual = (homemNao / totalHomens * 100) if totalHomens > 0 else 0
    print(f"Total de homens que responderam 'Não': {homemNao}")
    print(f"Porcentagem de homens que disseram 'Não': {percentual:.2f}%")



main()


