# Importamos Process y Pool del módulo multiprocessing
# Pool permite gestionar automáticamente un conjunto de procesos
from multiprocessing import Process, Pool

# Importamos el módulo time para medir tiempos de ejecución
import time

"""
Modifica el ejercicio anterior para que el programa principal use 
un Pool para lanzar varios procesos de forma concurrente. 
Cambia el valor del número de procesos y compara los tiempos 
que tarda en ejecutarse en los distintos casos.
"""

# Función que suma todos los números desde 1 hasta el valor recibido
def suma_desde_1(numero: int):
    # Inicializamos la variable suma
    suma = 0

    # Recorremos los números desde 1 hasta 'numero' (incluido)
    for i in range(1, numero + 1):
        # Acumulamos la suma
        suma += i

    # Mostramos el resultado por pantalla
    # Este print lo ejecuta cada proceso de forma independiente
    print(f"Suma hasta {numero}: {suma}")

# Punto de entrada del programa principal
# Obligatorio cuando se trabaja con multiprocessing
if __name__ == "__main__":

    # Lista de números sobre los que se ejecutará la función
    numbers = [2, 3, 4, 5, 6, 7, 8]

    # Guardamos el instante inicial para medir el tiempo de ejecución
    inicio = time.perf_counter()

    # Creamos un Pool de procesos
    # processes=5 indica que como máximo habrá 5 procesos ejecutándose a la vez
    # El 'with' se encarga de cerrar el Pool automáticamente al finalizar
    with Pool(processes=5) as pool:

        # pool.map aplica la función suma_desde_1 a cada elemento de 'numbers'
        # Los trabajos se reparten entre los procesos del Pool
        # Es equivalente a un map normal, pero en paralelo
        results = pool.map(suma_desde_1, numbers)

    # Guardamos el instante final tras terminar todos los procesos
    fin = time.perf_counter()

    # Mostramos el tiempo total que ha tardado el programa
    print(f"Tiempo total de ejecución: {fin - inicio:.4f} segundos")

    # Este mensaje solo aparece cuando todos los procesos han terminado
    print("Todos los procesos han terminado")
