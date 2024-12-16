var1 = input().split()
var2 = input().split()
cont = 0
comp1 = int(var1[0])

for i in range(len(var2)):
    comp2 = int(var2[i])
    if(comp1 == comp2):
        cont = cont + 1

print(cont)
