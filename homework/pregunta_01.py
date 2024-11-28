# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


import os
import pandas as pd

def pregunta_01():

    def process_folder(base_path, output_csv):
        # Lista para almacenar las filas de datos
        data = []

        # Recorrer las carpetas dentro de la ruta base
        for folder in os.listdir(base_path):
            folder_path = os.path.join(base_path, folder)
            if os.path.isdir(folder_path):  # Verificar si es una carpeta
                target = folder  # El nombre de la carpeta será el valor de `target`
                for filename in os.listdir(folder_path):
                    if filename.endswith(".txt"):  # Procesar solo archivos .txt
                        file_path = os.path.join(folder_path, filename)
                        with open(file_path, "r", encoding="utf-8") as file:
                            line = file.readline().strip()  # Leer la primera línea y eliminar espacios
                            if line:  # Solo agregar si la línea no está vacía
                                data.append({"phrase": line, "target": target})

        # Crear el DataFrame organizado con columnas en orden
        df = pd.DataFrame(data, columns=["phrase", "target"])

        # Asegurar que el directorio de salida existe
        os.makedirs(os.path.dirname(output_csv), exist_ok=True)

        # Guardar en un archivo CSV
        df.to_csv(output_csv, index=False, encoding="utf-8")
        print(f"Datos estructurados guardados en {output_csv}")

    # Procesar el conjunto "train"
    process_folder("files/input/train", "files/output/train_dataset.csv")

    # Procesar el conjunto "test"
    process_folder("files/input/test", "files/output/test_dataset.csv")


"""
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
