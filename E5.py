"""Crea una función en Python que sea capaz de sumar todos los números comprendidos entre dos valores, incluyendo ambos valores y mostrar el 
resultado por pantalla. Estos valores se les pasará como argumentos. Hay que tener presente que el primer argumento puede ser mayor que el segundo, 
y habrá que tenerlo presente para realizar la suma.
Desde el programa principal crea varios procesos que ejecuten la función anterior. El programa principal debe imprimir un mensaje indicando que 
todos los procesos han terminado después de que los procesos hayan impreso el resultado.
"""

from multiprocessing import Process

# Función que suma todos los números entre dos valores
def suma_entre(val1: int, val2: int):
    inicio = min(val1, val2)
    fin = max(val1, val2)
    suma = sum(range(inicio, fin + 1))  # Usamos sum() para acortar
    print(f"Suma desde {val1} hasta {val2}: {suma}")

# Programa principal
if __name__ == "__main__":
    # Lista de rangos que queremos sumar (tuplas: inicio, fin)
    rangos = [
        (1, 5),
        (3, 10),
        (8, 2),
        (7, 7),
        (0, 4)
    ]

    # Creamos una lista para guardar los procesos
    procesos = []

    # Creamos e iniciamos los procesos en un bucle
    for inicio, fin in rangos:
        p = Process(target=suma_entre, args=(inicio, fin))
        procesos.append(p)
        p.start()

    # Esperamos a que todos los procesos terminen
    for p in procesos:
        p.join()

    print("Todos los procesos han terminado")
