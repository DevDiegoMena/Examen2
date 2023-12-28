def agregar_compra(compras):
    monto = float(input("Ingrese el monto de la compra: "))
    compras.append(monto)
    print(f"Compra por ${monto} agregada correctamente.")

def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Lista de compras:")
        for i, compra in enumerate(compras, start=1):
            print(f"Compra {i}: ${compra}")

def mostrar_total(compras):
    total = sum(compras)
    print(f"Total gastado: ${total:.2f}")

def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agregar_compra(compras)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(compras)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
