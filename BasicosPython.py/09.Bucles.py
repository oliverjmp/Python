# 1. Usa un bucle while para imprimir los números del 1 al 10.
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.
for num in [10, 20, 30, 40, 50]:
    print(num)

# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.
suma = 0
i = 1
while i <= 100:
    suma += i
    i += 1
print("La suma de los números del 1 al 100 es:", suma)

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
for letra in "Python":
    print(letra)

# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.
i = 1
while i <= 50:
    if i % 7 == 0:
        print("El primer número divisible por 7 entre 1 y 50 es:", i)
        break
    i += 1

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
for clave in {"name": "Brais", "age": 37, "country": "Galicia"}:
    print(clave)

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.
for i in range(10, 0, -1):
    print(i)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].
contador = 0
for num in [30, 10, 30, 20, 30, 40]:
    if num == 30:
        contador += 1
print("El número 30 aparece", contador, "veces en la lista.")

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
nombres = ["Ana", "Luis", "Oliver", "Marta"]
for nombre in nombres:
    if nombre == "Oliver":
        print("Se encontró el nombre:", nombre)
        break