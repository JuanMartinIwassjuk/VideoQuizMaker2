import json
import audio
import os
from config import NUMBER_OF_QUESTIONS
from creatomate import Element

def generarArchivoDeljson(json):
    with open("resultado_json","w") as arch:
     arch.write(json.toJSON())


def generar_tiempo_video(cant_preguntas):
    duracion_audio_inicio= str(audio.obtener_duracion_mp3_en_segundos_sin_formato(os.path.abspath(os.path.join(os.getcwd(), 'audio', f"{str(NUMBER_OF_QUESTIONS)}.mp3")))+2.5) + ' s'
    resultado = audio.sumar_tiempos( (str(cant_preguntas * 12))+' s' ,duracion_audio_inicio)
    return resultado

def encontrar_indice(lista, cadena):
    try:
        indice = lista.index(cadena)
        return indice
    except ValueError:
        # Si no se encuentra la cadena en la lista, se devuelve -1
        return -1


def extraer_primer_prefijo(cadena):
    # Dividir la cadena en base al primer espacio
    partes = cadena.split(" ", 1)
    
    # Devolver la primera parte
    return partes[0]

def extraer_segundo_prefijo(cadena):
    # Dividir la cadena en base al primer espacio
    partes = cadena.split(" ", 1)
    
    # Devolver la primera parte
    return partes[1]


def dividir_texto(texto):
    palabras = texto.split()  # Dividimos el texto en una lista de palabras
    longitud_total = len(palabras)
    longitud_porcion = longitud_total // 3  # Dividimos el número total de palabras en tres partes aproximadamente iguales

    # Calculamos las longitudes de las tres partes
    longitud_parte1 = longitud_porcion
    longitud_parte2 = longitud_porcion


    parte1 = ' '.join(palabras[:longitud_parte1])
    parte2 = ' '.join(palabras[longitud_parte1: longitud_parte1 + longitud_parte2])
    parte3 = ' '.join(palabras[longitud_parte1 + longitud_parte2:])

    print(parte1)
    print(parte2)
    print(parte3)

    # Creamos los elementos con las partes de texto
    elemento1 = Element("text", track=43, text=str(parte1), fill_color="#ffffff", x="50%", y="25%", font_size="35vmin", width=800, height=400, x_alignment="0%", y_alignment="0%", letter_spacing="75%", font_family="Arial Black")
    elemento2 = Element("text", track=44, text=str(parte2), fill_color="#ffffff", x="50%", y="45%", font_size="35vmin", width=800, height=400, x_alignment="0%", y_alignment="0%", letter_spacing="75%", font_family="Arial Black")
    elemento3 = Element("text", track=45, text=str(parte3), fill_color="#ffffff", x="50%", y="65%", font_size="35vmin", width=800, height=40, x_alignment="0%", y_alignment="0%", letter_spacing="75%", font_family="Arial Black")

    return elemento1, elemento2, elemento3



dividir_texto("It is impossible to get a 10/10. Let\'s get started!")

