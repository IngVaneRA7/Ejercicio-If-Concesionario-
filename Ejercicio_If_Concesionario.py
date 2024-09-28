"""
Ejercicio solo usando if

Bueno, trabajas en una concesionaria de carros donde permiten modificar el vehículo a lo que quiere el cliente, entonces tienes:

Sedan 5 puertas: 30.000
4x4 5 puertas: 50.000
Convertible 2 puertas: 60.000
Deportivo 2 puertas: 80.000

4 llantas todoterreno: 500
4 llantas deportivas: 800
Llantas de serie: 0

Alerón: 200
Sin alerón: 0

Color rojo: 200
Color azul: 200
Color blanco: 0
Color verde: 200
Color negro: 100

"""

# Precios tipos de vehículos
precio_sedan = 30000
precio_4x4 = 50000
precio_convertible = 60000
precio_deportivo = 80000

# Precios tipos de llantas
llantas_todoterreno = 500
llantas_deportivas = 800
llantas_de_serie = 0

# Precios por alerón
aleron_si = 200
aleron_no = 0

# Precios por color
color_rojo = 200
color_azul = 200
color_blanco = 0
color_verde = 200
color_negro = 100

# Elección del tipo de vehículo
vehiculo = input("Elige el tipo de vehículo (sedan, 4x4, convertible, deportivo): ").lower()

if vehiculo == "sedan":
    precio_base = precio_sedan
elif vehiculo == "4x4":
    precio_base = precio_4x4
elif vehiculo == "convertible":
    precio_base = precio_convertible
elif vehiculo == "deportivo":
    precio_base = precio_deportivo
else:
    print("Opción no válida")
    precio_base = 0

# Elección de llantas
llantas = input("Elige el tipo de llantas (todoterreno, deportivas, serie): ").lower()

if llantas == "todoterreno":
    precio_llantas = llantas_todoterreno
elif llantas == "deportivas":
    precio_llantas = llantas_deportivas
elif llantas == "serie":
    precio_llantas = llantas_de_serie
else:
    print("Opción no válida")
    precio_llantas = 0

# Elección de alerón
aleron = input("¿Quieres alerón? (si/no): ").lower()

if aleron == "si":
    precio_aleron = aleron_si
elif aleron == "no":
    precio_aleron = aleron_no
else:
    print("Opción no válida")
    precio_aleron = 0

# Elección del color
color = input("Elige el color del vehículo (rojo, azul, blanco, verde, negro): ").lower()

if color == "rojo":
    precio_color = color_rojo
elif color == "azul":
    precio_color = color_azul
elif color == "blanco":
    precio_color = color_blanco
elif color == "verde":
    precio_color = color_verde
elif color == "negro":
    precio_color = color_negro
else:
    print("Opción no válida")
    precio_color = 0

# Precio total del vehículo con las modificaciones
precio_total = precio_base + precio_llantas + precio_aleron + precio_color

# Resultado
print(f"El precio total del vehículo configurado es: ${precio_total}")
