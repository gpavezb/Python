
def menu_principal():
    print ("--- Bienvenido a dulce tentacion ---")
    print ("1.- Registrar venta")
    print ("2.- Salir")
    return input("Ingrese opcion: \n")


def menu_comidas():
    print ("---Bienvenido a Dulce tentacion.Selecciona que quieres comer---")
    print ("1.- Dulce")
    print ("2.- Salado")
    print ("3.- Helados")
    print ("4.- Colaciones")
    print ("5.- Salir")
    return input("Ingrese opcion: \n")

def datos_cliente():
    nombre=input("ingrese su nombre:\n ")
    direccion= input("Ingrese su direccion:\n ")
    forma_pago=input("Ingrese su forma de pago:\n 1)Tarjeta de credito\n 2)Tarjeta de debito\n 3)Transferencia bancaria\n")
    return nombre,direccion,forma_pago

def aplicar_descuento_envio(forma_pago, ventas_totales):
    descuento=0
    envio_gratis=False
    if forma_pago=='2':
        descuento=ventas_totales*0.02
    elif forma_pago=='3':
        envio_gratis=True
    return descuento,envio_gratis

def dulces():
    Lista_dulce=[
        ("chocolate", 800),
        ("alfajor", 700),
        ("galleta", 600),
        ("dulce", 500),
        ("queque", 400)
    ]
    cantidad_por_caterogia={item[0]:0 for item in Lista_dulce}

    print("#################################")
    print("---Esta es la lista de cosas dulces---\n")
    for item, precio in Lista_dulce:
        print(f"{item}: ${precio}")
    seleccion= int(input("Seleccione el numero de dulce que desea: "))
    cantidadd= int(input("Ingrese la cantidad que desea comprar: "))

    if seleccion <1 or seleccion >len(Lista_dulce):
        print ("Seleccion invalida")
        
    dulce_seleccionado=Lista_dulce[seleccion-1]
    totald= dulce_seleccionado[1]*cantidadd

    categoria = dulce_seleccionado[0]
    cantidad_por_caterogia[categoria]+=cantidadd

    descuento_aplicado=False
    if cantidad_por_caterogia[categoria]>=10:
        descuentod=totald*0.10
        totald-=descuentod
        print("Tienes un 10% de descuento debido a que tus compras de una categoria fue de al menos 10 productos")
        descuento_aplicado=True
    elif sum(cantidad_por_caterogia.values())>5:
        descuentod=totald*0.02
        totald -=descuentod
        print("Se aplica 2% de desuento por la compra de 10 productos")
        descuento_aplicado=True
    print ("Detalle de compra: ")
    print(f"-Producto: {dulce_seleccionado}")
    print(f"-Cantidad: {cantidadd}")
    print(f"-Subtotal:{totald}")
    if descuento_aplicado:
        print(f"Descuento aplicado: ${descuentod}")
    return totald


def salado():
    Lista_salada=[
        ("Papas fritas", 2000),
        ("Ensalada", 2000),
        ("Camarones salteados", 8000),
        ("Champiñones al pil pil", 3000),
        ("Provoleta", 4000)
    ]
    cantidad_por_caterogia={item[0]:0 for item in Lista_salada}

    print("#################################")
    print("---Esta es la lista de cosas saladas---\n")
    for item, precio in Lista_salada:
        print(f"{item}: ${precio}")
    seleccion= int(input("Seleccione el numero de salado que desea: "))
    cantidad= int(input("Ingrese la cantidad que desea comprar: "))

    if seleccion <1 or seleccion >len(Lista_salada):
        print ("Seleccion invalida")
        
    salado_seleccionado=Lista_salada[seleccion-1]
    total= salado_seleccionado[1]*cantidad

    categoria = salado_seleccionado[0]
    cantidad_por_caterogia[categoria]+=cantidad

    descuento_aplicado=False
    if cantidad_por_caterogia[categoria]>=10:
        descuento=total*0.10
        total-=descuento
        print("Tienes un 10% de descuento debido a que tus compras de una categoria fue de al menos 10 productos")
        descuento_aplicado=True
    elif sum(cantidad_por_caterogia.values())>5:
        descuento=total*0.02
        total -=descuento
        print("Se aplica 2% de desuento por la compra de 10 productos")
        descuento_aplicado=True

    print ("Detalle de compra: ")
    print(f"-Producto: {salado_seleccionado}")
    print(f"-Cantidad: {cantidad}")
    print(f"-Subtotal:{total}")
    if descuento_aplicado:
        print(f"Descuento aplicado: ${descuento}")
    return total

def helados():
    Lista_helados=[
        ("simple", 1500),
        ("doble", 2000),
        ("helado con crepa", 6000),
        ("banana split", 5000),
        ("helado con brownie", 4000)
    ]
    cantidad_por_caterogia={item[0]:0 for item in Lista_helados}

    print("#################################")
    print("---Esta es la lista helados---\n")
    for item, precio in Lista_helados:
        print(f"{item}: ${precio}")

    seleccion= int(input("Seleccione el numero de helado que desea: "))
    cantidad= int(input("Ingrese la cantidad que desea comprar: "))

    if seleccion <1 or seleccion >len(Lista_helados):
        print ("Seleccion invalida")
        
    helado_seleccionado=Lista_helados[seleccion-1]
    total= helado_seleccionado[1]*cantidad

    categoria = helado_seleccionado[0]
    cantidad_por_caterogia[categoria]+=cantidad

    descuento_aplicado=False
    if cantidad_por_caterogia[categoria]>=10:
        descuento=total*0.10
        total-=descuento
        print("Tienes un 10% de descuento debido a que tus compras de una categoria fue de al menos 10 productos")
        descuento_aplicado=True
    elif sum(cantidad_por_caterogia.values())>5:
        descuento=total*0.02
        total -=descuento
        print("Se aplica 2% de desuento por la compra de 10 productos")
        descuento_aplicado=True

    print ("Detalle de compra: ")
    print(f"-Producto: {helado_seleccionado}")
    print(f"-Cantidad: {cantidad}")
    print(f"-Subtotal:{total}")
    if descuento_aplicado:
        print(f"Descuento aplicado: ${descuento}")
    return total

def colaciones():
    Lista_colaciones=[
        ("Colacion simple", 8000),
        ("Colacion + ensalada", 9000),
        ("Colacion + bebida", 8500)
    ]
    cantidad_por_caterogia={item[0]:0 for item in Lista_colaciones}

    print("#################################")
    print("---Esta es la lista colaciones---\n")
    for item, precio in Lista_colaciones:
        print(f"{item}: ${precio}")
    
    seleccion= int(input("Seleccione el numero de colacion que desea: "))
    cantidad= int(input("Ingrese la cantidad que desea comprar: "))

    if seleccion <1 or seleccion >len(Lista_colaciones):
        print ("Seleccion invalida")
        
    colacion_seleccionado=Lista_colaciones[seleccion-1]
    total= colacion_seleccionado[1]*cantidad

    categoria = colacion_seleccionado[0]
    cantidad_por_caterogia[categoria]+=cantidad

    descuento_aplicado=False
    if cantidad_por_caterogia[categoria]>=10:
        descuento=total*0.10
        total-=descuento
        print("Tienes un 10% de descuento debido a que tus compras de una categoria fue de al menos 10 productos")
        descuento_aplicado=True
    elif sum(cantidad_por_caterogia.values())>5:
        descuento=total*0.02
        total -=descuento
        print("Se aplica 2% de desuento por la compra de 10 productos")
        descuento_aplicado=True
    print ("Detalle de compra: ")
    print(f"-Producto: {colacion_seleccionado}")
    print(f"-Cantidad: {cantidad}")
    print(f"-Subtotal:{total}")
    if descuento_aplicado:
        print(f"Descuento aplicado: ${descuento}")
    return total



def main():
    ventas_totales =0
    while True:
        opcion= menu_principal()
        if opcion=='1':
            nombre,direccion,forma_pago=datos_cliente()
            while True:
                otromenu=menu_comidas()
                if otromenu=='1':
                    ventas_totales+=dulces()   
                elif otromenu=='2':
                    ventas_totales+=salado()
                elif otromenu=='3':
                    ventas_totales+=helados()
                elif otromenu=='4':
                    ventas_totales+=colaciones()
                elif otromenu=='5':
                    break
                else:
                    print("Opcion no valida")
            descuento,envio_gratis=aplicar_descuento_envio(forma_pago,ventas_totales)
            ventas_totales-=descuento
            if envio_gratis:
                print("Por tu medio de pago, tienes envio gratis a tu domicilio")
            print("******************Factura******************")    
            print(f"Detalle de venta:\n-Nombre del cliente: {nombre}\n-Direccion: {direccion}")
            print(f"-Descuento aplicado por medio de pago: {descuento}\n-Total venta: ${ventas_totales}")
            break
        elif opcion=='2':
                print("Adios!")
                break
        else:
            print("opcion no valida")
main()