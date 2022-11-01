from math import sqrt
import os
import numpy as np
def REGRESION(x=list,y=list):
        xy=[]
        x2=[]
        sum_x=sum(x)
        sum_y=sum(y)
        prom_x=(sum_x/len(x))
        prom_y=(sum_y/len(y))
        for i in range(len(x)):
            xy.append(x[i]*y[i])
        sum_xy=sum(xy)
        for i in range(len(x)):
            x2.append(x[i]*x[i])
        sum_x2=sum(x2)
        m=((len(x)*(sum_xy))-(sum_x*sum_y)/((len(x)*sum_x2)-(sum_x*sum_x)))
        b=prom_y-m*prom_x
        print(f"\n\nLa ecuación de la recta de la regresión lineal es y = {m}x+({b})\n\n")
        return [m,b]
def MODELOEXP(x=list,y=list):
        log_y = np.log(y)
        coefficients = np.polyfit(x, log_y, 1)
        return coefficients
def ECUACIONES(x,y):
    log_x = np.log(x,10)
    log_y = np.log(y,10)
    coefficients = np.polyfit(log_x,log_y,1)
    return coefficients
def RAZONES(x,y):
    for i in range(len(x)):
         x_inv=[]
         y_inv=[]
         x_inv.append(1/x[i])
         y_inv.append(1/y[i])
         coefficients = np.polyfit(x_inv,y_inv,1)
         return coefficients
 
x=[1,3,5,7,9,11,13,15]
y=[2.1,3.2,3.8,4,4.2,4.4,4.5,4.7]
xnp=np.array(x)
ynp=np.array(x)
print("X    -   Y\n")
for i in range(len(x)):
    print(f"{x[i]}    -   {y[i]}")
print(f"MÍNIMOS CUADRADOS: y = {REGRESION[0]}x+({REGRESION[1]})\n")
print(f"MODELO EXPONECIAL: y = {MODELOEXP(xnp,ynp)[0]}x+({MODELOEXP(xnp,ynp)[1]})")
print(f"ECUACIONES DE POTENCIA: y = {ECUACIONES(xnp,ynp)[0]}x+({ECUACIONES(xnp,ynp)[1]}")
print(f"RAZÓN DE CAMBIO: y = y = {RAZONES(x,y)[0]}x+({RAZONES(x,y)[1]}")