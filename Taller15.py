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
inversa = np.copy(AB[:,n:])

C = np.array([[1,2,0,4],
              [2,0,-1,-2],
              [0,4,1,0]], dtype=float)

casicero = 1e-15 
tamano = np.shape(A)
n = tamano[0]
identidad = np.identity(n)
CD = np.concatenate((C,identidad),axis=1)
CD0 = np.copy(CD)
tamano = np.shape(CD)
inversa1 = np.copy(CD[:,n:])

print('Inversa de A: ')
print(inversa)
print("inversa de C:")
print(inversa1)
