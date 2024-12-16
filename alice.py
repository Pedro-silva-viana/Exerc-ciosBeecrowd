x, y, z = map(int, input().split())
p = x+y+z
if(p == 3):
    print(3)
elif(p == 6):
    print(0)
elif(p == 4):
    print(2)
else:
    print(1)