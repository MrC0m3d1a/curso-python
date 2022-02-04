 # 2) Requerir al usuario que ingrese un número entero positivo e imprimir 
   # todos los números entre el ingresado por el usuario y uno menos 
   # del doble del mismo.

num_int = int(input('Ingrese un numero entero positivo: '))
num2 = num_int + num_int

for numero in range(num_int, num2):
    print(numero)
