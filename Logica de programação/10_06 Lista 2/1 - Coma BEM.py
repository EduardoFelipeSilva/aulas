def main():
    # Tabela de preços
    precos = {
        1: 9.10,  # Cachorro-quente
        2: 10.30, # Bauru
        3: 13.50, # Bauru com ovo
        4: 14.10, # Hamburger
        5: 16.30, # Cheeseburger
        6: 5.00   # Refrigerante
    }

    dia = 1
    cliente_count = 0

    while dia != 0:
        cliente = 1
        cliente_count += 1
        total_final = 0

        print(f"\nAtendimento do Cliente {cliente_count}\n")

        while cliente != 0:
            pedido = int(input("Digite o código do produto: "))
            quantidade = int(input("Digite a quantidade: "))

            if pedido in precos:
                total = precos[pedido] * quantidade
                total_final += total
            else:
                print("Código inválido!")

            cliente = int(input("Deseja fazer outro pedido? (1-Sim / 0-Não): "))

        print(f"Total do cliente {cliente_count}: R$ {total_final:.2f}\n")
        dia = int(input("Encerrar o dia? (0-Sim / 1-Não): "))

main()
