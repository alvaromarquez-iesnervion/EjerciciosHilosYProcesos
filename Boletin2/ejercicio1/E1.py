"""Crea un proceso que cuente las vocales de un fichero de texto. Para ello crea una función que reciba una vocal y devuelva 
cuántas veces aparece en un fichero. Lanza el proceso de forma paralela para las 5 vocales. 
Tras lanzarse se imprimirá el resultado por pantalla."""

from multiprocessing import Process, Manager
import os


def contar_vocal(vocal, ruta_fichero):
    if vocal.lower() not in "aeiou":
        raise ValueError("Debes pasar una vocal válida (a, e, i, o, u)")

    contador = 0
    vocal = vocal.lower()

    with open(ruta_fichero, "r", encoding="utf-8") as f:
        for linea in f:
            contador += linea.lower().count(vocal)

    print(f"La vocal {vocal} aparece {contador} veces.")

if __name__ == "__main__":
    fichero = "./Boletin2/ejercicio1/fichero.txt"
    vocales = ["a", "e", "i", "o", "u"]
    procesos = []

    for vocal in vocales:
        p = Process(target=contar_vocal, args=(vocal, fichero))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()
