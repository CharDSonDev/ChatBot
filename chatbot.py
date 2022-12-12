import nltk
import json

try:
    with open("qa.json", "r") as f:
        qa = json.load(f)
except FileNotFoundError:
    print("Error: no se pudo encontrar el archivo qa.json.")
    exit(1)
except PermissionError:
    print("Error: no se tienen permisos para leer el archivo qa.json.")
    exit(1)

# creamos un diccionario con las preguntas y sus respuestas asociadas
questions = {
    "menstruacion": qa["¿Qué es la menstruacion?"],
    "periodo": qa["¿Cuál es la duración del periodo femenino?"],
    "relaciones": qa["¿Qué son las relaciones sexuales?"],
    "cuerpo": qa["¿Cómo funciona el cuerpo humano?"],
    "desarrollo": qa["¿Qué es el desarrollo?"],
}

while True:
    # pedimos una pregunta al usuario
    question = input("Tú: ")

    # si el usuario ingresa la palabra "salir", salimos del ciclo
    if question == "salir":
        break

    # utilizamos NLTK para tokenizar la pregunta del usuario
    tokens = nltk.word_tokenize(question)

    # buscamos la respuesta en el diccionario de preguntas
    for token in tokens:
        if token in questions:
            print("Bot: ", questions[token])
        else:
            print("Bot: Lo siento, no tengo una respuesta para esa pregunta.")
