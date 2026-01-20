from multiprocessing import Pipe, Process
import random


def generar_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def clase_ip(ip):
    primer_octeto = int(ip.split('.')[0])
    clase = None  

    if 1 <= primer_octeto <= 126:
        clase = 'A'
    elif 128 <= primer_octeto <= 191:
        clase = 'B'
    elif 192 <= primer_octeto <= 223:
        clase = 'C'

    return clase


def imprimir_ip(ip, clase):
    print(f"Dirección IP: {ip}, Clase: {clase}")

def proceso1_funcion(conn):
    for _ in range(10):
        conn.send(generar_ip())
    conn.close()  

def proceso2_funcion(conn_entrada, conn_salida):
    while conn_entrada.poll():  
        ip = conn_entrada.recv()
        clase = clase_ip(ip)
        if clase in ['A', 'B', 'C']:
            conn_salida.send((ip, clase))
    conn_entrada.close()
    conn_salida.close()

def proceso3_funcion(conn):
    while conn.poll():  
        ip, clase = conn.recv()
        imprimir_ip(ip, clase)
    conn.close()  

if __name__ == "__main__":
    
    conn1_p1, conn1_p2 = Pipe()
    conn2_p2, conn2_p3 = Pipe()

    p1 = Process(target=proceso1_funcion, args=(conn1_p1,))
    p2 = Process(target=proceso2_funcion, args=(conn1_p2, conn2_p2))
    p3 = Process(target=proceso3_funcion, args=(conn2_p3,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
