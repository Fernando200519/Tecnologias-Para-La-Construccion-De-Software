def suma(a, b):
    return a + b

def resta(a, b):
    return a -b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "\nError: No se puede dividir entre 0"

print("Calculadora en Python\n")

while True:
    print("Opciones: +  -  *  /  (o 'salir' para terminar)")

    operacion = input("Elige la operación: ")

    if operacion == 'salir':
        break

    try:
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
    except ValueError:
        print("\nError: Debes introducir un número valido")

    if operacion == "+":
        print("Resultado: ", suma(num1, num2))
    elif operacion == "-":
        print("Resultado: ", resta(num1, num2))
    elif operacion == "*":
        print("Resultado: ", multiplicacion(num1, num2))
    elif operacion == "/":
        print("Resultado: ", division(num1, num2))
    else:
        print("Opción invalida")