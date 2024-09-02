# Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.
# Escribe un programa que incluya una matriz bidimensional (puede ser una matriz pequeña de 3x3) con valores numéricos.
matriz_bidimensional = [
    [6, 16, 26],
    [3, 13, 23],
    [9, 19, 29]
]


# Implementa una función que realice una búsqueda en la matriz para encontrar un valor específico que definas.
def busqueda_lineal(numero_a_buscar, matriz_bidimensional):
    for fila in range(len(matriz_bidimensional)):
        for columna in range(len(matriz_bidimensional[fila])):
            if matriz_bidimensional[fila][columna] == numero_a_buscar:
                print("Felicidades, se encontró el número: ", numero_a_buscar, " en la fila: ", fila, " y la columna: ",
                      columna)
                return
    print("No se encontró el número: ", numero_a_buscar, " en el arreglo.")


# Muestra un mensaje que indique si el valor se encontró o no, y muestra su posición en la matriz si se encontró.
numero_a_buscar = int(input("Ingrese el número a buscar: "))

busqueda_lineal(numero_a_buscar, matriz_bidimensional)


