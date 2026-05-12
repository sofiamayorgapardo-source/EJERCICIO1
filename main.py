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