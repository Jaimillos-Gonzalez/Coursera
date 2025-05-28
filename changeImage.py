#!/usr/bin/env python3

import os
from PIL import Image

def resize_and_convert_images(directorio):

    for filename in os.listdir(directorio):
        if filename.endswith(".tiff"):  
            filepath = os.path.join(directorio, filename)
            try:
                img = Image.open(filepath)

                # Convertir de RGBA a RGB si es necesario
                if img.mode == "RGBA":
                    img = img.convert("RGB")

                # Cambiar el tamaño de la imagen
                img = img.resize((600, 400))

                # Crear el nombre del archivo de salida
                new_filename = os.path.splitext(filename)[0] + ".jpeg"
                new_filepath = os.path.join(directorio, new_filename)

                # Guardar la imagen como JPEG
                img.save(new_filepath, "JPEG")

                print(f"Imagen convertida y redimensionada: {filename} -> {new_filename}")

            except FileNotFoundError:
                print(f"Error: No se encontró el archivo {filename}")
            except Exception as e:
                print(f"Error al procesar {filename}: {e}")

def convertir_jpg_a_tiff(archivo_jpg, archivo_tiff, ancho=3000, alto=2000):

    try:
        # Abrir la imagen JPG
        img = Image.open(archivo_jpg)

        # Cambiar el tamaño de la imagen
        img = img.resize((ancho, alto))

        # Guardar la imagen como TIFF
        img.save(archivo_tiff, "TIFF")

        print(f"Imagen convertida y redimensionada: {archivo_jpg} -> {archivo_tiff}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_jpg}")
    except Exception as e:
        print(f"Error al procesar {archivo_jpg}: {e}")

"""
if __name__ == "__main__":
    archivo_entrada = "Careto_Comic.jpg"  
    archivo_salida = "Careto_Comic.tiff" 

    convertir_jpg_a_tiff(archivo_entrada, archivo_salida)
    print("Proceso completado.")
"""

if __name__ == "__main__":
    directorio_imagenes = "c:\Solo_Jaime\WORKSPACE\Python\Coursera\Imagenes"  # Reemplaza con la ruta a tu directorio
    resize_and_convert_images(directorio_imagenes)
    print("Proceso completado.")
