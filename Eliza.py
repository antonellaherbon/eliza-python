import random

def Nombrearchivo(lista_palabras,index):
    if index < len(lista_palabras):
        for clave,lista_disparadores in disparadores.items():
            if lista_palabras[index] in lista_disparadores:
                return 'Preguntas'+clave+'.txt'
        return Nombrearchivo(lista_palabras,index+1)
    return ""

disparadores = {
    'Tristeza': ['mal', 'llorar', 'triste', 'tristeza', 'soledad', 'desahuciado', 'solo', 'pena', 'duelo', 'depresivo', 'depresion', 'desanimado', 'sin'],
    'Miedos': ['miedo', 'asustado', 'terror', 'fobia', 'susto', 'perplejo', 'angustia', 'atonito','ansioso'],
    'Felicidad': ['feliz', 'contento', 'alegre', 'entusiasmado', 'bien', 'jocoso', 'alegria', 'placentero', 'jubilo']
}

print("Bienvenidos a ELIZA, el juego de ayuda psicológica")
print("Para salir del juego, escriba 'Chau'")
print("Hola, ¿Cómo te encuentras hoy?")
respuesta = input("Ingrese su respuesta: ")

archivo = Nombrearchivo(respuesta.lower().split(),0)
listaPreguntas = []

if archivo == '':
    print("No puedo ayudarte con tu problema! Lo siento")
else:
    try:
        archivoAbierto = open(archivo, "rt", encoding="UTF-8")
        for pregunta in archivoAbierto:
            listaPreguntas.append(pregunta)
    except FileNotFoundError:
        print("el archivo no existe")
    except OSError:
        print("no se puede abrir el archivo")
    finally:
        try:
            archivoAbierto.close()
        except OSError:
            print("no se puede cerrar el archivo")

    pregunta_anterior = None
    while respuesta != 'chau':
        preguntaelegida = random.choice(listaPreguntas)
        while preguntaelegida == pregunta_anterior: 
            preguntaelegida = random.choice(listaPreguntas)
        print(preguntaelegida)
        pregunta_anterior = preguntaelegida
        respuesta = input("Ingrese su respuesta: ").lower()

print("El juego ha terminado! Esperamos que haya sido de tu agrado.")
