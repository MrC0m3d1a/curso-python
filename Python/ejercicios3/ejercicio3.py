print('elija una opcion')
print('1 suma')
print('2 resta')
print('3 multiplicacion')
print('4 division')

opcion = input()
if opcion == '1':
    print('Ingrese un numero: ')
    num1 = int(input())
    print('Ingrese otro numero: ')
    num2 = int(input())
    resultado = num1 + num2
    print('el resultado de la suma es: ' + str(resultado))

elif opcion == '2':
    print('Ingrese un numero: ')
    num1 = int(input())
    print('Ingrese otro numero: ')
    num2 = int(input())
    resultado = num1 - num2
    print('el resultado de la resta es: ' + str(resultado))

elif opcion == '3':
    print('Ingrese un numero: ')
    num1 = int(input())
    print('Ingrese otro numero: ')
    num2 = int(input())
    resultado = num1 * num2
    print('el resultado de la multiplicacion es: ' + str(resultado))

elif opcion == '4':
    print('Ingrese un numero: ')
    num1 = int(input())
    print('Ingrese otro numero: ')
    num2 = int(input())
    resultado = num1 / num2
    print('el resultado de la division es: ' + str(resultado))
