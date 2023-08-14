"""1. Escriba una función redondear() que permita redondear un número
decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
anterior (3)"""

def redondear_numero(numero):
    if numero - int(numero) > 0.50:
        print(int(numero) + 1)
    else:
        print(int(numero))

redondear_numero(4.26)

"""2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
módulo que esté fuera de ese paquete, cree una función de suma de
decimales que redondee el resultado haciendo uso de la función
redondear() del paquete recién creado."""

from redondear import redondear_numero

def sum_decimales(numero_1,numero_2):
    resultado = numero_1 + numero_2
    redondeado = redondear_numero(resultado)
    return redondeado


sum_decimales(8.20,3.40)



"""3. Usando el módulo datetime, escribe un programa que muestre la fecha
y hora actuales del sistema."""

import datetime 

fecha = datetime.datetime.now()
print(fecha)


"""4. Escriba un programa que devuelva un número par al azar entre 2 y 10
(pista: para comprobar si se pueden generar todos los números, pruebe
ejecutar el programa dentro de un ciclo infinito)."""

import random

def azar():
    while True:
        numeor = random.randint(2,10)
        if numeor % 2 == 0:
            print(numeor)
                
azar()

"""5. Bola mágica La bola mágica (Magic 8 ball) es un popular juguete usado
para la adivinación o para buscar consejo. Su mecanismo es muy simple:
ante una pregunta del usuario, la bola responde con una de 8 posibles
respuestas:
- Es seguro que sí
- Las chances son buenas
- Puedes contar con ello
- Pregúntame de nuevo más tarde
- Concéntrate y pregunta de nuevo
- No veo con claridad, intenta de nuevo
- Mi respuesta es no
- Mis fuentes me dicen que no
Escriba una función en Python para simular la bola mágica."""

import random

def bola_Magica(pregunta):
    numero_magico = random.randint(1,8)
    if numero_magico == 1 :
        print("Es seguro que sí")
    elif numero_magico == 2 :
        print("Las chances son buenas")
    elif numero_magico == 3 :
        print("Puedes contar con ello")
    elif numero_magico == 4 :
        print("Pregúntame de nuevo más tarde")
    elif numero_magico == 5 :
        print("Concéntrate y pregunta de nuevo")
    elif numero_magico == 6 :
        print("No veo con claridad, intenta de nuevo")
    elif numero_magico == 7:
        print("Mi respuesta es no")
    elif numero_magico == 8 :
        print("Mis fuentes me dicen que no")

bola_Magica("puedo?")


"""6. Encuentre el tiempo de ejecución de los programas de los ejercicios
anteriores (pista: use el módulo time)"""

"""(Opcional) Sorteo: Escriba un programa que simule un sorteo donde
toman uno o más papeles al azar de un pozo para elegir los ganadores."""

nombres = []
for i in range(1,6):
    participante = input("Ingrese su nombre: ")
    nombres.append(participante)
elegir = random.choice(nombres)
print(elegir)

"""8. (Opcional) Escriba una función que pida al usuario ingresar su fecha de
nacimiento y sea capaz de devolver la cantidad de días desde su
nacimiento hasta hoy.
9. (Opcional) Implemente el programa del ejercicio 6 usando un diccionario."""