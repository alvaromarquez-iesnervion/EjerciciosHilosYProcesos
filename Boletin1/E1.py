# Importamos la clase Process del módulo multiprocessing
# Nos permite crear y gestionar procesos independientes
from multiprocessing import Process

"""
Crea una función en Python que sea capaz de sumar todos los números 
desde el 1 hasta un valor introducido por parámetro, incluyendo ambos 
valores y mostrar el resultado por pantalla.
Desde el programa principal crea varios procesos que ejecuten la 
función anterior. El programa principal debe imprimir un mensaje 
indicando que todos los procesos han terminado después de que los 
procesos hayan impreso el resultado.
"""

# Definimos una función que recibe un número entero como parámetro
def suma_desde_1(numero: int):
    # Inicializamos la variable suma a 0
    suma = 0
    
    # Recorremos los números desde 1 hasta 'numero' (incluido)
    for i in range(1, numero + 1):
        # Vamos acumulando la suma
        suma += i
    
    # Mostramos por pantalla el resultado de la suma
    print(f"Suma hasta {numero}: {suma}")

# Este bloque se ejecuta solo si el archivo es el programa principal
# Es OBLIGATORIO cuando se usa multiprocessing (especialmente en Windows)
if __name__ == "__main__":

    # Creamos varios procesos, cada uno ejecutará la función suma_desde_1
    # con un número distinto como argumento
    p1 = Process(target=suma_desde_1, args=(3,))
    p2 = Process(target=suma_desde_1, args=(4,))
    p3 = Process(target=suma_desde_1, args=(5,))
    p4 = Process(target=suma_desde_1, args=(6,))
    p5 = Process(target=suma_desde_1, args=(7,))

    # Iniciamos la ejecución de los procesos
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    # join() bloquea el programa principal hasta que el proceso termine
    # Aquí esperamos a que TODOS los procesos finalicen
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

    # Este mensaje solo se imprime cuando todos los procesos han terminado
    print("Todos los procesos han terminado")

    
    # Otra forma más ordenada y escalable de hacer lo mismo
    

    # Creamos una lista para almacenar los procesos
    procesos = []

    # Creamos procesos en un bucle para los valores del 3 al 7
    for n in range(3, 8):
        # Creamos el proceso
        p = Process(target=suma_desde_1, args=(n,))
        
        # Lo añadimos a la lista
        procesos.append(p)
        
        # Iniciamos el proceso
        p.start()

    # Esperamos a que todos los procesos de la lista terminen
    for p in procesos:
        p.join()

    # Mensaje final cuando todos han acabado
    print("Todos los procesos han terminado")
