# Considerar el caso en que ambos números son iguales.

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un segundo numero: '))

if num1 == num2:
    print('el numero ' + str(num1) + ' es igual')

elif num1 < num2:
    print('el numero ' + str(num1) + ' es menor a ' + str(num2))

else:
  print('el numero ' + str(num2) + ' es menor a ' + str(num1))