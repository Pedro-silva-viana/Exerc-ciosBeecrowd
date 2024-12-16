var = input().split()
cont = 0

for i in range(len(var)):
    cont = cont + int(var[i])

cont = cont - (len(var) - 1)
print(cont)