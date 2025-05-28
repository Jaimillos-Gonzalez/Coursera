#!/usr/bin/env python3

import os
import json
from PIL import Image

def txt_to_json(directorio):
    for filename in os.listdir(directorio):
        if filename.endswith(".txt"):
            filepath = os.path.join(directorio, filename)
            try:
                with open(filepath, "r") as f:
                    # Leer el contenido del archivo TXT
                    content = f.read()

                    # Dividir el contenido en líneas (asumiendo un formato específico)
                    lines = content.splitlines()

                    # Extraer la información (ajusta esto según tu formato TXT)
                    name = lines[0].split(":")[1].strip() if len(lines) > 0 else ""
                    weight = int(lines[1].split(":")[1].strip()) if len(lines) > 1 else 0
                    description = lines[2].split(":")[1].strip() if len(lines) > 2 else ""
                    image_name = lines[3].split(":")[1].strip() if len(lines) > 3 else ""

                    # Crear el diccionario con la estructura JSON
                    data = {
                        "name": name,
                        "weight": weight,
                        "description": description,
                        "image_name": image_name
                    }

                    # Crear el nombre del archivo JSON de salida
                    new_filename = os.path.splitext(filename)[0] + ".json"
                    new_filepath = os.path.join(directorio, new_filename)

                    # Escribir el diccionario en un archivo JSON
                    with open(new_filepath, "w") as outfile:
                        json.dump(data, outfile, indent=4)  # indent=4 para formato legible

                    print(f"Archivo JSON generado: {filename} -> {new_filename}")

            except FileNotFoundError:
                print(f"Error: No se encontró el archivo {filename}")
            except Exception as e:
                print(f"Error al procesar {filename}: {e}")

if __name__ == "__main__":
    directorio_txt = "descriptions"  # Reemplaza con la ruta a tu directorio
    txt_to_json(directorio_txt)
    print("Proceso completado.")