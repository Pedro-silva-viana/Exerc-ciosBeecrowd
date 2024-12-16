import math
ndp = int(input("numero de paradas"))
X = []
Y = []
angulo = 0
sol = 0.00
sol_ab = 900000000
tempo_atu = 0
cos = 0
for i in range(int(ndp)):
    x = input("eixo x:")
    y = input("eixo y:")
    x = int(x)
    y = int(y)
    if(-10000<=x<=10000 and -10000<=y<=10000):
        X.append(x)
        Y.append(y)
    else:
        print("ta erado faz de novo:")
        i = i - 1
for i in range(360):
    angulo = i
    angulo = math.radians(angulo)
    for j in range (len(X)):
        x_atu = X[j]
        y_atu = Y[j]
        if(j+1 == len(X)):
            m = (Y[1] - y_atu)/(X[1] - x_atu)
            m = math.atan(m)
            m = math.radians(m)
        else:
            m = (Y[j+1] - y_atu)/(X[j+1] - x_atu)
            m = math.atan(m)
        angulo = angulo + m
        angulo = math.radians(angulo)
        tempo_atu = math.sqrt((y_atu - Y[j])**2 + (x_atu - X[j])**2)
        y_atu = Y[j]
        x_atu = X[j]
        if(math.cos(angulo) < 0):
            cos = 0
        else:
            cos = math.cos(angulo)
        sol = sol + (cos * tempo_atu)
        print(sol)
    if(sol < sol_ab):
        sol_ab = sol
print(sol_ab)
