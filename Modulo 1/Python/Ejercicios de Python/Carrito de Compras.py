# Carrito de Compras Interactivo

# Listas para almacenar los productos y sus precios
names = []
prices = []

# Función para mostrar el menú principal
def show_menu():
    print("\n🛒 BIENVENIDO A TU CARRITO DE COMPRAS 🛒")
    print("Por favor, elige una de las siguientes opciones:")
    print("1. Agregar artículo")
    print("2. Ver carrito")
    print("3. Eliminar artículo")
    print("4. Calcular total")
    print("5. Salir")

# Función para agregar un nuevo artículo
def add_item():
    name = input("¿Qué artículo deseas agregar?: ").strip()
    try:
        price = float(input(f"¿Cuál es el precio de {name}?: "))
        if price < 0:
            print("El precio no puede ser negativo.")
            return
        names.append(name)
        prices.append(price)
        print(f"✅ '{name}' ha sido agregado al carrito.")
    except ValueError:
        print("❌ Precio inválido. Por favor, introduce un número válido.")

# Función para mostrar el contenido del carrito
def view_cart():
    if not names:
        print("🛒 El carrito está vacío.")
    else:
        print("\n🧾 Contenido del carrito:")
        for i, (name, price) in enumerate(zip(names, prices), start=1):
            print(f"{i}. {name} - ${price:.2f}")

# Función para eliminar un artículo
def remove_item():
    if not names:
        print("🛒 El carrito está vacío. No hay nada que eliminar.")
        return

    view_cart()
    try:
        number = int(input("¿Qué número de artículo deseas eliminar?: "))
        index = number - 1
        if 0 <= index < len(names):
            removed = names.pop(index)
            prices.pop(index)
            print(f"❌ '{removed}' fue eliminado del carrito.")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida. Por favor, introduce un número.")

# Función para calcular el total de la compra
def compute_total():
    if not prices:
        print("🛒 El carrito está vacío.")
        return
    total = sum(prices)
    print(f"💰 El total de la compra es: ${total:.2f}")

# Función principal para ejecutar el menú
def main():
    while True:
        show_menu()
        choice = input("Ingresa tu opción (1-5): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            compute_total()
        elif choice == "5":
            print("👋 Gracias por usar el carrito de compras. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

# Iniciar el programa
if __name__ == "__main__":
    main()
