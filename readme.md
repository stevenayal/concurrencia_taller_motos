# Documentación del Taller de Reparación de Motos

## Identificación y Descripción del Problema

### Situación Elegida: Taller de Reparación de Motos

Un taller de reparación de motos donde varios mecánicos trabajan simultáneamente en diferentes motos. Cada mecánico realiza tareas como cambiar aceite, reparar frenos y ajustar la cadena. Esto crea un entorno de concurrencia en el que múltiples procesos pueden ocurrir al mismo tiempo.

### Consecuencias Nocivas de la Concurrencia

| Problema                  | Descripción                                                               |
|---------------------------|---------------------------------------------------------------------------|
| Confusión de Herramientas | Dos mecánicos pueden intentar usar las mismas herramientas simultáneamente.|
| Seguridad                 | Riesgo de accidentes si un mecánico no sabe que otro está trabajando.   |
| Interferencias            | Falta de comunicación puede causar retrasos y malentendidos.             |

### Eventos Concurrentes sin Importancia de Ordenamiento Relativo

| Tarea 1                | Tarea 2                |
|-----------------------|-----------------------|
| Cambio de aceite      | Ajuste de cadena      |
| Revisión de documentación | Reparación de frenos |

## Descripción de los Mecanismos de Sincronización Empleados

| Mecanismo      | Descripción                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `Lock`         | Asegura que solo un mecánico pueda utilizar las herramientas simultáneamente.|
| `Queue`        | Maneja las tareas asignadas a los mecánicos, asegurando que no haya solapamientos. |

## Lógica de Negocio

1. Cada mecánico toma tareas de una cola.
2. Utiliza un `Lock` para acceder a las herramientas.
3. Completa las tareas asignadas y notifica la finalización.

## Identificación del Estado Compartido

| Variable/Estructura | Descripción                                |
|---------------------|--------------------------------------------|
| `tool_lock`         | Un objeto `Lock` que sincroniza el uso de herramientas. |
| `task_queue`        | Una cola que almacena las tareas asignadas a los mecánicos. |

## Descripción Algorítmica del Avance de Cada Hilo/Proceso

1. **Inicio del Hilo:**
   - Cada mecánico inicia su hilo y entra en un bucle para tomar tareas de la cola.
   
2. **Obtención de Tareas:**
   - Intenta obtener una tarea de `task_queue`.
   - Si no hay tareas, el hilo finaliza.

3. **Ejecución de Tareas:**
   - Utiliza `Lock` para asegurar herramientas.
   - Realiza la tarea y notifica la finalización.

4. **Terminación del Hilo:**
   - Cuando no hay más tareas, el hilo finaliza.

## Descripción de la Interacción entre Hilos/Procesos

- **Uso de `Lock`:** Los mecánicos adquieren el `Lock` antes de usar herramientas y lo liberan al finalizar la tarea.
- **Uso de `Queue`:** Los mecánicos interactúan con la cola para obtener tareas, lo que evita solapamientos y asegura que cada tarea se realice una sola vez.

## Descripción del Entorno de Desarrollo

| Aspecto                      | Detalles                                                      |
|------------------------------|--------------------------------------------------------------|
| **Lenguaje**                 | Python                                                       |
| **Versión**                  | Python 3.8 o superior                                       |
| **Bibliotecas**              | `threading`, `time`, `random`, `queue` (bibliotecas estándar) |
| **Sistema Operativo**        | Desarrollado y probado en Windows 10 y Linux (Ubuntu 20.04) |

## Ejemplos o Pantallazos de una Ejecución Exitosa

### Ejemplo de Salida