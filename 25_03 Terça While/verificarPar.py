n = int(input())
m = int(input())
for m in range (0,n+1,m):
    if n % 2  == 0:
        print(m,"Par")
    else:
        print(m,"impar")