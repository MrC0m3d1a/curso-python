print('Ingrese el primer numero: ')
num1 = int(input())
print('Ingrese el segundo numero: ')
num2 = int(input())
residuo = num1 % num2

if num1 == 0:
    print('No se puede dividir por 0')
else:
    if 0 == residuo:
        print('la division es exacta ')
    else:
        print('La division no es exacta ')  
