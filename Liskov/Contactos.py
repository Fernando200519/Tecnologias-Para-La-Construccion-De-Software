contactos = {}

def agregar_contacto(nombre, telefono):
    contactos[nombre] = telefono
    print(f"Contacto {nombre} agregado")

def mostrar_contactos():
    if not contactos:
        print("No hay contactos disponibles")
    else:
        for nombre, telefono in contactos.items():
            print(f"{nombre}: {telefono}")

def busar_contacto(nombre):
    if nombre in contactos:
        print(f"{nombre} -> {contactos[nombre]}")
    else:
        print(f"Contacto {nombre} no encontrado")

while True:
    print("\n1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        agregar_contacto(nombre, telefono)
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        nombre = input("Nombre del contacto a buscar: ")
        busar_contacto(nombre)
    elif opcion == "4":
        break
    else:
        print("Opción no valida")
