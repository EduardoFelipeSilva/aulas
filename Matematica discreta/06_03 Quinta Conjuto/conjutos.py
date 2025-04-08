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

A = {-2,0,1,3}
B = {0,2,3,4,5}
C = {-2,0,1,3, 5}
U = {-2,-1,0,1,2,3,4,5}
cA = U-A
# Complementar de A
cB = U-B
# complementar de B
ccA = U - cA
# complementar do complementar de A
uAB = A | B
# União de AB
cAB = U - uAB
# Complementar de União A com B
iAB = A & B 
# Intersecção A com B
cAintB = U - iAB
# complementar de intersecção de A com B


# print("A ordenado:", sorted(A))
# print("B ordenado:", sorted(B))
# print("U ordenado:", sorted(U))




# print("1 se A < C então A união C = C ? ", A | C == C)
# print("*********************************************************")
# print("2 Idempotência: A União B = B União A ? ", A | B == B | A)
# print("*********************************************************")
# print("3 Elementos neutros: A União Vazio = A ? ", A | set() == A)
# print("*********************************************************")
# print("4 Comutativa: A União B = B uniao A ? ", A | B == B | A)
# print("*********************************************************")
# print("5 Associativa: (A União B)União C = A União(B União C) ? ", (A | B) | U == A | (B | U))
# print("*********************************************************")
# print("6 Distributiva: A intersecção(B União C) = (A União B)intersecção(A União C) ? ", A & (B | U) == (A & B) | (A & U))
# print("*********************************************************")
# print("7 Absorção: A intersecção (A União B) = A ? ", A & (A | B) == A)
# print("7 Absorção: A intersecção (cA União B) = A intersecção B ? ", A & (cA | B) == A & B )
# print("*********************************************************")
# print("8 Complemento duplo: Complementar do complementar de A = A ? ", ccA == A)
# print("*********************************************************")
# print("9 Leis de Morgan: O Complementar de A união complementar B = Complementar A intersecção Complementar B ? ", cAB == cA & cB)
# print("9 Leis de Morgan: O Complementar A intersecção complementar B = complementar A uniao complemtentar B ? ", cAintB == cA | cB)
# print("*********************************************************")
# print("10 Lei da nulidade: A intersecção complementar de A = Vazio ? ", A & cA == set())
# print("*********************************************************")
# print("11 Lei do complemento: A união complementar A = U ? ", A | cA == U)
# print("*********************************************************")
# print("12 A diferença B = A intersecção complementar B ? ", A-B == A & cB)
# print("*********************************************************")





