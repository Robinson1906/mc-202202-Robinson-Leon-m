from audioop import mul
from math import factorial



menu=["1: Operacion 1 ","2: Operacion 2 ","3: SALIR" ]

num=0.85
errorS=(0.5*(10**-8))*100
e=0
anterior=1
errorA=1
iteraciones=0
signo=-1
expo=1
valorAnterior=1

for i in menu:
    print(i)

opc=input("Elija una opcion: ")

if opc=="1":
    while errorA>=errorS:
        multiplicacion=signo*((num**expo)/factorial(expo))
        e=anterior+multiplicacion
        errorA=100*(abs((e-anterior)/e))
        
        signo*=-1
        expo+=1
        iteraciones+=1
        anterior=e

elif opc=="2":
    while errorA>=errorS:
        multiplicacion=(num**expo)/factorial(expo)
        serie=anterior+multiplicacion
        e=1/serie
        errorA=100*(abs((e-valorAnterior)/e))
        
        
        expo+=1
        iteraciones+=1
        anterior=serie
        valorAnterior=e
       
else: 
    print("La opcion no es valida")

    
print("El valor final es: ", e)
print("El error final fue de: ", errorA)
print("Se realizaron: ", iteraciones," iteraciones")