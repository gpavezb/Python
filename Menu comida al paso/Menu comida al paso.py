

def menu_principal():
    print ("--- Bienvenido a Comida al paso ---")
    print ("1.- Registrar venta")
    print ("2.- Consultar venta")
    print ("3.- Salir")
    return input("Ingrese opcion: \n")


def menu_comidas():
    print ("---Selecciona que quieres comer---")
    print ("11.- Hamburguesa")
    print ("12.- Completo")
    print ("13.- Papas fritas")
    print ("14.- Salir")
    return input("Ingrese opcion: \n")


def hambuguesa():
    pan=1000
    carne=1500
    precio_base=pan+carne
    ingredientes={
        'palta': 800,
        'tomate': 700,
        'cebolla' :600,
        'mayo': 500,
        'mostaza': 400
    }
    totalVentaH=precio_base
    print ("Has elegido la hamburguesa, agrega tus aderezos")
    print (f"El valor base es {precio_base}, ya que corresponde al precio del pan ({pan}) y la carne ({carne})")
    for ingrediente, precio in ingredientes.items():
        aderezo=input(f"Agregas {ingrediente} por {precio}? Responda con un si o un no\n").strip().lower()
        if aderezo=='si' or 'SI':
            totalVentaH +=precio
    print(f"El total de la venta es de: {totalVentaH} ")
    return totalVentaH

def completo():
    pancito=800
    salchicha=1200
    preciob=pancito+salchicha
    ingredientes={
        'palta': 700,
        'tomate': 600,
        'chucrut': 500,
        'mayo': 500,
        'mostaza': 400
    }
    totalVentaC=preciob
    print("Has elegido completo, agrega tus aderezos")
    print (f"El valor base es {preciob}, ya que corresponde al precio del pan ({pancito}) y la salchicha ({salchicha})")
    for ingrediente,precio in ingredientes.items():
        aderezo=input(f"Agregas {ingrediente} por {precio}? Responda con un si o un no\n").strip().lower()
        if aderezo=='si' or aderezo=='SI':
            totalVentaC+=precio
    print(f"El total de la venta es de: {totalVentaC}")
    return totalVentaC

def papitas():
    tiposdepapas={
        'chica': 900,
        'mediana': 2500,
        'familiar': 5000
    }
    totalventaF=0
    print("PAPITAS FRITAS")
    for tipo, precio in tiposdepapas.items():
        medida=input(f"Desea una papa {tipo} por {precio}? Responda con un si o un no\n").strip().lower()
        if medida=='si' or medida=='SI':
            totalventaF+=precio
    print(f"El total de la venta es de: {totalventaF}")
    return totalventaF

def main():
    ventas_totales =0
    while True:
        opcion= menu_principal()
        if opcion=='1':
            while True:
                otromenu=menu_comidas()
                if otromenu=='11':
                    ventas_totales+=hambuguesa()
                elif otromenu=='12':
                    ventas_totales+=completo()
                elif otromenu=='13':
                    ventas_totales+=papitas()
                elif otromenu=='14':
                    break
                else:
                    print("Opcion no valida")
        elif opcion=='2':
                print(f"El total de ventas realizadas es de : {ventas_totales}")
        elif opcion=='3':
                print("Adios!")
                break
        else:
            print("opcion no valida")
main()



