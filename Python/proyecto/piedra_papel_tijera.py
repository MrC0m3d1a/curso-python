import random

opciones = ('piedra', 'papel', 'tijera')
pc0ption = random.choice(opciones)

user0ption = input('Piedra, papel o tijera? ')
print(pc0ption)

if user0ption == pc0ption:
    print('empate')

elif user0ption == 'piedra':
    if pc0ption == 'papel':
        print('Has perdido jijija')
    elif pc0ption == 'tijera':
        print('Ganaste :D')

elif user0ption == 'papel':
    if pc0ption == 'tijera':
        print('Perdiste :C')
    elif pc0ption == 'piedra':
        print('tu ganas')
    
elif user0ption == 'tijera':
    if pc0ption == 'piedra':
        print('Buen intento')
    elif pc0ption == 'papel':
        print('Bien jugado')

