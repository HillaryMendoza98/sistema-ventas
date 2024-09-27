productos = {}

# Lista para almacenar las ventas realizadas
ventas = []

# Función para agregar productos al sistema
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    productos[nombre] = precio
    print(f"Producto {nombre} agregado con éxito.\n")

# Función para mostrar los productos disponibles
def mostrar_productos():
    if not productos:
        print("No hay productos disponibles.\n")
        return
    print("Productos disponibles:")
    for nombre, precio in productos.items():
        print(f"{nombre}: ${precio:.2f}")
    print()

# Función para registrar una venta
def registrar_venta():
    mostrar_productos()
    producto = input("Ingrese el nombre del producto vendido: ")
    
    if producto in productos:
        cantidad = int(input(f"Ingrese la cantidad de {producto} vendidos: "))
        total_venta = productos[producto] * cantidad
        ventas.append(total_venta)
        print(f"Venta registrada: {cantidad} {producto}(s) por ${total_venta:.2f}\n")
    else:
        print("Producto no encontrado.\n")

# Función para mostrar el total de ventas realizadas
def mostrar_total_ventas():
    if not ventas:
        print("No se han registrado ventas.\n")
        return
    total_ingresos = sum(ventas)
    print(f"Total de ingresos por ventas: ${total_ingresos:.2f}\n")

# Bucle principal del programa
while True:
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Registrar venta")
    print("4. Mostrar total de ventas")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        registrar_venta()
    elif opcion == "4":
        mostrar_total_ventas()
    elif opcion == "5":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.\n")

