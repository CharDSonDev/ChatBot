import re
import random
from typing import List


class RespuestaBot:
    def __init__(self, respuesta: str, palabras_reconocidas: List[str], palabras_requeridas: List[str] = []):
        self.respuesta = respuesta
        self.palabras_reconocidas = palabras_reconocidas
        self.palabras_requeridas = palabras_requeridas

    def calcular_probabilidad_coincidencia(self, mensaje: str) -> int:
        patron = re.compile('|'.join(self.palabras_reconocidas))
        coincidencias = patron.findall(mensaje)

        certeza_mensaje = float(len(coincidencias)) / \
            float(len(self.palabras_reconocidas))

        tiene_palabras_requeridas = all(
            palabra in mensaje for palabra in self.palabras_requeridas)

        if tiene_palabras_requeridas:
            return int(certeza_mensaje * 100)
        else:
            return 0


def obtener_respuesta(entrada_usuario: str) -> str:
    mensaje_partido = entrada_usuario.lower().split()

    respuestas = [
        RespuestaBot('La educación sexual es un derecho y una necesidad para todas las personas.', [
                     'educacion', 'sexual', 'derecho', 'necesidad']),
        RespuestaBot('Es importante hablar de educación sexual desde temprana edad para desarrollar una sana sexualidad.', [
                     'importante', 'hablar', 'temprana', 'edad', 'desarrollar', 'sana', 'sexualidad'], palabras_requeridas=['importante']),
        RespuestaBot('La educación sexual también abarca temas como el consentimiento y la salud sexual y reproductiva.', [
                     'educacion', 'sexual', 'abarca', 'temas', 'consentimiento', 'salud', 'reproductiva']),
        RespuestaBot('Es fundamental que las mujeres tengan acceso a información y recursos para su educación sexual.', [
                     'fundamental', 'mujeres', 'acceso', 'informacion', 'recursos', 'educacion', 'sexual'])
    ]

    mejor_coincidencia = max(
        respuestas, key=lambda x: x.calcular_probabilidad_coincidencia(mensaje_partido))

    if not mejor_coincidencia:
        return desconocido()
    else:
        return mejor_coincidencia.respuesta


def desconocido() -> str:
    respuesta = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres',
                 'búscalo en google a ver que tal'][random.randrange(3)]
    return respuesta


while True:
    print("Bot: " + obtener_respuesta(input('You: ')))
