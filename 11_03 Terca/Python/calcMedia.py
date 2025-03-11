n1 = float (input("Informe a nota 1: "))
n2 = float (input("Informe a nota 2: "))
m = (n1 + n2)/2
print("A média é: ",m)
if(m >= 5):
    print("Aluno aprovado")
elif(m>=4 and m < 5 ):
    print("Aluno de exame")
else:
    print("Aluno reprovado")