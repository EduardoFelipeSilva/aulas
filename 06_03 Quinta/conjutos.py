# | União
# & Intersecção
# - diferença
# <(esta contido/subconjunto)
# print(type(A)) Saber o tipo, precisa ser set
A = {-2,0,1,3}
B = {0,2,3,4,5}
U = {-2,-1,0,1,2,3,4,5}
cA = U-A
# Complementar de A
cB = U-B
# complementar de B
ccA = U - cA
# complementar do complementar de A
AB = A | B
# União de AB
cAB = U - AB
# Complementar de União A com B


# print("A ordenado:", sorted(A))
# print("B ordenado:", sorted(B))
# print("U ordenado:", sorted(U))

# print("5 esta contido B",5 in B)
# print("A é subconjuto de B",A < B)
# print("A intersecção B", A & B)
# print("A Uniao B", A | B)
# print("A diferença B", A - B)
# print("Complementar A", U - A)
# print("2 Idempotência A União B = B União A", A | B == B | A)
# print("5 Associativa (A União B)União C = A União(B União C) ", (A | B) | U == A | (B | U))
# print("6 Distributiva A intersecção(B União C) = (A União B)intersecção(A União C) ", A & (B | U) == (A & B) | (A & U))
# print("7 Absorção A intersecção (A União B) = A ", A & (A | B) == A)
# print("7 Absorção A intersecção (cA União B) = A intersecção B ", A & (cA | B) == A & B )
# print("8 Complementar do complementar de A = A ", ccA == A)
print("9 O Complementar de A união B = Complementar A intersecção Complementar B", cAB == cA & cB)
# print("10 A intersecção complementar de A = Vazio ", A & cA == set())
# print("11 A união complementar A = U ", A | cA == U)
# print("12 A diferença B = A intersecção complementar B ", A-B == A & cB)



