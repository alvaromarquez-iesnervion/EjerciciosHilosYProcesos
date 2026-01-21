"""
En este ejercicio debes implementar los siguientes procesos y el Main como se explica a continuación:

Proceso 1: Genera 6 números aleatorios entre 1 y 10, ambos inclusive, y los guarda en un fichero. Estos números deben contener decimales. 
La ruta a este fichero se le indicará como parámetro de entrada. Estos 6 números representan las notas de un alumno.

Proceso 2: Lee un fichero pasado por parámetro que contiene las notas de un alumno, cada una en una línea distinta, y realiza la media de las notas. 
También recibe como parámetro el nombre del alumno. Esta media se almacenará en un fichero de nombre medias.txt. Al lado de cada media debe aparecer el 
nombre del alumno, separados por un espacio.

Proceso 3: Lee el fichero medias.txt. En cada línea del fichero aparecerá una nota, un espacio y el nombre del alumno. Este proceso debe leer el fichero y 
obtener la nota máxima. Imprimirá por pantalla la nota máxima junto con el nombre del alumno que la ha obtenido.

Main: Lanza 10 veces el primer proceso de forma concurrente. Cada una de esas veces debe guardarse el resultado en un fichero distinto. Es decir, 
al final tiene que haber 10 ficheros distintos con las notas de cada alumno. Pon a los ficheros nombres como Alumno1.txt, Alumno2.txt, …, Alumno10.txt.

A continuación, se debe lanzar el proceso 2 que toma los ficheros creados en el paso anterior como entrada. Por lo que el proceso 2 se 
lanzará 10 veces también, una por cada fichero generado por el proceso 1, y realizarlo todo de forma simultánea/concurrente. Es decir, debe haber 
10 procesos ejecutándose simultáneamente.

Por último, debe lanzarse el proceso 3. Hay que tener presente que para que este proceso pueda funcionar correctamente deben estar todas las notas ya escritas.
Prueba a realizar el ejercicio haciendo uso de Pool y haciendo uso de bucles for.
"""
import random

def generar_notas_alumno(ruta_fichero: str, num_notas: int = 6) -> str:
    """
    Genera notas aleatorias con decimales y las guarda en un fichero.
    """
    with open(ruta_fichero, "w", encoding="utf-8") as fichero:
        for _ in range(num_notas):
            nota = round(random.uniform(1, 10), 2) 
            fichero.write(f"{nota}\n")

    return ruta_fichero

def calcular_media_alumno(ruta_notas: str, nombre_alumno: str, ruta_medias: str):
    """
    Calcula la media de las notas de un alumno y la guarda en el fichero de medias.
    """
    with open(ruta_notas, "r", encoding="utf-8") as fichero:
        notas = [float(linea.strip()) for linea in fichero]

    media = sum(notas) / len(notas)

    with open(ruta_medias, "a", encoding="utf-8") as fichero_medias:
        fichero_medias.write(f"{media:.2f} {nombre_alumno}\n")  


def obtener_mejor_alumno(ruta_medias: str):
    """
    Lee el fichero de medias y muestra el alumno con la nota más alta.
    """
    nota_maxima = float("-inf")
    mejor_alumno = ""

    with open(ruta_medias, "r", encoding="utf-8") as fichero:
        for linea in fichero:
            nota, nombre = linea.strip().split(maxsplit=1)
            nota = float(nota)

            if nota > nota_maxima:
                nota_maxima = nota
                mejor_alumno = nombre

    print(f"La nota máxima es {nota_maxima:.2f} y la obtuvo {mejor_alumno}")


from multiprocessing import Pool
import os

def main():
    ruta_medias = "./Boletin2/ejercicio3/medias.txt"

    # Limpiar fichero de medias si existe
    if os.path.exists(ruta_medias):
        os.remove(ruta_medias)

    alumnos = [f"Alumno{i}" for i in range(1, 11)]
    ficheros_notas = [f"./Boletin2/ejercicio3/{alumno}.txt" for alumno in alumnos]

    # PROCESO 1: generar notas concurrentemente
    with Pool() as pool:
        pool.starmap(generar_notas_alumno, [(fichero,) for fichero in ficheros_notas])

    # PROCESO 2: calcular medias concurrentemente
    with Pool() as pool:
        pool.starmap(
            calcular_media_alumno,
            [(fichero, alumno, ruta_medias) for fichero, alumno in zip(ficheros_notas, alumnos)]
        )

    # PROCESO 3: solo cuando todo ha terminado
    obtener_mejor_alumno(ruta_medias)


if __name__ == "__main__":
    main()
