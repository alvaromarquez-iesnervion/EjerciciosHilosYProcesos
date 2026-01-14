
from multiprocessing import Pool

def square(number):
    """Funcion que calcula el cuadrado de un número"""
    return number*number

if __name__=='__main__':
    #Con Pool indicamos que vamos a tener 3 procesos en paralelo
    with Pool(processes=3) as pool:
        numbers=[1,2,3,4,5,6]
        results=pool.map(square, numbers)

    print("Resultados:", results)