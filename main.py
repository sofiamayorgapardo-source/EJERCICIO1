input("Bienvenidos al programa para saber tus nota Su continuacion sigue los pasos a seguir gracias por usar nuetro programa te lo ageradesco de corazon")
# Menú de opciones
print("1. Ingresar varios estudiantes")
print("2. Ingresar un solo estudiante")
# Proceso para ingresar estudiantes
for e in range(cantidad):

    print(f" Estudiante #{e + 1}")
# Si elige varios estudiantes
if opcion == 1:
    cantidad = int(input("¿Cuántos estudiantes desea ingresar?: "))

# Si elige un solo estudiante
elif opcion == 2:
    cantidad = 1

# Opción inválida
else:
    print("Opción no válida")
    cantidad = 0
        # Solicitar nombre
    nombre = input("Ingrese el nombre del estudiante: ")

    # Lista para guardar las notas
    notas = []

    # Solicitar 5 notas
    for i in range(5):
        nota = float(input(f"Ingrese la nota #{i + 1}: "))
        notas.append(nota)

    # Calcular promedio
    promedio = sum(notas) / 5

    # Mostrar resultados
    print("Resultado")
    print("Estudiante:", nombre)
    print("Notas:", notas)
    print("Promedio:", promedio)

    # Evaluar desempeño
    if promedio >= 4.5:
        print("Estado: Excelente")
    elif promedio >= 3.0:
        print("Estado: Aprobado")
     else: print("Estado: Reprobado")
