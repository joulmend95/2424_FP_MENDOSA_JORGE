# Abre el archivo 'my_notes.txt' en modo de escritura ('w'). Si el archivo no existe, lo crea.
my_notes = open('my_notes.txt', 'w')

# Escribe varias líneas de texto en el archivo con información personal
my_notes.write("Soy de la ciudad de Santo Domingo.\n")
my_notes.write("Vivo en una parroquia rural llamada El Esfuerzo.\n")
my_notes.write("Para ir al trabajo viajo en moto.\n")
my_notes.write("Me gusta la chuleta a la plancha.\n")
my_notes.write("Disfruto ir de viaje durante las vacaciones.\n")

# Cierra el archivo después de la escritura para asegurar que los cambios se guarden.
my_notes.close()

# Abre el archivo 'my_notes.txt' en modo de lectura ('r') para leer su contenido.
my_notes = open('my_notes.txt', 'r')

# Lee el archivo línea por línea usando readlines() y muestra el contenido en la consola.
# rstrip() elimina el salto de línea al final de cada línea.

for linea in my_notes.readlines():
    print(linea.rstrip('\n'))  # Imprime cada línea sin el salto de línea adicional.

# Cierra el archivo después de la lectura para liberar los recursos.
my_notes.close()
