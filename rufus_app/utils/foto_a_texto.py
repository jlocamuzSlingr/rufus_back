import re
import pytesseract
import cv2
import requests

from .texto_a_ingred import procesar_oracion

def obtener_texto_imagen(menu_object):
    url_imagen = menu_object['image']
    url_imagen_sin_host = url_imagen.replace('http://localhost:8000/', '')
    print(url_imagen_sin_host)
    # Cargar la imagen
    img = cv2.imread(url_imagen_sin_host)
    # Convertir la imagen a escala de grises
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Aplicar umbralización a la imagen
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # Obtener el texto de la imagen
    texto = pytesseract.image_to_string(img, lang='spa')
    print(texto)
    # Buscar precios en el texto utilizando expresiones regulares
    precios = re.findall(r'\$\d+', texto)
    # Dividir el texto en oraciones utilizando los precios como punto de separación
    oraciones = re.split(r'\$\d+', texto)
    # Pasar a minúsculas y eliminar saltos de línea
    texto = [linea.lower().replace('\n', '').rstrip() for linea in oraciones if linea.strip()]
    palabras_oraciones = []
    for oracion in texto:
        oracion = oracion.split('$')[0].strip()
        palabras_oraciones.append(procesar_oracion(oracion))
    print("palabras oraciones ",palabras_oraciones)
    return palabras_oraciones

if __name__ == '__main__':
    path_imagen = '/Users/julialocamuz/Downloads/wpp3.jpeg'
    texto_imagen = obtener_texto_imagen(path_imagen)
    print(texto_imagen)