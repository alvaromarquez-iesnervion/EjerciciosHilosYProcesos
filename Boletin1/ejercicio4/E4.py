# Importamos Pipe y Process de multiprocessing
# Pipe permite la comunicación directa entre dos procesos
# Process nos permite crear y ejecutar procesos independientes
from multiprocessing import Pipe, Process
import time  # Para medir tiempos de ejecución

"""
Enunciado: 
- Leer números de un fichero usando un proceso (productor) 
  y enviarlos a otro proceso (consumidor) mediante Pipe.
- El consumidor suma los números y termina cuando recibe None.
"""

# Función productora: lee el fichero y envía los números
def leer_fichero(ruta_fichero, conn):
    # Abrimos el fichero en modo lectura
    with open(ruta_fichero, "r") as f: 
        # Recorremos cada línea del fichero
        for linea in f:
            # Convertimos la línea a entero (elimina saltos de línea)
            numero = int(linea.strip())
            # Enviamos el número al proceso consumidor a través del Pipe
            conn.send(numero)  

    # Una vez leídos todos los números, enviamos None
    # Esto indica al proceso consumidor que ya no hay más datos
    conn.send(None)

# Función consumidora: recibe números y calcula la suma
def suma_desde_1(conn):
    while True:
        # Recibimos un número del Pipe
        # Esta operación bloquea hasta que haya un dato disponible
        numero = conn.recv()  

        # Si recibimos None, significa que el productor terminó
        if numero is None:
            break  # Salimos del bucle y terminamos el proceso

        # Calculamos la suma de 1 hasta el número recibido
        suma = 0
        for i in range(1, numero + 1):
            suma += i

        # Mostramos el resultado
        print(f"Suma hasta {numero}: {suma}")

# Programa principal
if __name__ == "__main__":
    # Creamos un Pipe que devuelve dos extremos conectados
    # left y right son los extremos del Pipe
    left, right = Pipe()

    # Medimos el tiempo de ejecución total
    inicio = time.perf_counter()

    # Creamos el proceso lector (productor)
    # Le pasamos la ruta del fichero y el extremo 'left' del Pipe
    p_lector = Process(target=leer_fichero, args=("ejercicio3/numeros.txt", left))

    # Creamos el proceso que suma los números (consumidor)
    # Le pasamos el extremo 'right' del Pipe
    p_suma = Process(target=suma_desde_1, args=(right,))

    # Iniciamos ambos procesos
    p_lector.start()
    p_suma.start()

    # Esperamos a que ambos procesos terminen antes de continuar
    p_lector.join()
    p_suma.join()

    # Medimos el tiempo final y calculamos duración
    fin = time.perf_counter()

    # Mostramos el tiempo total que ha tardado la ejecución
    print(f"Tiempo total de ejecución: {fin - inicio:.4f} segundos")
    print("Todos los procesos han terminado")
