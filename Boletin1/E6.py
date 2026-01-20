from multiprocessing import Pool
import time

# -------------------------------
# Función que suma todos los números entre dos valores
# -------------------------------
def suma_entre(val1: int, val2: int):
    inicio = min(val1, val2)
    fin = max(val1, val2)
    suma = sum(range(inicio, fin + 1))  # Suma rápida con sum()
    print(f"Suma desde {val1} hasta {val2}: {suma}")

# -------------------------------
# Programa principal
# -------------------------------
if __name__ == "__main__":
    # Lista de rangos que queremos sumar (tuplas: inicio, fin)
    rangos = [
        (1, 5),
        (3, 10),
        (8, 2),
        (7, 7),
        (0, 4)
    ]

    inicio_tiempo = time.perf_counter()

    # Creamos un Pool con 3 procesos (puedes ajustar el número)
    with Pool(processes=3) as pool:
        # starmap permite pasar múltiples argumentos a la función
        pool.starmap(suma_entre, rangos)

    fin_tiempo = time.perf_counter()

    print(f"Tiempo total de ejecución: {fin_tiempo - inicio_tiempo:.4f} segundos")
    print("Todos los procesos han terminado")
