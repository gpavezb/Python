###### Gonzalo Pavez Barrales RUT: 18.778.164-7



from datetime import datetime

class Turista:
    def __init__(self,nombre,nacionalidad,pasaporte,rut,fechaIngreso,diasEstadia,tipoHabitacion):
        self.nombre=nombre
        self.nacionalidad=nacionalidad
        self.pasaporte=pasaporte
        self.rut=rut
        self.fechaIngreso=fechaIngreso
        self.diasEstadia=diasEstadia
        self.tipoHabitacion=tipoHabitacion
        self.consumoHabitacion=[]
    
    def consumo(self,descripcion,cantidad,precio,fechaHora):
        self.consumoHabitacion.append({"Descripcion": descripcion, "cantidad":cantidad, "precio": precio, "fechaHora": fechaHora})

    def calcularTotalEstadia(self):
        if self.tipoHabitacion.lower=='Normal':
            costoPorNoche=50
        elif self.tipoHabitacion=='Premium':
            costoPorNoche=100
        totalEstadia=costoPorNoche*self.diasEstadia

        if self.nacionalidad.lower()=='brasil' and self.diasEstadia >=3:
            totalEstadia*=0.8
        
        return totalEstadia
    
    def calcularTotalConsumo(self):
        totalConsumo=0
        for item in self.consumoHabitacion:
            totalConsumo+=item['precio']*item['cantidad']
        return totalConsumo
    
    def checkout(self):
        totalEstadia=self.calcularTotalEstadia()
        totalConsumo=self.calcularTotalConsumo()
        totalPagar=totalEstadia+totalConsumo
        detalleConsumo="\n".join([f"{item['descripcion']}x{item['cantidad']}-{item['precio']}CLP-{item['fechaHora']}"for item in self.consumoHabitacion])
        salidaDetallada=(f"Nombre: {self.nombre}\n"
                         f"Nacionalidad: {self.nacionalidad}\n"
                         f"Servicio de Habitacion: {self.tipoHabitacion}\n"
                         f"Dias de servicio de Habitacion: {self.diasEstadia}\n"
                         f"Fecha de ingreso: {self.fechaIngreso}\n"
                         f"Consumo del servicio de Habitacion: \n {detalleConsumo}\n"
                         f"Total Estadia: {totalEstadia} USD\n"
                         f"Total Consumo: {totalConsumo} CLP\n"
                         f"Total a pagar: {totalPagar}USD (Estadia) + {totalConsumo}CLP (Consumo)\n"                         
                         )
        return salidaDetallada

def checkin(turistas):
       nombre=input("Ingrese nombre del turista: ")
       nacionalidad= input("Ingrese nacionalidad del turista: ")
       pasaporte=input("Ingrese pasaporte del turista (dejar en blanco si es nacional): ")
       rut=input("Ingrese RUT del turista (dejar en blanco si es extranjero): ")
       fechaIngreso=input("Ingrese fecha de ingreso (DD-MM-AAAA): ")
       diasEstadia=int(input("Ingrese el numero de dias de estadia: "))
       tipoHabitacion=input("Ingrese el tipo de habitacion(Normal/Premium): ")

       turista=Turista(nombre,nacionalidad,pasaporte,rut,fechaIngreso,diasEstadia,tipoHabitacion)
       turistas.append(turista)
       print (f"Turista {nombre} registrado exitosamente")

def registrarConsumo(turistas):
       nombre=input("Ingrese el nombre del turista: ")
       for turista in turistas:
           if turista.nombre==nombre:
               descripcion=input("Ingrese la descripcion del consumo: ")
               cantidad=int(input("Ingrese la cantidad: "))
               precio=int(input("Ingrese el precio: "))
               fechaHora=input("Ingrese la fecha y hora del consumo (DD-MM-AAAA): ")
               turista.agregarConsumo(descripcion,cantidad,precio,fechaHora)
               print(f"Consumo registrado exitosamente para el turista {nombre}")
               return
       print (f"Turista {nombre} no encontrado.")
    
def check_out(turistas):
       nombre=input("Ingrese el nombre del turista para relizar el check-out: ")
       for turista in turistas:
           if turista.nombre==nombre:
               print(turista.checkout())
               turistas.remove(turista)
               return
       print(f"Turista {nombre} no encontrado")

def listarTuristas(turistas):
       if not turistas:
           print("No hay turistas registrados")
       else:
           for turista in turistas:
               print(f"Nombre: {turista.nombre}, Nacionalidad: {turista.nacionalidad}, Tipo de Habitacion: {turista.tipoHabitacion}, Dias de estadia: {turista.diasEstadia} ")

    
def Registros(turistas):
    with open('Hotel.txt', mode='w') as file:
        file.write("Nombre,Nacionalidad,Pasaporte,RUT,Fecha Ingreso, Dias Estadia, Tipo Habitacion,Consumo\n")
        for turista in turistas:
            consumos= "; ".join ([f"{item['descripcion']} x {item['cantidad']} - {item['precio']} CLP - {item['fechaHora']}" for item in turista.consumoHabitacion])
            file.write(f"{turista.nombre},{turista.nacionalidad},{turista.pasaporte},{turista.rut},{turista.fechaIngreso},{turista.diasEstadia},{turista.tipoHabitacion},{consumos}\n")
    print("Registros guardados existosamente en hotel.txt")

def menu():
        turistas=[]
        while True:
            print("********** Bienvenido a Gran Hotel Santiago **********")
            print("1.- Check-in")
            print("2.- Registrar Consumo")
            print("3.- Check-out")
            print("4.- Listar Turistas")
            print("5.- Guardar Registros en documento")
            print("6.- Salir")
            print("*******************************************************")
            opcion=input("Selecione una opcion: ")
            if opcion=="1":
                checkin(turistas)
            elif opcion=="2":
                registrarConsumo(turistas)
            elif opcion=="3":
                 check_out(turistas)
            elif opcion=="4":
                 listarTuristas(turistas)
            elif opcion=="5":
                 Registros(turistas)
            elif opcion=="6":
                 print("Adios!")
                 break
            else:
                 print("Opcion no valida. Vuelva a ingresar un valor.")


if __name__=="__main__":
     menu()