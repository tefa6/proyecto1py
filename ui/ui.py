# ui.py
import pandas as pd
from tabulate import tabulate

def obtener_entrada_usuario():
    # Solicitar al usuario los parámetros de consulta
    nombre_departamento = input("Ingrese el nombre del departamento que desea consultar: ")
    limite_registros = int(input("Ingrese el número de registros que desea obtener (p.ej., 5): "))
    return nombre_departamento, limite_registros

def mostrar_datos(datos):
    # Verifica si hay datos para mostrar
    if not datos:
        print("No se obtuvieron datos.")
        return
    
    # Crear un DataFrame a partir de los datos
    df = pd.DataFrame(datos)
    
    # Definir el subconjunto de columnas necesarias y su orden
    columnas_requeridas = ['ciudad_municipio_nom', 'departamento_nom', 'edad', 'ubicacion', 'estado', 'pais_viejo_1_nom']
    
    # Asegurarse de que todas las columnas requeridas están presentes en el DataFrame
    for columna in columnas_requeridas:
        if columna not in df.columns:
            df[columna] = 'N/A'
    
    # Filtrar solo las columnas necesarias y ordenar las filas
    df_subset = df[columnas_requeridas].copy()
    
    # Reemplazar valores nulos con 'N/A'
    df_subset.fillna('N/A', inplace=True)
    
    # Crear una lista de encabezados que se alineen con las columnas en el DataFrame
    encabezados = ['Ciudad de Ubicación', 'Departamento', 'Edad', 'Tipo', 'Estado', 'País de Procedencia']
    
    # Mostrar los datos en una tabla formateada
    print(tabulate(df_subset, headers=encabezados, tablefmt='grid', showindex=False))

