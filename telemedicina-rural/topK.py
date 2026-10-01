import json
import heapq


def cargar_pacientes(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    return datos["pacientes"]


def seleccionar_top_k(pacientes, k):

    if k <= 0:
        raise ValueError("K debe ser un entero positivo")

    min_heap = []

    for orden, paciente in enumerate(pacientes):

        # guardamos: IVMT, orden de llegada, ID y nombre
        elemento = (
            paciente["ivmt"],
            -orden,
            paciente["id"],
            paciente["nombre"]
        )

        # mientras no tengamos K pacientes, agregamos directamente
        if len(min_heap) < k:
            heapq.heappush(min_heap, elemento)

        # si ya tenemos K, reemplazamos al de menor IVMT
        elif elemento > min_heap[0]:
            heapq.heapreplace(min_heap, elemento)

    # ordenamos solamente los K pacientes seleccionados
    min_heap.sort(key=lambda x: x[0], reverse=True)

    resultado = []

    for paciente in min_heap:
        resultado.append({
            "id": paciente[2],
            "nombre": paciente[3],
            "ivmt": paciente[0]
        })

    return resultado


def main():

    archivo = "pacientes.json"
    k = 10

    pacientes = cargar_pacientes(archivo)

    seleccionados = seleccionar_top_k(pacientes, k)

    print(f"Top {k} pacientes con mayor IVMT:")
    print("-" * 50)

    for posicion, paciente in enumerate(seleccionados, 1):
        print(
            f"{posicion}. "
            f"{paciente['id']} - "
            f"{paciente['nombre']} - "
            f"IVMT: {paciente['ivmt']}"
        )


if __name__ == "__main__":
    main()