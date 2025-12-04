import subprocess

import time

def run_example(path):
    start = time.time()
    result = subprocess.run(['python', path], capture_output=True, text=True)
    end = time.time()
    return result.stdout, end - start

print("\nIniciando comparacion\n")

print("Ejecutando ejemplo incorrecto...")

output1, time1 = run_example('1_ejemplo_incorrecto/main.py')

print("\nEjecutando ejemplo correcto...")

output2, time2 = run_example('2_ejemplo_correcto/main.py')

print("\nResultados de la comparación: ")

print("-" * 40)

print(f"Tiempo ejemplo incorrecto: {time1:.2f} segundos")

print(f"Tiempo ejemplo correcto: {time2:.2f} segundos")

print("-" * 40)

print(f"Mejora de eficiencia: {((time1 - time2) / time1 * 100):.1f} %")

print("\nComparacion finalizada")