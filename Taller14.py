import numpy as np 
import os

A = np.array([[1,0,1],
              [3,4,3],
              [4,1,0]])

B = np.array([[2.5],
              [11.5],
              [15.0]])

casicero = 1e-15 
AB = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

for i in range(0,n-1,1):
    columna = abs(AB[i:,i])
    dondemax = np.argmax(columna)
    if (dondemax !=0):
        temporal = np.copy(AB[i,:])
        AB[i,:] = AB[dondemax+i,:]
        AB[dondemax+i,:] = temporal
AB1 = np.copy(AB)
for i in range(0,n-1,1):
    pivote = AB[i,i]
    adelante = i + 1
    for k in range(adelante,n,1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
AB2 = np.copy(AB)
ltfila = n-1
ultcolumna = m-1
for i in range(ltfila,0-1,-1):
    pivote = AB[i,i]
    atras = i-1 
    for k in range(atras,0-1,-1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
    AB[i,:] = AB[i,:]/AB[i,i]
X = np.copy(AB[:,ultcolumna])
X = np.transpose([X])

os.system('cls')
print(f"La matriz A es: \n {A}\n")
print(f"La matriz B es: \n {B}\n")
print(f"La matriz resultado es \n{X}")