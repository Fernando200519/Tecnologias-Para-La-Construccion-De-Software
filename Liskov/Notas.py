notas = {}

def agregar_nota(estudiante, nota):
    if estudiante not in notas:
        notas[estudiante] = []
    notas[estudiante].append(nota)

def mostrar_notas():
    for estudiante, lista_notas in notas.items():
        promedio = sum(lista_notas) / len(lista_notas)
        print(f"{estudiante} Notas: {lista_notas}, Promedio: {promedio:.2f}")

def guardar_en_archivo():
    with open("notas txt", "w") as f:
        for estudiante, lista_notas in notas.items():
            f.write(f"{estudiante}: {lista_notas}\n")

        