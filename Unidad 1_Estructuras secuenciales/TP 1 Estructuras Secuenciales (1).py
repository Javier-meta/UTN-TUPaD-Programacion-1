#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.#

print ("hola mundo!\n")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.#

nombre = input("ingrese su nombre: ")
print (f"Hola {nombre}!\n")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados.

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = int(input("ingrese su edad: "))
residencia = input("ingrese su residencia: ")
print (f"Hola, soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = float(input("ingrese el radio del circulo: "))
area = 3.14 * (radio**2)
perimetro = 2 * 3.14 * radio
print (f"el area es: {area}")
print (f"el perimetro es: {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = int(input("ingrese los segundos: "))
horas = segundos / 3600
print (f"los segundos ingresados equivalen a {horas} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("ingrese un numero: "))
for i in range(11):
    print (f"{numero} x {i} = {numero * i}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))
print (f"la suma es: {num1 + num2}")
print (f"la division es: {num1 / num2}")
print (f"el producto es: {num1 * num2}")
print (f"la resta es: {num1 - num2}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal.

altura = float(input("ingrese su altura: "))
peso = float(input("ingrese su peso (en kg): "))
imc = peso / (altura**2)
print (f"su indice de masa corporal es de: {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit.

celsius = float(input("ingrese la temperatura en grados celsius: "))
fahrenheit = (9/5) * celsius + 32
print (f"la temperatura en grados fahrenheit es de: {fahrenheit}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números

a = int(input("numero: "))
b = int(input("numero: "))
c = int(input("numero: "))
promedio = (a + b + c) / 3
print (f"el promedio es: {promedio}") 