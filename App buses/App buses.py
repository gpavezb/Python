
def menu():
    print("Bienvenido a buses interurbanos")
    print("Seleccione destino:")
    print("1.- Santiago $18.000 por tramo")
    print("2.- Arica $18.500 por tramo")
    print("3.- Temuco $20.580 por tramo")
    print("4.- Concepción 18.600 por tramo")

def calcular_precio_total (precio_base, equipaje):
    precio_total =precio_base
    if  equipaje >1:
          precio_total =(equipaje-1)*5000
    return precio_total 

def mostrar_boleto(destino,precio_total ,equipaje):
    print ("***************PASAJE INTERURBANOS***************")
    print (f"Destino {destino} con valor ${precio_total }")
    print (f"Numero de equipaje {equipaje} con un valor de $ {(equipaje-1)*5000}")
    print (f"******Total: ${precio_total +(equipaje-1)*5000}******")
    print ("**************************************************")

def main():
    ventas= {"Santiago":0,
             "Arica":0,
             "Temuco":0,
             "Concepcion":0
             }
    total_pasajes=0
    total_maletas=0

    while True:
        menu()
        opcion=input("Ingrese el numero de destino:\n ")
        
        destinos={
            "1":("Santiago", 18000),
            "2":("Arica",18500),
            "3":("Temuco", 20580),
            "4":("Concepcion",18600), 
        }
        if opcion in destinos:
            destino, precio_base=destinos[opcion]

            retorno=input("Desea pasaje de vuelta? Si o no\n")
            if retorno.lower()=='si':
                precio_base*=2

            equipaje=int(input("Cuantas maletas lleva?\n"))
            if equipaje <0:
                    equipaje=0

            precio_total = calcular_precio_total(precio_base, equipaje)
            mostrar_boleto(destino,precio_total ,equipaje)

            ventas[destino]+=1
            total_pasajes+=precio_total 
            total_maletas+=equipaje*5000

            otra_vez=input("Necesitas otro pasaje? responda si o no\n")
            if otra_vez.lower()!='si':
                 break
    
    print("***************PASAJE INTERURBANOS***************")
    print("Resumen de ventas")
    for destino, cantidad in ventas.items():
         if cantidad >0:
              print(f"{destino}:{cantidad}")
    print (f"TOTAL EN PASAJES: ${total_pasajes}")
    print (f"TOTAL EN MALETAS: ${total_maletas}")
    print ("**************************************************")


main()