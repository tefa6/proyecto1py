# api.py
import pandas as pd
from sodapy import Socrata

def obtener_datos(nombre_departamento, limite_registros):
    # Configuración del cliente Socrata para obtener datos públicos
    client = Socrata("www.datos.gov.co", None)  # No se requiere token para conjuntos de datos públicos
    
    try:
        # Construir la consulta usando un filtro WHERE para el departamento
        where_clause = f"departamento_nom = '{nombre_departamento}'"
        results = client.get("gt2j-8ykr", limit=limite_registros, where=where_clause)
        print(f"Resultados filtrados obtenidos: {results[:5]}")  # Muestra los primeros 5 resultados para verificación
        
        if not results:
            print("No se encontraron resultados.")
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return []

    # Filtrar solo las columnas requeridas
    columnas_requeridas = ['ciudad_municipio_nom', 'departamento_nom', 'edad', 'ubicacion', 'estado', 'pais_viajo_1_nom']
    datos_filtrados = [{col: result.get(col, 'N/A') for col in columnas_requeridas} for result in results]

    print(f"Datos filtrados: {datos_filtrados}")  # Verifica los datos filtrados
    return datos_filtrados
