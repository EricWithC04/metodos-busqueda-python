# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 170]

def busqueda_binaria(l, min, max, e):
    
    half = (min + max) // 2

    if (l[half] == e):
        return f"Elemento {l[half]} encontrado en la posicion {half}"
    
    if (half == max):
        return 'Elemento no encontrado'

    if (l[half] < e):
        return busqueda_binaria(l, half+1, max, e)
    if (l[half] > e):
        return busqueda_binaria(l, min, half-1, e)

# print(busqueda_binaria(numeros, 0, len(numeros)-1, 170))