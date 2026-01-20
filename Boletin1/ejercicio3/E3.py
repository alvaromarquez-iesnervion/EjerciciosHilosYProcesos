
from multiprocessing import Process, Queue
import time

"""Realiza el ejercicio anterior pero esta vez va a haber otra función que lea los números de un fichero. 
En el fichero habrá un número por línea. En este caso, tienes que llevar a cabo una comunicación entre los 
dos procesos utilizando colas (Queue), de forma que la función que se encarga de leer los números los guarde en la cola, 
y la función que realiza la suma, recibirá la cola y tomará de ahí los números. La función que lee el fichero, una vez 
haya terminado de leer y de añadir elementos a la cola, debe añadir un objeto None para que el receptor sepa cuándo terminar 
de leer de la cola.
"""

# Función que lee números de un fichero y los mete en la cola
def leer_fichero(ruta_fichero, cola):
    with open(ruta_fichero, "r") as f: # "r" significa que se abre en modo lectura
        for linea in f:
            numero = int(linea.strip())
            cola.put(numero)  # Metemos el número en la cola

    # Cuando no haya más números, metemos None para avisar al consumidor
    cola.put(None)

# Función que lee números de la cola y calcula la suma
def suma_desde_1(cola):
    while True:
        numero = cola.get()  # Bloquea hasta que haya un dato

        # Si recibimos None, sabemos que ya no hay más datos
        if numero is None:
            break

        suma = 0
        for i in range(1, numero + 1):
            suma += i

        print(f"Suma hasta {numero}: {suma}")

if __name__ == "__main__":

    # Creamos la cola para comunicar procesos
    cola = Queue()

    inicio = time.perf_counter()

    # Proceso productor: lee el fichero
    p_lector = Process(target=leer_fichero, args=("ejercicio3/numeros.txt", cola))

    # Proceso consumidor: calcula las sumas
    p_suma = Process(target=suma_desde_1, args=(cola,))

    # Iniciamos los procesos
    p_lector.start()
    p_suma.start()

    # Esperamos a que terminen
    p_lector.join()
    p_suma.join()

    fin = time.perf_counter()

    print(f"Tiempo total de ejecución: {fin - inicio:.4f} segundos")
    print("Todos los procesos han terminado")
