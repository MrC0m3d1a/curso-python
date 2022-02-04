import random

pc0ption = random.randint(1, 10)

vidas = 5

while True:
    print('Ingrese un numero del 1 al 10')
    user0ption = int(input())

    if pc0ption == user0ption:
        print('Has ganado!!! :D')
        break
    else:
        print('intente de nuevo')
        vidas = vidas - 1
        print('vidas restantes: ' + str(vidas))
    
    if vidas == 0:
        print('Se te han agotado las vidas: :/ ')
        break
