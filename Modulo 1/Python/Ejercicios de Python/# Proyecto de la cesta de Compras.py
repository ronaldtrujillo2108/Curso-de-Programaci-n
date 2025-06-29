# Cesta de la compra interactiva

# Diccionario de productos disponibles con precios
productos_disponibles = {
    "manzana": 0.5,
    "pan": 1.5,
    "leche": 2.0,
    "queso": 3.0,
    "huevo": 0.2
}

# Lista que representa la cesta de la compra del usuario
cesta = []

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Agregar un nuevo elemento")
    print("2. Mostrar la cesta de la compra")
    print("3. Eliminar un elemento")
    print("4. Calcular el total")
    print("5. Renunciar (Salir)")

# Función para agregar productos
def agregar_elemento():
    print("\nProductos disponibles:")
    for producto, precio in productos_disponibles.items():
        print(f"- {producto} (${precio:.2f})")
    
    eleccion = input("¿Qué producto quieres agregar?: ").lower()
    if eleccion in productos_disponibles:
        cesta.append(eleccion)
        print(f"{eleccion} se ha agregado a tu cesta.")
    else:
        print("Ese producto no está disponible.")

# Función para mostrar la cesta
def mostrar_cesta():
    if not cesta:
        print("\nTu cesta está vacía.")
    else:
        print("\nContenido de la cesta:")
        for i, item in enumerate(cesta, start=1):
            print(f"{i}. {item} - ${productos_disponibles[item]:.2f}")

# Función para eliminar un producto
def eliminar_elemento():
    mostrar_cesta()
    if cesta:
        try:
            index = int(input("¿Qué número de elemento quieres eliminar?: "))
            if 1 <= index <= len(cesta):
                eliminado = cesta.pop(index - 1)
                print(f"{eliminado} ha sido eliminado de tu cesta.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, introduce un número válido.")

# Función para calcular el total
def calcular_total():
    total = sum(productos_disponibles[item] for item in cesta)
    print(f"\nTotal a pagar: ${total:.2f}")

# Bucle principal
def iniciar():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            agregar_elemento()
        elif opcion == "2":
            mostrar_cesta()
        elif opcion == "3":
            eliminar_elemento()
        elif opcion == "4":
            calcular_total()
        elif opcion == "5":
            print("Gracias por usar el sistema de compra. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Iniciar el programa
iniciar()
