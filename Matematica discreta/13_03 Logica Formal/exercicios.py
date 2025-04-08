# | União
# & Intersecção
# - diferença
# <(esta contido/subconjunto)
# Vazio = set()
# print(type(A)) Saber o tipo, precisa ser set
# print("5 esta contido B",5 in B)
# print("A é subconjuto de B",A < B)
# print("A intersecção B", A & B)
# print("A Uniao B", A | B)
# print("A diferença B", A - B)
# print("Complementar A", U - A)

A = {-1,0,1,4}
B = {-1,1,4,5}
U = {-1,0,1,2,3,4,5,6}
uAB = A | B
cA=U-A
cB=U-B

print("1º A união B = ", A | B )
print("*********************************************************")
print("2º A intersecção B = ", A & B)
print("*********************************************************")
print("3º A diferença B = ", A - B)
print("*********************************************************")
print("4º B diferença A = ", B - A)
print("*********************************************************")
print("5º complementar A = ", U - A)
print("*********************************************************")
print("6º complementar B = ", U - B)
print("*********************************************************")
print("7º A diferença (A intersecção B) = ", A - (A&B))
print("*********************************************************")
print("8º B - (A união B) = ", B - uAB)
print("*********************************************************")
print("9º Complementar uniao AB = ", U - uAB)
print("*********************************************************")
print("10º Complementar A uniao complementar B = ",((cA| cB)))
print("*********************************************************")


# A | B
# A & B
# A - B
# B - A
# complementar A
# complementar B 
# a - (A intersecção B) 
# B - (A uniao B)
# complementar da uniao de A e B 
# complementar A uniao B

