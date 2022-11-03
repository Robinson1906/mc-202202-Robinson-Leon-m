import copy
from itertools import count
import math
from re import A
import re

x = [0, 1, 2, 3, 4, 5, 6]
y = [-0.9, 0, 2, 4.5, 8.3, 13, 18]

sumX = 0
sumX2 = 0
sumX3 = 0
sumX4 = 0
sumY = 0
sumXY = 0
sumX2Y = 0
st = 0
sr = 0

for i in range(len(x)) :
    sumX += x[i]
    sumX2 += (x[i])**2
    sumX3 += (x[i])**3
    sumX4 += (x[i])**4
    sumY += y[i]
    sumXY += (x[i]*y[i])
    sumX2Y += ((x[i])**2)*y[i]

promedioY = sumY / len(y)

def matrix_format(matriz, formato):
    n_rows = len(matriz)
    n_cols = len(matriz[0])

    #Determinar el máximo ancho necesario por columna.
    col_max_width = []
    for col in range(n_cols): # Examinar la columna.
        max_width = 0 # Maximo ancho en esta columna
        for row in range(n_rows):
            # Formatear el valor en la celda para 
            # determina su ancho.
            edit_value = formato % matriz[row][col]
            max_width = max(max_width, len(edit_value))
        col_max_width.append(max_width)

    # Ahora que sabemos el ancho necesario por columna,
    # generar la matriz de salida ajustando los anchos
    # de cada valor editado.
    salida = []
    for row in range(n_rows):
        edit_row = []
        for col in range(n_cols):
            #  Primero editar el valor con su formato.
            edit_value = formato % matriz[row][col]
            #  Calcular el numero de espacios para ajustar
            #  a la derecha el valor editado
            edit_space = " "*(col_max_width[col] - len(edit_value))
            edit_row.append("%s%s" % (edit_space, edit_value))
        salida.append(edit_row)
    
    return salida

def imprimirEcuaciones(a, b):
    salida = matrix_format(a, " %.1f")
    i = 0
    for row in salida: 
        for col in row:
            print(col, end="  ")
        print("| " + str(b[i]))
        i += 1


def gaussJordan(a, b):
    aAux = copy.deepcopy(a)
    bAux = copy.deepcopy(b)

    n = len(bAux)

    #Se construye la matriz identidad
    count = 1
    count2 = 1
    for i in range(n):
        if aAux[i][i] == 0:
            for c in range(n):
                if aAux[c][i] != 0:
                    tempA = aAux[i]
                    tempB = bAux[i]
                    aAux[i] = aAux[c]
                    aAux[c] = tempA
                    bAux[i] = bAux[c]
                    bAux[c] = tempB
                    count += 1
        div = aAux[i][i]
        for e in range(n):
            aAux[i][e] /= div
        bAux[i] /= div
        for j in range(n):
            if i != j:
                fact = -aAux[j][i] / aAux[i][i]
                for k in range(n):
                    aAux[j][k] += (aAux[i][k] * fact)

                bAux[j] += (bAux[i] * fact)
                count2 += 1

    return bAux

#Programa principal
a = [[len(x), sumX, sumX2], [sumX, sumX2, sumX3], [sumX2, sumX3, sumX4]]
b = [sumY, sumXY, sumX2Y]

print("\n")
res = gaussJordan(a, b)

#Se imprimen los resultados
for i in range(len(res)):
    print("a" + str(i) + " = " + str(res[i]))

print(f'y = {res[0]} + {res[1]}x + {res[2]}x^2')

for i in range(len(x)):
    st += (y[i] - promedioY)**2
    sr += (y[i] - res[0] - res[1]*x[i] - res[2]*(x[i]**2))**2

sy = math.sqrt(st/(len(x)-1))
sy_x = math.sqrt(sr/(len(x)-3))
r = math.sqrt((st - sr)/st) * 100

print("Desviacion estandar: ", sy)
print("Error estandar: ", sy_x)
print("Coeficiente de correlacion: ", r,"%")
