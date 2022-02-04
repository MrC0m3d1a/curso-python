from ast import Break
import random
palabras = ['ESTRATEGIA', 'PYTHON', 'JUEGOS', 'VICTORIA', 'PROGRAMACION', 'CODIGO', 'MRBOOMBASTIC', 'ENEMY']
palabra = random.choice(palabras)
user0ption = ''
vidas = 6
letrasIngresadas = []

while vidas > 0:
    letraUser = input('Ingrese una letra: ')
    letrasIngresadas.append(letraUser)
    palabraActual = ''
    for letra in palabra:
        if letra in letrasIngresadas:
            palabraActual += letra
        else:
            palabraActual += '- '
    print('Palabra: ' + palabraActual)
    if palabraActual == palabra:
     print('Enhorabuena, ganaste :D')
     break

    if letraUser in palabra: 
        print('Letra correcta')
    else: 
        vidas = vidas - 1
    print('vidas restantes: ' + str(vidas))
    
else:
     vidas = 0
     print('Lastima, has perdido :(')
     
    