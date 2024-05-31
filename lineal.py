# numeros = [1, 2, 3, 7, 234, 5, 6, 2, 1, 23, 23, 52, 5, 34, 3, 34, 23]

def busqueda_lineal(l, e):
    element = None
    position = 0

    # Se recorre la lista uno por uno cada elemento y si se encuentra se guarda junto con la posición.
    for i, v in enumerate(l, start=0):
        if (v == e):
            element = v
            position = i
            break
    
    # Si no se encuentra el elemento, devuelve el mensaje 'Elemento no encontrado'
    if (element == None):
        return 'Elemento no encontrado'

    # si se encuntra el elemento se devuelve junto con su posición.
    return f"Elemento '{element}' encontrado en la posición {position}"

# print(busqueda_lineal(numeros, 23))