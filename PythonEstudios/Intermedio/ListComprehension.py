# 1. Genera una lista utilizando comprensión con los números del 0 al 10.
lista1 = [x for x in range(11)]
print(lista1)

# 2. Crea una lista utilizando comprensión con los cuadrados de los números del 1 al 10.
lista2 = [x**2 for x in range(1, 11)]
print(lista2)

# 3. Genera una lista utilizando comprensión con los números pares del 0 al 20.
lista3 = [x for x in range(21) if x % 2 == 0]
print(lista3)

# 4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprensión.
temperaturas_celsius = [0, 10, 20, 30, 40]
temperaturas_fahrenheit = [(x * 9/5) + 32 for x in temperaturas_celsius]
print(temperaturas_fahrenheit)

# 5. Crea una lista utilizando comprensión con los caracteres de una cadena.
cadena = "Hola"
caracteres = [x for x in cadena]
print(caracteres)

# 6. Filtra una lista de palabras y deja solo las que tienen más de 4 letras utilizando comprensión.
palabras = ["Hola", "adiós", "bienvenido", "chao"]
palabras_filtradas = [x for x in palabras if len(x) > 4]
print(palabras_filtradas)

# 7. Aumenta en 5 cada número de una lista con comprensión usando una función externa.
def aumentar_en_cinco(x):
    return x + 5

numeros = [1, 2, 3, 4, 5]
numeros_aumentados = [aumentar_en_cinco(x) for x in numeros]
print(numeros_aumentados)

# 8. Crea una lista de booleanos que indique si cada número es mayor que 10 utilizando comprensión.
numeros = [5, 10, 15, 20]
mayores_que_diez = [x > 10 for x in numeros]
print(mayores_que_diez)

# 9. Multiplica solo los números impares por 3 en una lista utilizando comprensión.
lista = [1, 2, 3, 4, 5]
resultado = [x * 3 for x in lista if x % 2 != 0]
print(resultado)
# 10. Usa comprensión de listas anidada para generar una matriz 3x3 con números del 1 al 9.
matriz = [[x for x in range(1, 4)] for y in range(1, 4)]
print(matriz)