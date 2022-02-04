# if 1 == 2:
    # print('hola')
    # print('Como estas')

# else:
    # print('Buenos dias')

# elif 1 == 1:
    # print('Bienvenido')

8 < 10
3 > 2
5 == 5
2 != 3

password = input()


if password == 'paloma':
    print('welcome!')

password = input('Ingrese una contraseña: ')

if len(password) > 5:
    if password == 'paloma':
        print('welcome!')
    else:
        print('contraseña incorrecta')
else:
    print('contraseña invalida')