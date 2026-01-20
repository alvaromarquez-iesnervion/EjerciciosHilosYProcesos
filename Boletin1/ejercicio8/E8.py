from multiprocessing import Pipe, Process
import time


# Función productora: lee el fichero y envía los rangos por Pipe

def leer_fichero(ruta_fichero, conn):
    with open(ruta_fichero, "r") as f:
        for linea in f:
            # Convertimos la línea en dos enteros
            numeros = tuple(map(int, linea.strip().split()))
            # Enviamos la tupla por la Pipe
            conn.send(numeros)
    
    # Señal de fin
    conn.send(None)

# Función consumidora: recibe los rangos por Pipe y realiza la suma
def suma_entre(conn):
    while True:
        item = conn.recv()  # Bloquea hasta recibir un dato

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
    # Creamos un Pipe (dos extremos: left y right)
    left, right = Pipe()

    inicio_tiempo = time.perf_counter()

    # Proceso productor: lee el fichero y envía datos
    p_lector = Process(target=leer_fichero, args=("ejercicio8/numeros.txt", left))

    # Proceso consumidor: recibe los datos y realiza la suma
    p_suma = Process(target=suma_entre, args=(right,))

    # Iniciamos los procesos
    p_lector.start()
    p_suma.start()

    # Esperamos a que ambos procesos terminen
    p_lector.join()
    p_suma.join()

    fin_tiempo = time.perf_counter()

    print(f"Tiempo total de ejecución: {fin_tiempo - inicio_tiempo:.4f} segundos")
    print("Todos los procesos han terminado")
