# Tarea TopK

**Estudiante:** Benjamín López
**Profesor:** Ricardo Gacitua
**Curso:** Programación Avanzada - ICC708

## Descripción

El programa selecciona los **K pacientes con mayor Índice de Vulnerabilidad Médico-Territorial (IVMT)** a partir de los datos almacenados en `pacientes.json`.

Para realizar la selección se utiliza un **Min-Heap** mediante la librería `heapq`. El Heap mantiene como máximo **K pacientes** y en su raíz queda el paciente con menor IVMT de los seleccionados. Cuando aparece un paciente con un puntaje mayor, se reemplaza al que tiene el menor puntaje.

De esta forma, no es necesario ordenar todos los pacientes, sino que se van procesando uno por uno y se mantienen solamente los **K mejores**. Al finalizar, estos pacientes se ordenan de mayor a menor IVMT para mostrar el resultado.

La complejidad del algoritmo es **O(N log K)** y la estructura utilizada para mantener los pacientes seleccionados ocupa **O(K)** espacio.

El archivo `pacientes.json` contiene los datos de los pacientes, por lo que estos no se encuentran escritos directamente en el código. El valor de **K** se puede modificar según la cantidad de cupos disponibles.