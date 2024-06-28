###### Gonzalo Pavez Barrales RUT: 18.778.164-7


class Estudiante:

    def __init__(self, rut, nombre, apellido, edad, materia, notas=None):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.materia = materia
        self.notas = notas if notas is not None else []
        self.promedio = 0.0
        self.estado = "Reprobado"

    def promedios(self):
        if len(self.notas) == 2:
            self.promedio = (self.notas[0] +
                              self.notas[1] ) /2
            self.estado = "Aprobado" if self.promedio >= 4.0 else "Reprobado"

    def describe(self):
        print(f"Estudiante:")
        print(f"Rut: {self.rut}")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Nota: {self.promedio:.2f}")
        print(f"Estado: {self.estado}")
        print(f"Materia: {self.materia}")

def registro_usuario(estudiantes):
    rut = input("Ingrese el RUT del alumno: \n")
    nombre = input("Ingrese nombre del alumno: \n")
    apellido = input("Ingrese apellido del alumno: \n")
    edad = input("Ingrese edad del alumnos: \n")
    materia = input("Ingrese la materia: \n")
    estudiante = Estudiante(rut, nombre, apellido, edad, materia)
    estudiantes.append(estudiante)

def registro_notas(estudiantes):
    rut = input("Ingrese el rut del estudiante: \n")
    for estudiante in estudiantes:
        if estudiante.rut == rut:
            print(f"Ingrese las notas del estudiante {estudiante.nombre} {estudiante.apellido}")
        notas = []
        for i in range(2):
            nota = float(input(f"Ingrese la nota {i+1}: "))
            while nota < 1 or nota > 7:
                print("Nota invalida, ingrese una nota entre 1 y 7")
                nota = float(input(f"Ingrese la nota {i+1}: "))
            notas.append(nota)
        estudiante.notas = notas
        estudiante.promedios()
        return
    print("Alumno no encontrado")

def listar_notas_alumnos(estudiantes):
    print("******Notas Estudiantes******")
    for estudiante in estudiantes:
        estudiante.describe()

def menu():
    estudiantes = []
    while True:
        print("******Bienvenido a la aplicacion de sistema de Notas******")
        print("1.-Ingrese un Alumno")
        print("2.-Ingresar notas de Alumno")
        print("3.-Listar notas de Alumnos")
        print("4.-Salir")

        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            registro_usuario(estudiantes)
        elif opcion == "2":
            registro_notas(estudiantes)
        elif opcion == "3":
            listar_notas_alumnos(estudiantes)
        elif opcion == "4":
            print("Saliendo de la aplicacion")
            break
        else:
            print("Opcion invalida, por favor ingrese una opcion valida")


if __name__ == "__main__":
    menu()
