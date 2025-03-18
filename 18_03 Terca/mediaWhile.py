r = "S"
a = 0
aprovado = 0
reprovado = 0
exame = 0
m = 0
mSala = 0
while r.upper() == "S":
    n1 = int(input("Entre com a nota 1: "))
    n2 = int(input("Entre com a nota 2: "))
    mSala = m + mSala
    m = (n1+n2)/2
    a += 1
    print("A média do aluno",a, "foi:",m)
    if(m > 5):
        print("Aluno aprovado")
        aprovado += 1
    elif(m>=3):
        print("Aluno de exame")
        exame += 1
    else:
        print("Aluno reprovado")
        reprovado += 1

    r = input("Tem mais aluno para fazer a média? S/N: ")
mediaSala = mSala/a
print("A quantidade de alunos aprovados foram: ",aprovado, "\n", "A quantidade de reprovados é: ", 
      reprovado, "\n", "A quantidade de alunos em exame é: ",exame, "\n", "A média da sala é: ",mediaSala)