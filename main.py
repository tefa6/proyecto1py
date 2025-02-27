# main.py
from api.api import obtener_datos
from ui.ui import obtener_entrada_usuario, mostrar_datos

def main():
    # Obtener entradas del usuario
    nombre_departamento, limite_registros = obtener_entrada_usuario()
    
    # Obtener datos de la API
    datos = obtener_datos(nombre_departamento, limite_registros)
    
    # Mostrar los datos obtenidos
    mostrar_datos(datos)

if __name__ == "__main__":
    main()
