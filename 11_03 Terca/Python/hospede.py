
nome = input("Escreva o nome do hóspede: ")
apartamento = input("Escolha o tipo de apartamento \n 1 A \n 2 B \n 3 C \n 4 D \n): ")
diarias = int(input("Número de diárias: "))
consumo = float(input("Consumo interno: "))


if apartamento == "A":
    valor_diaria = 150
elif apartamento == "B":
    valor_diaria = 100
elif apartamento == "C":
    valor_diaria = 75
elif apartamento == "D":
    valor_diaria = 50
else:
    print("Tipo de apartamento inválido.")
    exit()  


total_diaria = diarias * valor_diaria


subtotal = total_diaria + consumo


taxa_servico = subtotal * 0.1


total = subtotal + taxa_servico


print(f"\nO nome do hóspede é: {nome}")
print(f"O tipo de apartamento que ele ficou foi: {apartamento}")
print(f"O número de diárias utilizadas foi: {diarias}")
print(f"O valor da diária para esse tipo de apartamento é: {valor_diaria}")
print(f"O consumo interno foi: {consumo}")
print(f"O subtotal foi: {subtotal}")
print(f"O valor da taxa de serviço foi: {taxa_servico}")
print(f"O total gasto foi: {total}")
