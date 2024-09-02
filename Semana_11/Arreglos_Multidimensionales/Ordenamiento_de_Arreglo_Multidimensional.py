# Crea un nuevo proyecto en PyCharm y un archivo Python para este programa
# Escribe un programa que incluya una matriz bidimensional con valores numéricos (puede ser una matriz pequeña de 3x3).

matriz_numerica = [
    [15, 11, 35],
    [32, 71, 18],
    [9, 22, 4]
]

# Implementa una función que ordene una fila específica de la matriz en orden ascendente utilizando un algoritmo de
# ordenación de tu elección (por ejemplo, Bubble Sort o QuickSort).
def ordenador_numerico(posicion_fila_selecionada, matriz_numerica):
    fila_seleccionada = matriz_numerica[posicion_fila_selecionada]
    cambios = True
    while cambios == True:
        for iterador in range(len(fila_seleccionada) - 1):
            if fila_seleccionada[iterador] > fila_seleccionada[iterador + 1]:
                variable_temporal = fila_seleccionada[iterador + 1]
                fila_seleccionada[iterador + 1] = fila_seleccionada[iterador]
                fila_seleccionada[iterador] = variable_temporal
                cambios = True
            else:
                cambios = False

    matriz_numerica[posicion_fila_selecionada] = fila_seleccionada

# Muestra la matriz original y la matriz con la fila ordenada.
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

numero_correcto = False
while (numero_correcto == False):
    posicion_fila_selecionada = int(input("Ingrese la posición de la fila ha ordenar: "))
    if (posicion_fila_selecionada > len(matriz_numerica) or posicion_fila_selecionada < 0):
        print("Vuelve a ingresar el número de la posición de la fila ha ordenar, Por favor!")
    else:
        numero_correcto = True

print("Matriz original: ")
mostrar_matriz(matriz_numerica)

ordenador_numerico(posicion_fila_selecionada, matriz_numerica)

print("Matriz ordenada: ")
mostrar_matriz(matriz_numerica)
