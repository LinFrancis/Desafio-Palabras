import time

print('Bienvenidx al juego Ahorcado - Desafíos entre dos jugadores')
print('')
time.sleep(2)
print("Sí, para dos personas que se desafían a jugar")
time.sleep(2)
print('')
nombrej1 = input ("¿Quién desafía? ")
time.sleep(1)
nombrej2 = input("¿Quién ha sido desafiado? ")
print('')
print('')
time.sleep(2)
print("Perfecto, "+nombrej1+" desafía a "+nombrej2+".")
print('')
time.sleep(1)
print('Ahora, vamos a jugar')
time.sleep(1)
print('')
time.sleep(1)
print('¿Listos?')
time.sleep(1)
print('')
print('1')
time.sleep(1)
print('')
print('2')
time.sleep(1)
print('')
print('y')
time.sleep(1.5)
print('')
print('3')
print("")
time.sleep(1)
print("")



print(nombrej1+". ¿Con cuántas palabras secretas desafías a "+nombrej2+"? ",end="")
numero = int(input())
print("")
time.sleep(1)
print(nombrej2+" no mires lo que "+nombrej1+" escribirá ahora. Sería hacer trampa")
print("")
time.sleep(2)
print(nombrej1+" por favor, usando letra minuscula...")
time.sleep(2)
if numero < 1:
    print("¡Imposible!")
else:
    palabras = []
    for i in range(numero):
        print("Dígame la palabra secreta", str(i + 1) + ": ", end="")
        word = input()
        palabras += [word]
    print("Sus palabras secretas son:", palabras)



print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

## Comienzo del juego

print("¡A jugar!")
print(" ")

import random
AHORCADO = ['''
      +---+
      |   | 
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']



def buscarPalabraAleat(listaPalabras):
    # Esta funcion retorna una palabra aleatoria.
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]

def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(AHORCADO[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)): # Remplaza los espacios en blanco por la letra bien escrita
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print (letra, fin)
    print ("")

def elijeLetra(algunaLetra):
    # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
    while True:
        print (nombrej2+'. Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce una sola letra.') 
        elif letra in algunaLetra:
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letra

def empezar():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print (nombrej2+' ¿Quieres continuar el desafío con las otras palabras? (Si o No)')
    return input().lower().startswith('s')

print ('¡AHORCADO! '+nombrej1+' desafía a ' +nombrej2+' con '+str(numero)+' palabras secretas')
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscarPalabraAleat(palabras)
finJuego = False
while True:
    displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
    # El usuario elije una letra.
    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        # Se fija si el jugador ganó
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ("¡Muy bien "+nombrej2+"! La palabra secreta es '"+ palabraSecreta + "' ¡Has ganado el desafío!")
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
        if len(letraIncorrecta) == len(AHORCADO) - 1:
            displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
            print (nombrej2+' ¡Te has quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
            print('')
            print ("¡"+nombrej1+" gana el desafio!")
            finJuego = True
    # Pregunta al jugador si quiere jugar de nuevo
    print('')
    time.sleep(1)
    
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabraSecreta = buscarPalabraAleat(palabras)
        else:
            print("El desafío ha terminado. Muchas gracias "+nombrej1+" y "+nombrej2+" por jugar.")
            break
