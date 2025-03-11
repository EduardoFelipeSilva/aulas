# cargo = int(input("Entre com o codigo do cargo entre 1 a 5: "))
# if(cargo == 1):
#     print("O cargo selecionado foi: Escrituário")
# elif(cargo == 2):
#     print("O cargo selecionado foi: Secretária")
# elif(cargo == 3):
#     print("O cargo selecionado foi: Caixa")
# elif(cargo == 4):
#     print("O cargo selecionado foi: Gerente")
# elif(cargo == 5):
#     print("O cargo selecionado foi: Diretor")
# else:
#     print("Codigo selecionado invalido")

cargo = int(input("Entre com o codigo do cargo entre 1 a 5: "))

match cargo:
    case 1:
        print("O cargo selecionado foi: Escrituário")
    case 2:
        print("O cargo selecionado foi: Secretária")
    case 3:
        print("O cargo selecionado foi: Caixa")
    case 4:
        print("O cargo selecionado foi: Gerente")
    case 5:
        print("O cargo selecionado foi: Diretor")
    case _:
        print("O codigo nao cadastrado")