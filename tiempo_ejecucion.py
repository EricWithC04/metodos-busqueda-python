import time
from lineal import busqueda_lineal as bl
from binaria import busqueda_binaria as bb

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 170, 1000, 3845, 5000, 10000]

# Búsqueda Lineal
inicio1 = time.perf_counter()
print(bl(numeros, 170))
fin1 = time.perf_counter()

# Búsqueda Binaria
inicio2 = time.perf_counter()
print(bb(numeros, 0, len(numeros)-1, 170))
fin2 = time.perf_counter()

# Calculo de los tiempos de ejecución
tiempo1 = fin1 - inicio1
tiempo2 = fin2 - inicio2

# Los tiempos se muestran por consola
print(f'El tiempo de ejecución 1 fue de: {tiempo1} segundos')
print(f'El tiempo de ejecución 2 fue de: {tiempo2} segundos')