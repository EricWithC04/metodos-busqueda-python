# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 170]

def busqueda_binaria(l, min, max, e):
    
    # Se obtiene la posición de enmedio de la lista
    half = (min + max) // 2

    # Si se encuentra se devuelve el elemento junto con su posición
    if (l[half] == e):
        return f"Elemento {l[half]} encontrado en la posicion {half}"
    
    # Si la posicion de enmedio es igual al maximo, significa que la sublista ya no le quedan elementos para buscar, por lo tanto, no se encontró el elemento
    if (half == max):
        return 'Elemento no encontrado'

    # Se invoca la función recursivamente con una sublista dependiendo de si el elemento a buscar es menor o mayor al buscado
    if (l[half] < e):
        return busqueda_binaria(l, half+1, max, e)
    if (l[half] > e):
        return busqueda_binaria(l, min, half-1, e)

# print(busqueda_binaria(numeros, 0, len(numeros)-1, 170))