# 3) Crear un programa que pida al usuario que ingrese 10 numeros con un bucle for y 
   # luego imprima la suma de todos los numeros
suma = 0
for num in range(10):
    numero = int(input('Ingrese un numero: '))
    suma = numero + suma

print('el resultado de la suma es ' + str(suma))
