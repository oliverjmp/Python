# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.
print("1.Verificando si el nÃºmero es positivo, negativo o cero.")
number = float(input("Ingrese un número: "))
if number > 0:
    print("El número es positivo.")
elif number < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.
print("2.Verificando si eres mayor de edad.")
age=int(input("Ingrese su edad: "))
if age >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.
print("3.Verificando si la cadena de texto está vacía.")
texto = input("Ingrese un texto: ")
if texto:
    print("La cadena de texto no está vacía.")
else:
    print("La cadena de texto está vacía.")

# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
print("4.Ingrese dos números para compararlos.")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 > num2:
    print("El primer número es mayor.")
elif num1 < num2:
    print("El segundo número es mayor.")
else:
    print("Los números son iguales.")

# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo.
print("5.Verificando si el número es divisible por 3 y por 5.")
num = int(input("Ingrese un número: "))
if num % 3 == 0 and num % 5 == 0:
    print("El número es divisible por 3 y por 5.")
else:
    print("El número no es divisible por 3 y por 5.")

# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.
print("6.Verificando si el número es par o impar.")
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18). Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.
print("7.Verificando si la persona puede votar.")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Puede votar.")
elif edad == 16 or edad == 17:
    print("Puede votar con permiso especial.")
else:
    print("No puede votar.")

# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida. Si no coincide, muestra un mensaje de error.
print("8.Verificando la contraseña.")
contrasena = input("Ingrese la contraseña: ")
if contrasena == "mi_contrasena_secreta":
    print("Contraseña correcta.")
else:
    print("Contraseña incorrecta.")

# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).
print("9.Verificando si el número está entre 10 y 20.")
numero = int(input("Ingrese un número: "))
if 10 <= numero <= 20:
    print("El número está entre 10 y 20.")
else:
    print("El número no está entre 10 y 20.")

# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
print("10.Simulando un semáforo.")
color = input("Ingrese el color del semáforo (rojo, amarillo, verde): ")
if color == "rojo":
    print("Debe detenerse.")
elif color == "amarillo":
    print("Está alerta.")
elif color == "verde":
    print("Puede avanzar.")
else:
    print("Color no válido.")