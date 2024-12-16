from functools import reduce
n, m = map(int,input().split())
nm = input()
var = 0
lec = 0
cont = 0
for cont in range (len(nm)):
    vetor_f = set()
    for i in range (n):
        vetor_n = len(vetor_f)
        contas = 0
        if(cont + n >= len(nm)):
            vetor = nm[cont :]
            vetor += nm[: cont+n-len(nm)]
        else:
            vetor = nm[cont : cont + n]
        contas = reduce(lambda x,y: x+y,vetor)
        vetor_f.add(contas)
        if(len(vetor_f) == vetor_n):
            print("N")
            lec = lec + 1
            break
if(lec == 0):
    print("S")