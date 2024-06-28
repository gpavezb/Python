###### Gonzalo Pavez Barrales RUT: 18.778.164-7



from datetime import datetime

class Repartidor:
    def __init__ (self, rut, nombre, fechaNacimiento, direccion, correo, telefono, estadoCivil, comuna, region):
        self.rut=rut
        self.nombre=nombre
        self.fechaNacimiento=fechaNacimiento
        self.direccion=direccion
        self.correo=correo
        self.telefono=telefono
        self.estadoCivil=estadoCivil
        self.comuna=comuna
        self.region=region

class Envio:
    codigoCounter=1

    def __init__(self,remitenteRUT,remitenteNombre,remitenteDireccion,remitentePais,remitenteComuna,receptorRUT,receptorNombre,receptorDireccion,receptorPais,receptorComuna,fechaEnvio,pesoPaquete,estadoEnvio,repartidor,encargadoDespacho=None, fechaEntrega=None):
        self.codigo=Envio.codigoCounter
        Envio.codigoCounter+=1
        self.remitenteRUT=remitenteRUT
        self.remitenteNombre=remitenteNombre
        self.remitenteDireccion=remitenteDireccion
        self.remitentePais=remitentePais
        self.remitenteComuna=remitenteComuna
        self.receptorRUT=receptorRUT
        self.receptorNombre=receptorNombre
        self.receptorDireccion=receptorDireccion
        self.receptorPais=receptorPais
        self.receptorComuna=receptorComuna
        ##self.receptor=receptor
        self.fechaEnvio=fechaEnvio
        self.pesoPaquete=pesoPaquete
        self.costoEnvio=self.calcularCosto(pesoPaquete)
        self.estadoEnvio=estadoEnvio
        self.repartidor=repartidor
        self.encargadoDespacho=encargadoDespacho
        self.fechaEntrega=fechaEntrega

    def calcularCosto(self, peso):
        base=1800
        if peso <=1:
            return base
        else:
            pesoExtra=peso-1
            costoAdicional=1000*pesoExtra
            descuento=0.05*(pesoExtra//10)
            costoTotal= base+costoAdicional-(costoAdicional*descuento)
            return costoTotal
        

    def descripcion(self):
        print (f"*****************************************************")
        print (f"Codigo: {self.codigo}")
        print (f"Remitente: {self.remitenteRUT},  {self.remitenteNombre},  {self.remitenteDireccion},  {self.remitentePais},  {self.remitenteComuna}")
        print (f"Receptor: {self.receptorRUT},  {self.receptorNombre}, {self.receptorDireccion},  {self.receptorPais},  {self.receptorComuna}")
        print (f"Fecha de envío: {self.fechaEnvio}")
        print (f"Fecha de Entrega: {self.fechaEntrega}")
        print (f"Estado del Envio: {self.estadoEnvio}")
        print (f"Costo de del Envío: {self.costoEnvio}")
        print (f"Repartidor: {self.repartidor}")
        print (f"Encargado del despacho: {self.encargadoDespacho}")
        print (f"*****************************************************")

def ingresarRepartidor(repartidores):
    rut=input("Ingrese RUT del repartidor: ")
    nombre=input("Ingrese nombre completo del repartidor: ")
    fechaNacimiento=input("Ingrese fecha de nacimiento del repartidor DD-MM-AAAA: ")
    direccion=input("Ingrese direccion del repartidor: ")
    correo=input("Ingrese correo electronico del repartidor: ")
    telefono=input("Ingrese telefono del repartidor: ")
    estadoCivil=input("Ingrese estado civil del repartidor: ")
    comuna= input("Ingrese comuna del repartidor: ")
    region= input("Ingrese region del repartidor: ")
    repartidor=Repartidor(rut,nombre,fechaNacimiento,direccion,correo, telefono, estadoCivil, comuna, region)
    repartidores.append(repartidor)
    print(f"Repartidor {nombre} ingresado exitosamente")

def registro_envio(envios,repartidores):
    remitenteRut=input("Ingrese RUT del remitente: ")
    remitenteNombre=input("Ingrese nombre del remitente: ")
    remitenteDireccion=input("Ingrese direccion del remitente: ")
    remitentePais=input("Ingrese país del remitente: ")
    remitenteComuna=input("Ingrese comuna del remitente: ")
    receptorRut=input("Ingrese RUT del receptor: ")
    receptorNombre=input("Ingrese nombre del receptor: ")
    receptorDireccion=input("Ingrese direccion del receptor: ")
    receptorPais=input("Ingrese país del receptor: ")
    receptorComuna=input("Ingrese comuna del receptor: ")
    fechaEnvio=input("Ingrese fecha de envio DD-MM-AAAA: ")
    pesoPaquete=float(input("Ingreses peso del paquete en KG: "))
    estadoEnvio=input("Ingrese el estado del envío (en transito, no entregadom entregado sin registro): ")
    print("Selecionna el repartidor: ")
    for idx, repartidor in enumerate(repartidores):
        print (f"{idx + 1}.{repartidor.nombre}")
    repartidor_idx=int(input("ingrese el numero del repartidor: "))-1
    repartidor=repartidores[repartidor_idx].nombre
    envio=Envio(remitenteRut,remitenteNombre, remitenteDireccion, remitentePais,remitenteComuna,receptorRut,receptorNombre,receptorDireccion,receptorPais,receptorComuna,fechaEnvio,pesoPaquete,estadoEnvio,repartidor)
    envios.append(envio)
    print("Envío ingresado exitosamente")

def modificar_envio(envios):
    codigo=int(input("Ingrese el codigo dle envio a modificar: "))
    for envio in envios:
        if envio.codigo==codigo:
            nuevoEstado=input("Ingrese el nuevo estado del envío (en Transito, no entregado, entregado, sin registro): ")
            if nuevoEstado=="entregado":
                fechaEntrega=input("Ingrese la fecha de entrega DD-MM-AAAA: ")
                encargadoDespacho=input("Ingrese el nombre del encargado de despacho: ")
                envio.fechaEntrega=fechaEntrega
                envio.encargadoDespacho=encargadoDespacho
            envio.estadoEnvio=nuevoEstado
            print("Estado del envío modificado exitosamente. ")
            return
        print("Codigo de envio no encontrado.")

def listar_envios(envios):
    if not envios:
        print("No hay envios registrados")
    else:
        for envio in envios:
            envio.descripcion()

def menu():
    repartidores=[]
    envios=[]
    while True:
        print("**********Bienvenido a la aplicacion de Envío Instantaneos **********")
        print("1.- Ingrese un repartidor")
        print("2.- Ingrese un envio")
        print("3.- Modifique un envio")
        print("4.- Listar todos los envios")
        print("5.-Salir")
        print("*********************************************************************")
        opcion=input("Selecionne una opcion: ")
        if opcion=="1":
            ingresarRepartidor(repartidores)
        elif opcion=="2":
            registro_envio(envios,repartidores)
        elif opcion=="3":
            modificar_envio(envios)
        elif opcion == "4":
            listar_envios(envios)
        elif opcion == "5":
            print("Saliendo de la aplicacion")
            break
        else:
            print("Opcion no valida. Vuelva a ingresar un valor")

if __name__=="__main__":
    menu()