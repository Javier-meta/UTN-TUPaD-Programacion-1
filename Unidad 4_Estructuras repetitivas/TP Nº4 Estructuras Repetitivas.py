#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0,101):
    print (i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = input("ingrese un numero entero: ")
cont = 0
for i in num:
    cont += 1
print (f"el numero ingresado contiene {cont} digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num_1 = int(input("ingrese el primer numero: "))
num_2 = int(input("ingrese el segundo numero: "))
sumatoria = 0
if num_1 > num_2:
    for i in range(num_2 + 1,num_1):
        sumatoria += i
else:
    for i in range(num_1 + 1,num_2):
        sumatoria += i
print (f"la suma de los numeros es: {sumatoria}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

sumatoria = 0
while True:
    num = int(input("ingrese el numero: "))
    if num == 0:
        break
    else:
        sumatoria += num
print (f"la suma de los numeros es: {sumatoria}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_aleatorio = random.randint(0,9)
cont = 0
while True:
    print ("!!!Adivina el numero!!!")
    numero = int(input("ingrese el numero (entre 0 y 9): "))
    if numero == numero_aleatorio:
        cont += 1
        break
    else:
        cont += 1
print (f"Acertaste, el numero es {numero}. Numero de intentos: {cont}")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100,-1,-2):
        print (i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

numero = int(input("ingrese un numero entero positivo: "))
sumatoria = 0
for i in range(0,numero + 1):
    sumatoria += i
print (f"la suma de los numeros es: {sumatoria}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cont_pares = 0
cont_impares = 0
cont_negativos = 0
cont_positivos = 0
for i in range(100):
    num = int(input("numero: "))
    if num > 0:
        cont_positivos += 1
    else:
        cont_negativos += 1
    if num % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1
print (f"cantidad de numeros pares: {cont_pares}")
print (f"cantidad de numeros impares: {cont_impares}")
print (f"cantidad de numeros negativos: {cont_negativos}")
print (f"cantidad de numeros positivos: {cont_positivos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

sumatoria = 0
for i in range(1,101):
    num =  int(input("numero: "))
    sumatoria += num
print (f"la media de los numeros es: {sumatoria / i}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("ingrese un numero: ")
cont_digitos = len(numero)
for i in range(-1,-cont_digitos-1,-1):
    print (numero[i],end="")
print ()


















