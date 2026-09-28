estudiantes = {}

estudiantes["Maria"] = float(input("Ingrese la nota de Maria: "))
estudiantes["Belen"] = float(input("Ingrese la nota de Belen: "))
estudiantes["Ana"] = float(input("Ingrese la nota de Ana: "))

print("Estudiantes registrados:")

for nombre, nota in estudiantes.items():
    print(nombre, "tiene una nota de", nota)

buscar = input("Ingrese un nombre para buscar: ")

if buscar in estudiantes:
    print("La nota de", buscar, "es", estudiantes[buscar])
else:
    print("El estudiante no está registrado")