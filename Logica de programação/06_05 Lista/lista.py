#                 Lista
alunos = ["Eduardo","Vinicius","Davi","kaua","kaue",1,2,]
print(alunos)
print(type(alunos))
for aluno in alunos:
    print(aluno)

#               Remover
del alunos[6]

alunos.remove("Davi")
print(alunos)
print(type(alunos))
for aluno in alunos:
    print(aluno)

#              Dicionario
alunos = {"Eduardo": "Vinicius","Davi" :"kaua","kaue":1}
print(alunos)
print(type(alunos))

#             Remover Dicionario
del alunos["Eduardo"]
alunos["Vinicius"] = "Aristeu"