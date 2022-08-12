
import os


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


def union(a,b):
        unionC=set()

        for i in b:
 
            unionC.add(i)
        for i in a:

            unionC.add(i)
        
        return unionC

def interseccion(a,b):
    inter=set()

    for i in a:
        if i in b:
            inter.add(i)
    return inter

def dif(a,b):
    inter=set()

    for i in a:
        if not(i in b):

            inter.add(i)
    return inter

def simetrica(a,b):
    sim=set()

    union=set()

    for i in a:

        union.add(i)
    for i in b:

        union.add(i)
    
    inter=set()

    for i in a:
        if i in b:
            inter.add(i)
    
    for i in union:
        if not(i in inter):

            sim.add(i)
    return sim



# M={1,2,3,4}
# L={4,5,6,7}
a={6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
b={2,4,6,8,10,12,14,16,18,20,22,24}
c={1,4,8,10,12,15,18,20}
d={2,3,5,7,11,13,17,19,23,29,31,37,41,43}
os.system('cls')

op= 0
while op!=5:
    os.system('pause')
    os.system('cls')


    op=tryInt("1.operacionA \n2.operacionB \n3.operacionC \n4.operacionD \n5.salir\n:) ")
    if (op==1):
        sim=simetrica(c,d)
        final=interseccion(b,sim)
        print("Resultado: ")
        print(final)

    elif (op==2):
        
        inte=interseccion(a,c)
        final=union(b,inte)
        print("Resultado: ")
        print(final)

        
    elif (op==3):
        
        uni=union(b,c)
        final=dif(uni,c)
        print("Resultado: ")
        print(final)
        


    elif (op==4):
        
        dife=dif(a,b)
        int=interseccion(a,b)
        sim=simetrica(dife,int)
        print("Resultado: ")
        print(sim)        

        
    elif (op==5):
        pass
 