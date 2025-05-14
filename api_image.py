from PIL import Image
import glob
import os



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
