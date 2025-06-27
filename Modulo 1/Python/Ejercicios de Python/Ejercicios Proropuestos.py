#Ejercicio 1

edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#Ejercicio 2
numero = int(input("Ingresa un número entero: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")


#Ejercicio 3
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if num1 > num2:
    print("El primer número es mayor.")
elif num2 > num1:
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")


#Ejercicio 4
año = int(input("Ingresa un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")

#Ejercicio 5
precio_original = float(input("Ingresa el precio original: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))

precio_final = precio_original - (precio_original * descuento / 100)
print(f"El precio final con descuento es: {precio_final}")



#Ejercicio 6
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)

if b != 0:
    print("División:", a / b)
else:
    print("No se puede dividir entre cero.")

#Ejercicio 7
numero = int(input("Ingresa un número dentro del rango de 10 a 50.: "))
if 10 <= numero <= 50:
    print("El número está dentro del rango de 10 a 50.")
else:
    print("El número está fuera del rango.")

#Ejercicio 8
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
ciudad = input("Ingresa tu ciudad de residencia: ")

print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

#Ejercicio 9
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
print("La suma es:", num1 + num2)

#Ejercicio 10
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

print(a > 10 and b > 10)

#Ejercicio 11
x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))
z = int(input("Ingresa el tercer número: "))

if x > y and y > z:
    print("El primer número es mayor que el segundo y el segundo es mayor que el tercero.")
else:
    print("No se cumple la condición.")

#Ejercicio 12
a = True
b = False

print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

#Ejercicio 13
n = int(input("Ingresa un número: "))
if n % 2 == 0 and 20 <= n <= 50:
    print("El número es par y está entre 20 y 50.")
else:
    print("No cumple con ambas condiciones.")

#Ejercicio 14
nota = int(input("Ingresa la calificación (1-100): "))

if 90 <= nota <= 100:
    print("A")
elif 80 <= nota < 90:
    print("B")
elif 70 <= nota < 80:
    print("C")
elif 60 <= nota < 70:
    print("D")
else:
    print("F")


#Ejercicio 15 
n = float(input("Ingresa un número: "))

if n > 0:
    print("El número es positivo.")
elif n < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

