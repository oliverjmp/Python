# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print("Longitud de la cadena:", len(text))

# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.
greeting = "Hola"
language = "Python"
print("Cadena concatenada:", greeting + " " + language)

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
multiline_text = "Esta es una línea.\nY esta es otra línea."
print("Texto con salto de línea:\n", multiline_text)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name = "Oliver"
last_name = "Morales"
age = 43
print(f"Mi nombre es {name} {last_name} y tengo {age} años.")

# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.
char1, char2, char3, char4, char5, char6 = "Python"
print("Desempaquetando 'Python':")
print(char1)
print(char2)
print(char3)
print(char4)
print(char5)
print(char6)

# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
programacion = "Programación"
slice_programacion = programacion[3:8]
print("Slice de 'Programación':", slice_programacion)

# 7. Invierte la cadena “Python” usando slicing y muestra el resultado.
python = "Python"
python_invertido = python[::-1]
print("Cadena 'Python' invertida:", python_invertido)

# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
cadena_minusculas = "aprendiendo python"
cadena_mayusculas = cadena_minusculas.upper()
print("Cadena en mayúsculas:", cadena_mayusculas)

# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
programacion_en_python = "Programación en Python"
contador_n = programacion_en_python.count("n")
print("La letra 'n' aparece", contador_n, "veces.")

# 10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
cadena_numerica = "12345"
es_numerica = cadena_numerica.isdigit()
print("¿La cadena '12345' es numérica?", es_numerica)