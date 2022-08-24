import math
#s=1.04719755
s=float(input('Escribe un numero en Radianes'))
ea=100
es=(0.5*pow(10,-8))*100
interacion=0
potencia=2
valor=1
signo=-1

while ea>es:
    operacion=valor+signo*(pow(s,potencia) / math.factorial(potencia))
    ea=abs(100*((operacion-valor)/operacion) )
    
    valor=operacion

    interacion +=1
    potencia +=2
    signo *=-1
    
   
print(f'El valor del coseno es:{valor} iteraciones: {interacion}')
    
