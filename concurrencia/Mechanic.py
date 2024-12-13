import threading
import time
import random
from queue import Queue

# Clase que representa un mecánico
class Mechanic(threading.Thread):
    def __init__(self, name, tool_lock, task_queue):
        super().__init__()
        self.name = name
        self.tool_lock = tool_lock
        self.task_queue = task_queue

    def run(self):
        while True:
            try:
                # Obtener una tarea de la cola
                task_id = self.task_queue.get_nowait()
                self.perform_task(task_id)
                self.task_queue.task_done()
            except Exception:
                break

    def perform_task(self, task_id):
        # Sincronizamos el uso de herramientas
        with self.tool_lock:
            print(f"{self.name} ha comenzado a trabajar en tarea {task_id}.")
            time.sleep(random.uniform(1, 3))  # Simula el tiempo que lleva la tarea
            print(f"{self.name} ha terminado la tarea {task_id}.")

# Función principal para iniciar el taller
def main():
    # Lock para sincronizar el uso de herramientas
    tool_lock = threading.Lock()

    # Cola para asignar tareas
    task_queue = Queue()

    # Asignar tareas a la cola
    for i in range(5):  # 5 tareas diferentes
        task_queue.put(i)

    # Creación de mecánicos
    mechanics = [
        Mechanic("Mecánico 1", tool_lock, task_queue),
        Mechanic("Mecánico 2", tool_lock, task_queue),
        Mechanic("Mecánico 3", tool_lock, task_queue)
    ]

    # Iniciar los hilos
    for mechanic in mechanics:
        mechanic.start()

    # Esperar a que todos los hilos terminen
    task_queue.join()  # Esperar a que todas las tareas en la cola se completen

    # Finalizando los mecánicos
    for mechanic in mechanics:
        mechanic.join()

    print("Todos los mecánicos han terminado sus tareas.")

if __name__ == "__main__":
    main()