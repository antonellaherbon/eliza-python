import random

def Nombrearchivo(i):
    for j in range(len(i)):
        if i[j] in disparadoresTristeza:
            return "PreguntasTristeza.txt"
        elif i[j] in disparadoresMiedos:
            return "PreguntasMiedos.txt"
        elif i[j] in disparadoresFelicidad:
            return "PreguntasFelicidad.txt"
        else:
            print("No puedo ayudarte con tu problema! Lo siento")
    return ''

print("Bienvenidos a ELIZA, el juego de ayuda psicológica")
print("Para salir del juego, escriba 'Chau'")
print("Hola, ¿Cómo te encuentras hoy?")

disparadoresTristeza = ['mal','llorar','triste','tristeza','soledad','desahuciado','solo']
disparadoresMiedos = ['miedo','asustado','terror','fobia','susto']
disparadoresFelicidad = ['feliz','contento','alegre','entusiasmado']

respuesta = input("Ingrese su respuesta: ")
i = (respuesta.lower()).split()
archivo = Nombrearchivo(i)
listaPreguntas = []

if archivo != '':
    try:
        archivoAbierto = open(archivo,"rt",encoding="UTF-8")
        for i in range(0,3):
            preg = archivoAbierto.readline()
            listaPreguntas.append(preg)
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
        respuesta = input("Ingrese su respuesta: ")
        respuesta = respuesta.lower()

print("El juego ha terminado! Esperamos que haya sido de tu agrado.")