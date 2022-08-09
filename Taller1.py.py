from operator import add
import os
from this import s

def tryInt(txt:str):#metodo para leer datos enteros
    isTry=True
    while isTry:
        try:
            x=int(input(txt))
        except:
            print("No es valido, ingrese nuevamente el dato")
        else:
            isTry=False
            return x


M = set()
L = set()
print()

# M={1,2,3,4}
# L={4,5,6,7}
os.system('cls')
conj=tryInt("introdusca la cardinalidad de su primer conjunto ")

print("ingrese los elementos del conjunto M")
RL= 0
while RL!=conj:
    RL+=1
    x=input(":)")
    L.add(x)

conj1=tryInt("introdusca la cardinalidad de su segundo conjunto ")

print("ingrese los elementos del conjunto L")

ML= 0
while ML!=conj1:
    ML+=1
    x=input(":)")
    M.add(x)

op= 0

while op!=5:
    os.system('pause')
    os.system('cls')
    op=int(input("1.union \n2.interseccion \n3.diferencia \n4.diferencia simetrica \n5.salir\n:) "))
    if (op==1):
        union=set()

        for i in M:
 
            union.add(i)
        for i in L:

            union.add(i)
        
        print(union)
        print("la cantidad de elementos es: ",len(union))
        
    elif (op==2):
        inter=set()

        for i in M:
            if i in L:
                inter.add(i)
        print(inter)
        print("la cantidad de elementos es: ",len(inter))       

        
    elif (op==3):
        
        inter=set()

        for i in M:
            if not(i in L):

                inter.add(i)
        print(inter)
        print("la cantidad de elementos es: ",len(inter))

    elif (op==4):
        sim=set()

        union=set()

        for i in M:
 
            union.add(i)
        for i in L:

            union.add(i)
        
        inter=set()

        for i in M:
            if i in L:
                inter.add(i)
        
        for i in union:
            if not(i in inter):

                sim.add(i)
        print(sim)
        print("la cantidad de elementos es: ",len(sim))

        
    elif (op==5):
        pass
 