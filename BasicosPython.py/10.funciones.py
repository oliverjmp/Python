# 1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting(nombre="desconocido"):
    print("Hola,", nombre)
personalized_greeting("Oliver Morales")

# 2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.
def multiply(a, b):
    return a * b
multiply_result = multiply(5, 10)
print(multiply_result)
# 3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.
def is_even(n):
    return n % 2 == 0
is_even_result = is_even(4)
print(is_even_result)

# 4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.
def convert_to_uppercase(text):
    return text.upper()
convert_to_uppercase_result = convert_to_uppercase("Hola, mundo")
print(convert_to_uppercase_result)

# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos.
def arbitrary_sum(*args):
    return sum(args)
arbitrary_sum_result = arbitrary_sum(1, 2, 3, 4, 5)
print(arbitrary_sum_result)

# 6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
def generate_full_greeting(nombre, apellido):
    return f"Hola, {nombre} {apellido}"
print(generate_full_greeting(nombre="Oliver", apellido="Morales"))

# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.
def power(base, exponente):
    return base ** exponente
power_result = power(2, 3)
print(power_result)

# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.
def calculate_average(a, b, c):
    return (a + b + c) / 3
calculate_average_result = calculate_average(5, 10, 15)
print(calculate_average_result)

# 9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.
def count_characters(text):
    return len(text)
count_characters_result = count_characters("Hola, mundo")
print(count_characters_result)

# 10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*messages):
    for msg in messages:
        print(msg.upper())
display_messages("Hola", "Python", "Funciones")