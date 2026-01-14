from multiprocessing import Process, Queue
import time

# Función productora: lee el fichero y mete los rangos en la cola
def leer_fichero(ruta_fichero, cola):
    with open(ruta_fichero, "r") as f:
        for linea in f:
            # Separamos los dos números por espacio y convertimos a int
            numeros = tuple(map(int, linea.strip().split()))
            # Metemos la tupla en la cola
            cola.put(numeros)

    # Señal de fin para el consumidor
    cola.put(None)

# Función consumidora: saca los rangos de la cola y realiza la suma
def suma_entre(cola):
    while True:
        item = cola.get()  # Bloquea hasta que haya un dato

        # Si recibimos None, terminamos
        if item is None:
            break

        val1, val2 = item
        inicio = min(val1, val2)
        fin = max(val1, val2)
        suma = sum(range(inicio, fin + 1))

        print(f"Suma desde {val1} hasta {val2}: {suma}")

# Programa principal
if __name__ == "__main__":
    # Creamos la cola para comunicar los procesos
    cola = Queue()

    # Medimos el tiempo
    inicio_tiempo = time.perf_counter()

    # Creamos los procesos
    p_lector = Process(target=leer_fichero, args=("ejercicio7/numeros.txt", cola))
    p_suma = Process(target=suma_entre, args=(cola,))

    # Iniciamos los procesos
    p_lector.start()
    p_suma.start()

    # Esperamos a que terminen
    p_lector.join()
    p_suma.join()

    fin_tiempo = time.perf_counter()

    print(f"Tiempo total de ejecución: {fin_tiempo - inicio_tiempo:.4f} segundos")
    print("Todos los procesos han terminado")
