# 1. Crear un diccionario llamado 'informacion_personal' con información ficticia
informacion_personal = {
    "Nombre": "Jorge Mendosa",  # Almacena el nombre de la persona
    "Edad": 28,  # Almacena la edad de la persona
    "Ciudad": "Santo Domingo",  # Almacena la ciudad de residencia
    "Profesion": "Funcionario Público"  # Almacena la profesión de la persona
}

# 2. Imprimir el diccionario inicial
print(informacion_personal)  # Muestra la información del diccionario

# 3. Modificar el valor asociado con la clave 'Ciudad'
informacion_personal["Ciudad"] = "Quito"  # Cambia la ciudad a "Quito"

# 4. Imprimir el diccionario después de la modificación
print(informacion_personal)  # Muestra el diccionario con la ciudad modificada

# 5. Modificar el valor asociado con la clave 'Profesion'
informacion_personal["Profesion"] = "Asistente de Atención al usuario"  # Actualiza la profesión

# 6. Verificar si la clave 'Telefono' no existe en el diccionario
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "+5931256001"  # Agrega un número de teléfono ficticio si no existe

# 7. Imprimir el diccionario después de agregar el teléfono
print(informacion_personal)  # Muestra el diccionario con la nueva clave 'Telefono'

# 8. Eliminar la clave 'Edad' del diccionario
del informacion_personal["Edad"]  # Elimina la clave 'Edad'

# 9. Iterar sobre las claves y valores del diccionario e imprimirlos
print("\nDICCIONARIO DE INFORMACIÓN PERSONAL")
for clave, valor in informacion_personal.items():
    print(clave, ":", valor)  # Imprime cada clave y su valor correspondiente en el formato "clave : valor"
