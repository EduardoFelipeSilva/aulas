n = 0
aluno = 0
notasala = 0

while n!= -1:
    m = int(input())
    aluno +=1
    notasala +=m
    print('tem mais aluno? (-1 caso não)')
    n = int(input())
mediaSala = notasala / aluno
print(mediaSala)