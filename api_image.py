from PIL import Image
import glob
import os
import requests
import json


# Para la pr  ctica de Coursera
directorio_imagenes = os.path.dirname(os.path.abspath(__file__))
patron = os.path.join(directorio_imagenes, "*.tiff")
directorio_destino = "./opt/icons/"

ruta_absoluta = os.path.abspath(directorio_imagenes)
print("Soy ruta_absoluta: " + ruta_absoluta)

ruta_directorio_padre = os.path.dirname(ruta_absoluta)
print("Soy directorio_padre: " + ruta_directorio_padre)

if not os.path.exists(ruta_directorio_padre + "/opt/icons/"):
    print("KAKA")

# Recorro la carpeta buscando todas las im  genes
print("Empiezo bucle")
for nombre_archivo in os.listdir(directorio_imagenes):
    nombre_base, extension = os.path.splitext(nombre_archivo)

    if not extension:
        try:
            tiff_image = Image.open(nombre_archivo)
            new_img = tiff_image.convert("RGB").rotate(90).resize((128,128),Image.Resampling.NEAREST)
            new_img.save(ruta_directorio_padre + "/opt/icons/" + nombre_archivo + ".jpeg")
        except Exception as e:
            print(f"Error al procesar: {nombre_archivo}: {e}")


#NUEVA PARTE DE PRACTICA
directorio_feedbacks = ""
#Creamos un diccionario donde almacenar los datos de cada fichero:
diccionario = {}

cont_lineas = 1

url = "http://http://34.75.9.73//feedback"

for feedback_file in os.listdir(directorio_feedbacks):
    print(feedback_file)
    cont_lineas = 1
    ruta_completa = os.path.join(directorio_feedbacks, feedback_file)
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            for linea in f:
                if cont_lineas == 1:
                    diccionario['title'] = linea
                if cont_lineas == 2:
                    diccionario['name'] = linea
                if cont_lineas == 3:
                    diccionario['date'] = linea
                if cont_lineas == 4:
                    diccionario['feedback '] = linea
                
                cont_lineas +=1 
    except FileNotFoundError: 
        print(f"  Error: El archivo '{feedback_file}' no se encuentra.")

    print("Elementos del diccionario:")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")

    #Ahora lo mando al REST
    request.post()
