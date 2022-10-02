import numpy as np

A = np.array([[3,2,2],
              [3,1,-3],
              [1,0,-2]], dtype=float)

casicero = 1e-15 
tamano = np.shape(A)
n = tamano[0]
identidad = np.identity(n)

AB = np.concatenate((A,identidad),axis=1)
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
    adelante = i+1
    for k in range(adelante,n,1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
AB2 = np.copy(AB)

ultfila = n-1
ultcolumna = m-1
for i in range(ultfila,0-1,-1):
    pivote = AB[i,i]
    atras = i-1 
    for k in range(atras,0-1,-1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
    AB[i,:] = AB[i,:]/AB[i,i]
inversa = np.copy(AB[:,n:])

C = np.array([[1,2,0,4],
              [2,0,-1,-2],
              [1,1,-1,0],
              [0,4,1,0]], dtype=float)

casicero = 1e-15 
tamano = np.shape(C)
n = tamano[0]
identidad = np.identity(n)

CD = np.concatenate((C,identidad),axis=1)
CD0 = np.copy(CD)

tamano = np.shape(CD)
n = tamano[0]
m = tamano[1]

for i in range(0,n-1,1):
    
    columna = abs(CD[i:,i])
    dondemax = np.argmax(columna)
    if (dondemax !=0):
        temporal = np.copy(CD[i,:])
        CD[i,:] = CD[dondemax+i,:]
        CD[dondemax+i,:] = temporal
CD1 = np.copy(CD)

for i in range(0,n-1,1):
    pivote = CD[i,i]
    adelante = i+1
    for k in range(adelante,n,1):
        factor = CD[k,i]/pivote
        CD[k,:] = CD[k,:] - CD[i,:]*factor
AB2 = np.copy(CD)

ultfila = n-1
ultcolumna = m-1
for i in range(ultfila,0-1,-1):
    pivote = CD[i,i]
    atras = i-1 
    for k in range(atras,0-1,-1):
        factor =CD[k,i]/pivote
        CD[k,:] = CD[k,:] - CD[i,:]*factor
    CD[i,:] = CD[i,:]/CD[i,i]

inversa1 = np.copy(CD[:,n:])

print('Inversa de A: ')
print(inversa)
print('Inversa de C: ')
print(inversa1)