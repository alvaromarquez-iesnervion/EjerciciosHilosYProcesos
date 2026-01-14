"""En este caso, vuelve a realizar la comunicación entre procesos pero usando tuberías (Pipe), de forma que la función que se encarga de 
leer los números del fichero se los envíe (send) al proceso que se encarga de la suma. El proceso que suma los números tiene que recibir (recv) 
un número y realizar la suma. Una vez que el proceso que lee el fichero termine de leer números en el fichero, debe enviar un None. El que recibe 
números dejará de realizar sumas cuando reciba un None.
"""

from multiprocessing import Pipe, Process
import time


def leer_fichero(ruta_fichero, conn):
    with open(ruta_fichero, "r") as f: 
        for linea in f:
            numero = int(linea.strip())
            conn.send(numero)  

    
    conn.send(None)

def suma_desde_1(conn):
    while True:
        numero = conn.recv()  # Bloquea hasta que haya un dato

        # Si recibimos None, sabemos que ya no hay más datos
        if numero is None:
            break

        suma = 0
        for i in range(1, numero + 1):
            suma += i

        print(f"Suma hasta {numero}: {suma}")

if __name__ == "__main__":
    left, right=Pipe()
    
    inicio = time.perf_counter()
    p_lector = Process(target=leer_fichero, args=("ejercicio3/numeros.txt", left))
    p_suma = Process(target=suma_desde_1, args=(right,))

    p_lector.start()
    p_suma.start()

    p_lector.join()
    p_suma.join()

    fin = time.perf_counter()

    print(f"Tiempo total de ejecución: {fin - inicio:.4f} segundos")
    print("Todos los procesos han terminado")