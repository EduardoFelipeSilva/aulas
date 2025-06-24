n = int(input())
n2 = int(input())
try:
    resultado = n/n2
    print(resultado)
    
# Para um erro especifico

except ZeroDivisionError:
    print("Erro de divisão por zero")
    
except Exception as e:
    print(f"erro de {e}")
 
#  Todos os erros com finalização no final e uma mensagem de sucesso so tiver ok
except:
    print("Todos erros com mensagem para sucesso")
else:
    print("Sucesso")
finally:
    print("Executa aqui com erro ou sem erro; Sempre executa")

