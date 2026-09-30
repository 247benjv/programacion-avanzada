import json

class NodoPersona:
    def __init__(self, id_persona, nombre, sexo):
        self.id = id_persona
        self.nombre = nombre
        self.sexo = sexo
        self.padres = []
        self.hijos = []

class ArbolGenealogico:
    def __init__(self):
        self.nodos = {}
        self.nombres = {}


    def cargar_desde_json(self, ruta_archivo):
        # lector del archivo json
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)

        for persona_data in datos['personas']:
            nuevo_nodo = NodoPersona(
                persona_data['id'], 
                persona_data['nombre'], 
                persona_data['sexo']
            )
            self.nodos[nuevo_nodo.id] = nuevo_nodo
            self.nombres[nuevo_nodo.nombre.lower()] = nuevo_nodo.id

        for relacion in datos['padres']:
            id_padre = relacion['padre']
            id_hijo = relacion['hijo']

            if id_padre in self.nodos and id_hijo in self.nodos:
                nodo_padre = self.nodos[id_padre]
                nodo_hijo = self.nodos[id_hijo]
                
                nodo_hijo.padres.append(nodo_padre)
                nodo_padre.hijos.append(nodo_hijo)
    #  para buscar y retornar por el nombre de la persona
    def buscar_persona(self, nombre):
        id_persona = self.nombres.get(nombre.lower())
        if id_persona:
            return self.nodos[id_persona]
        return None

    def consulta_padres_hermanos(self, nombre):
        persona = self.buscar_persona(nombre)
        if not persona:
            print(f"Error: La persona '{nombre}' no existe en el árbol genealógico.")
            return

        # obtener nombre de los padres
        nombres_padres = [p.nombre for p in persona.padres]

        # obtener hermanos
        hermanos = set()
        for padre in persona.padres:
            for hijo in padre.hijos:
                if hijo.id != persona.id:
                    hermanos.add(hijo.nombre)

        print(f"\n--- Padres y Hermanos de: {persona.nombre} ---")
        print(f"Padres: {', '.join(nombres_padres) if nombres_padres else 'No registrados'}")
        print(f"Hermanos: {', '.join(hermanos) if hermanos else 'Ninguno'}")

if __name__ == "__main__":
    arbol = ArbolGenealogico()
    archivo_json = 'arbol_genealogico.json'
    
    try:
        arbol.cargar_desde_json(archivo_json)
        print("Árbol genealógico cargado exitosamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_json}'.")
        print("Asegúrate de que esté en la misma carpeta que este script de Python.")
        exit()

    while True:
        print("\n" + "="*50)
        nombre_input = input("Ingrese el nombre de la persona a consultar: ")
        
        # Ejecutar las dos consultas obligatorias
        if arbol.buscar_persona(nombre_input):
            arbol.consulta_padres_hermanos(nombre_input)
        else:
            print(f"Error: La persona '{nombre_input}' no se encuentra en el registro.")