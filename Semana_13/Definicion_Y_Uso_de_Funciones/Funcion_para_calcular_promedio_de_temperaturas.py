# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"dia": "Lunes", "temperatura": 78},
            {"dia": "Martes", "temperatura": 80},
            {"dia": "Miércoles", "temperatura": 82},
            {"dia": "Jueves", "temperatura": 79},
            {"dia": "Viernes", "temperatura": 85},
            {"dia": "Sábado", "temperatura": 88},
            {"dia": "Domingo", "temperatura": 92}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temperatura": 76},
            {"dia": "Martes", "temperatura": 79},
            {"dia": "Miércoles", "temperatura": 83},
            {"dia": "Jueves", "temperatura": 81},
            {"dia": "Viernes", "temperatura": 87},
            {"dia": "Sábado", "temperatura": 89},
            {"dia": "Domingo", "temperatura": 93}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temperatura": 77},
            {"dia": "Martes", "temperatura": 81},
            {"dia": "Miércoles", "temperatura": 85},
            {"dia": "Jueves", "temperatura": 82},
            {"dia": "Viernes", "temperatura": 88},
            {"dia": "Sábado", "temperatura": 101},
            {"dia": "Domingo", "temperatura": 95}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temperatura": 75},
            {"dia": "Martes", "temperatura": 78},
            {"dia": "Miércoles", "temperatura": 80},
            {"dia": "Jueves", "temperatura": 79},
            {"dia": "Viernes", "temperatura": 84},
            {"dia": "Sábado", "temperatura": 87},
            {"dia": "Domingo", "temperatura": 101}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"dia": "Lunes", "temperatura": 62},
            {"dia": "Martes", "temperatura": 64},
            {"dia": "Miércoles", "temperatura": 68},
            {"dia": "Jueves", "temperatura": 70},
            {"dia": "Viernes", "temperatura": 73},
            {"dia": "Sábado", "temperatura": 75},
            {"dia": "Domingo", "temperatura": 79}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temperatura": 63},
            {"dia": "Martes", "temperatura": 66},
            {"dia": "Miércoles", "temperatura": 70},
            {"dia": "Jueves", "temperatura": 72},
            {"dia": "Viernes", "temperatura": 75},
            {"dia": "Sábado", "temperatura": 77},
            {"dia": "Domingo", "temperatura": 81}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temperatura": 61},
            {"dia": "Martes", "temperatura": 65},
            {"dia": "Miércoles", "temperatura": 68},
            {"dia": "Jueves", "temperatura": 70},
            {"dia": "Viernes", "temperatura": 72},
            {"dia": "Sábado", "temperatura": 76},
            {"dia": "Domingo", "temperatura": 80}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temperatura": 64},
            {"dia": "Martes", "temperatura": 67},
            {"dia": "Miércoles", "temperatura": 69},
            {"dia": "Jueves", "temperatura": 71},
            {"dia": "Viernes", "temperatura": 74},
            {"dia": "Sábado", "temperatura": 77},
            {"dia": "Domingo", "temperatura": 80}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"dia": "Lunes", "temperatura": 90},
            {"dia": "Martes", "temperatura": 92},
            {"dia": "Miércoles", "temperatura": 94},
            {"dia": "Jueves", "temperatura": 101},
            {"dia": "Viernes", "temperatura": 88},
            {"dia": "Sábado", "temperatura": 85},
            {"dia": "Domingo", "temperatura": 82}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temperatura": 89},
            {"dia": "Martes", "temperatura": 101},
            {"dia": "Miércoles", "temperatura": 93},
            {"dia": "Jueves", "temperatura": 90},
            {"dia": "Viernes", "temperatura": 87},
            {"dia": "Sábado", "temperatura": 84},
            {"dia": "Domingo", "temperatura": 81}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temperatura": 101},
            {"dia": "Martes", "temperatura": 93},
            {"dia": "Miércoles", "temperatura": 95},
            {"dia": "Jueves", "temperatura": 92},
            {"dia": "Viernes", "temperatura": 89},
            {"dia": "Sábado", "temperatura": 86},
            {"dia": "Domingo", "temperatura": 83}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temperatura": 88},
            {"dia": "Martes", "temperatura": 90},
            {"dia": "Miércoles", "temperatura": 92},
            {"dia": "Jueves", "temperatura": 89},
            {"dia": "Viernes", "temperatura": 86},
            {"dia": "Sábado", "temperatura": 83},
            {"dia": "Domingo", "temperatura": 80}
        ]
    ]
]


# Función para calcular el promedio de temperaturas
def calcular_promedio_de_temperaturas(temperaturas):
    # Inicializa el número de la ciudad y de la semana
    numero_ciudad = 0
    numero_semana = 0

    # Iterar sobre cada ciudad en la matriz de temperaturas
    for ciudad in temperaturas:
        numero_ciudad += 1  # Incrementa el contador de ciudades
        print("Ciudad:", numero_ciudad)

        # Iterar sobre cada semana en la ciudad actual
        for semana in ciudad:
            numero_semana += 1  # Incrementa el contador de semanas
            suma = 0  # Inicializa la suma de temperaturas para la semana

            # Iterar sobre cada día de la semana para sumar las temperaturas
            for dia in semana:
                suma = suma + dia["temperatura"]

            # Calcular el promedio dividiendo la suma entre el número de días en la semana
            promedio = suma / len(semana)

            # Imprimir el promedio de la semana actual
            print("El promedio de la semana ", numero_semana, " es: ", f"{promedio:.2f}")

        # Reinicia el contador de semanas para la siguiente ciudad
        numero_semana = 0


# Llamar a la función para calcular el promedio de las temperaturas
calcular_promedio_de_temperaturas(temperaturas)
