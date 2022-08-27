from ntpath import join
import random
from sys import audit


pp=0
mm=0
d = 0
dd = 1
AA=0
a=0
Resultado=0
def calculo(N1, N2, N0):
    global Resultado
    if N0 > 0:
        Resultado=N1+N2
    if N0 < 0:
        Resultado=N1-N2
def comprobador():
    global mejor
    global AA
    global RR
    if mejor <= res[zz]:
        mejor = (mejor -10000) * -1
    if int(Resultado) < res[zz] + mejor and int(Resultado) > res[zz] - mejor and int(Resultado) != mejor:
        if AA < 20 and dd < 50:
            mejor = int(Resultado)
            saf()
            AA +=1
        else:
            if int(Resultado) == res[zz] and dd < 50:
                AA=0
                mejor = int(Resultado)
                saf()
            else:
                RR = 0
                saturar()
    else:
        RR = 0
        saturar()
def saturar():
    global d
    global AA
    global au
    global a
    load()
    au+=1
    if au > 5:
        d += 1
        au=0
    if d > p:
        a = d
        madi = 0
        while a > p:
            AA=0
            img = random.uniform(-1 , 1)
            madi = random.randint(0 , p)
            peso[madi] = img
            a -= 1
    else:
        madi = 0
        img = random.uniform(-1 , 1)
        madi = random.randint(p - d - 1 , p-1)
        peso[madi] = img
def saf():
    global dd
    print(stard[zz],"OK","%",mejor,"R>>",RR)
    print(RR,"/R",":", int(Resultado))
    reg = open("sintaxis.txt", "w")
    reg.write(str(Fi) + "|" + str(Co) + "|" + str(mejor) + "\n" + pio)
    reg.close()
    global d
    d=dd
def load():
    global pp
    global mm
    global peso
    print("NO",AA,"D:",d)
    reg = open("sintaxis.txt", "r")
    r=reg.readlines()
    pp=r[0].split("|")
    mm=r[1].split("|")
    reg.close()
    peso = mm
def redNeuronal():
    global pio
    global p
    global nodo
    x = 0
    n = 0
    c = 0
    z = 0
    p = 0
    pio = ""
    while c < Fi:
        nodo[c] = 0
        c += 1
    while n < Co:
        if c >= Fi:
            c = 0
        while c < Fi:
            if nodo[c] != 0:
                entrada[c] = nodo[c]
                nodo[c] = 0
            c += 1
        if z >= Fi:
            z = 0
        while z < Fi:
            if x >= Fi:
                x = 0
            while x < Fi:
                nodo[z] += float(peso[p]) * float(entrada[x])
                pio += str(peso[p])
                if p < (Fi * Fi) * Co: pio += "|"
                p += 1
                x += 1
            while nodo[z] > Fi: nodo[z] -= Fi
            z += 1
        n += 1
    calculo(nodo[0],nodo[1],nodo[2])
#
load()
#
print(pp)
print(mm)
Fi = int(pp[0])
Co = int(pp[1])
entrada = list(range(Fi))

nodo = list(range(Fi * Co))
peso = list(range((Fi * Fi) * Co))
mejor = int(pp[2])
pio = ""
load()
#
zz=0
reg = open("situaciones.txt", "r")
r=reg.readlines()
situ = len(r)
x = 0
stard=list(range(situ))
res=list(range(situ))
mmm=list(range(len(r)))
while x < situ:
    mmm[x]=r[x].split("=")
    stard[x]=mmm[x][0].split("|")
    res[x]=int(mmm[x][1])
    x+= 1
reg.close()
#
print(res)
y = 0
comando = input("comando:>")
if comando == "crear":
    mejor = 100000
    Fi = int(input("filas:"))
    Co = int(input("colugnas:"))
    peso = list(range((Fi * Fi) * Co))
    entrada = list(range(Fi))
    nodo = list(range(Fi))
    while y < (Fi * Fi) * Co:
        peso[y] = 0
        y += 1
    e = 0
    while e < Fi:
        stard = list(range(Fi))
        if entrada[e] != "f":
            entrada[e] = input("entrada "+ str(e + 1) + "/" + str(Fi) + ":")
        if entrada[e] == "f":
            img = random.uniform(0 , 1)
            entrada[e] = img
            if e < Fi-1:
                entrada[e + 1] = "f"
        e += 1
else:
    e = 0
    while e < Fi:
        if entrada[e] != "f":
            entrada[e] = input("entrada "+ str(e + 1) + "/" + str(Fi) + ":")
        if entrada[e] == "f":
            entrada[e] = 0
            if e < Fi-1:
                entrada[e + 1] = "f"
        #print(entrada[e])
        e += 1

print("#--------------------#")
#---Prinsipal--------------
zz = random.randint(0 , situ-1)
RR = 0
au=0
p = 0

redNeuronal()
print(stard[zz],"OK","%",mejor,"R>>",RR)
print(RR,"/R",":", int(Resultado))

salir = False
comando = input("esta correcto?>")
while salir == False:
    if comando == "s":
        saf()
        salir = True
    if comando == "n":
        img = random.uniform(0 , 1)
        print("<----+",p,"+---->")
        peso[p - d] = img
        d += 1
        comando = "1"
        e = 0
        while e < Fi:
            entrada[e] = stard[zz][e]
            e += 1
        redNeuronal(Fi, Co)
    if comando == "a":
        if int(Resultado) == res[zz]:
            RR += 1
            AA=0
            dd+=1
            d+=dd
            zz = random.randint(0 , situ-1)
            if RR >= 10:
                saf()
                salir = True
        if int(Resultado) != res[zz]:
            comprobador()
            e = 0
            while e < Fi:
                entrada[e] = 0
                if e < 3:
                    entrada[e] = stard[zz][e]
                #print(entrada[e])
                e += 1
            redNeuronal()