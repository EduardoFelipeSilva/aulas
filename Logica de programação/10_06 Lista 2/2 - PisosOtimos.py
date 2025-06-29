def main():
    produtos = []
    aprovadas = 0
    reprovadas = 0

    while True:
        codigo = int(input("Entre com o código do produto: "))
        status = input("Entre com o status do produto (aprovado/reprovado): ").strip().lower()

        produto = {"codigo": codigo, "status": status}
        produtos.append(produto)

        if status == "reprovado":
            print(f"Produto reprovado - Código: {codigo}")
            reprovadas += 1
        else:
            aprovadas += 1

        continuar = input("Deseja cadastrar outro produto? (S/N): ").strip().upper()
        if continuar == "N":
            break

    print("\n=== RESUMO DO DIA ===")
    print(f"Total de peças aprovadas: {aprovadas}")
    print(f"Total de peças reprovadas: {reprovadas}")


main()
