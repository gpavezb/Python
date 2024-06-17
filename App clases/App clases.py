Class Estudiante:
def __init__(self, rut,nombre,apellido,edad,materia,notas=None):
    self.rut=rut
    self.nombre=nombre
    self.apellido=apellido
    self.edad=edad
    self.materia=materia
    self.notas=notas if notas is not None else []
    self.promedio=0.0
    self.estado="Reprobado"
    


def promedio(self):
    if len(self.notas) ==2:
        self.promedio=(self.notas[0]*0.4 + self.notas[1]*0.4)
        


def registro_usuario(estudiantes):
    rut=input ("Ingrese el RUT del alumno: \n")
    nombre=input("Ingrese nombre del alumno: \n")
    apellido=input("Ingrese apellido del alumno: \n")
    edad=input("Ingrese edad del alumnos: \n")
    materia=input("Ingrese la materia: \n")
    estudiante=Estudiante(rut,nombre,apellido,edad,materia)
    estudiante.append(estudiante)
