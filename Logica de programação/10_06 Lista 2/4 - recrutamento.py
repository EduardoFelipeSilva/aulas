def main():
    continuar = "S"
    candidatos = []
    while continuar.upper() != "N":
        numeroCandidato = int(input("Numero do candidato"))
        idadeCandidato = int(input("Idade do candidato"))
        sexoCandidato = input("Sexo do candidato")
        experienciaCandidato = input("experiência profissional(S - Sim / N - Não)")
        candidato = {"numero":numeroCandidato, "idade":idadeCandidato,"Sexo":sexoCandidato, "experiencia":experienciaCandidato}
        candidatos.append(candidato)

        continuar = input("Deseja continuar cadastrando candidatos? (S/N): ")

    IdadeMedia(candidatos)
    TotalCandidato(candidatos)

def IdadeMedia(candidatos):
    idade = 0
    totalCandidato = 0
    for x in candidatos:
        idade += x["idade"]
        totalCandidato += 1
        mediaIdade = idade / totalCandidato
        print(f"Media da idade: {mediaIdade}")

def TotalCandidato(candidatos):
    totalHomem = 0
    totalMulheres = 0
    for x in candidatos:
        if x["Sexo"].upper() == "F":
            totalMulheres += 1
        if x["Sexo"].upper() == "M":
            totalHomem += 1
    print(f"Total de Homens: {totalHomem}")
    print(f"Total de Mulheres: {totalMulheres}")

main()