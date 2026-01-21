"""
Para realizar este ejercicio es necesario que definas 2 procesos distintos y un Main:

Proceso 1: Recibe como parámetros una ruta de fichero y un año. El proceso leerá el fichero el cual almacena en cada línea 
la información de una película: nombre y año de estreno separados por punto y coma (;)

Debe enviar al siguiente proceso únicamente aquellas películas que se hayan estrenado en el año introducido por parámetro.

Proceso 2: Recibirá un número indeterminado de películas y debe almacenarlas en un fichero de nombre peliculasXXXX, donde XXXX es el año de estreno de las películas.

Main: Pide al usuario que introduzca un año por teclado, debe ser menor al actual. También solicitará la ruta al fichero donde se encuentran almacenadas las películas.
Piensa cuál es la mejor forma de comunicación entre los procesos e implementa las llamadas a los mismos atendiendo a ella. 
"""

import datetime
from multiprocessing import Pipe, Process


def lee_y_envia_peliculas(conn, ruta, año):
    """
    Proceso 1:
    Lee el fichero de películas y envía solo las del año indicado.
    """
    with open(ruta, "r", encoding="utf-8") as fichero:
        for linea in fichero:
            nombre, año_pelicula = linea.strip().split(";")
            if int(año_pelicula) == año:
                conn.send((nombre, año_pelicula))

    
    conn.send(None)
    conn.close()


def almacena_peliculas(conn, año):
    """
    Proceso 2:
    Recibe un número indeterminado de películas y las almacena en un fichero.
    """
    nombre_fichero = f"./Boletin2/ejercicio4/peliculas{año}.txt"

    with open(nombre_fichero, "a", encoding="utf-8") as fichero:
        for pelicula in iter(conn.recv, None):
            nombre, año_pelicula = pelicula
            fichero.write(f"{nombre};{año_pelicula}\n")
    conn.close()


def main():
    # Pedir año
    año_actual = datetime.date.today().year
    año = int(input("Introduce un año por consola: "))

    while año > año_actual:
        año = int(input("El año introducido es mayor que el actual, introduce uno correcto: "))

    # Pedir ruta del fichero
    nombre_fichero = input("Introduce el nombre del fichero que almacena las películas: ")
    ruta = f"./Boletin2/ejercicio4/{nombre_fichero}"

    # Crear Pipe
    conn_padre, conn_hijo = Pipe()

    # Crear procesos
    proceso1 = Process(target=lee_y_envia_peliculas, args=(conn_padre, ruta, año))
    proceso2 = Process(target=almacena_peliculas, args=(conn_hijo, año))

    # Lanzar procesos
    proceso1.start()
    proceso2.start()

    # Esperar a que terminen
    proceso1.join()
    proceso2.join()


if __name__ == "__main__":
 main()