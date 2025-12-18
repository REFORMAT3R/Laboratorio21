import time
import random
import threading
import asyncio
from multiprocessing import Process
def consulta_bd(id):
    t = random.randint(1, 5)
    print(f"Consulta {id} (sync) tarda {t}s")
    time.sleep(t)

def con_hilos():
    inicio = time.time()
    hilos = []

    while len(hilos) < 3:
        h = threading.Thread(target=consulta_bd, args=(len(hilos)+1,))
        hilos.append(h)
        h.start()

    for h in hilos:
        h.join()

    print("Tiempo total hilos:", round(time.time() - inicio, 2))

async def consulta_async(id):
    t = random.randint(1, 5)
    print(f"Consulta {id} (async) tarda {t}s")
    await asyncio.sleep(t)

async def con_async():
    inicio = time.time()
    await asyncio.gather(
        consulta_async(1),
        consulta_async(2),
        consulta_async(3)
    )
    print("Tiempo total async:", round(time.time() - inicio, 2))

def con_procesos():
    inicio = time.time()
    procesos = []

    i = 1
    while i <= 3:
        p = Process(target=consulta_bd, args=(i,))
        procesos.append(p)
        p.start()
        i += 1

    for p in procesos:
        p.join()

    print("Tiempo total procesos:", round(time.time() - inicio, 2))

if __name__ == "__main__":
    con_hilos()
    asyncio.run(con_async())
    con_procesos()