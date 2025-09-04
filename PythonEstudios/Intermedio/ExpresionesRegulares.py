import re
# 1. Busca si una cadena empieza por "Hola".
print("------¿La cadena empieza por 'Hola'?--------")
cadena1 = "Hola, ¿cómo estás?"
resultado1 = re.match(r"Hola", cadena1)
print("¿La cadena empieza con 'Hola'? :", bool(resultado1))

# 2. Busca la palabra "Python" en una cadena aunque esté en minúsculas.
print("\n------¿Se encontró 'Python' en la cadena?--------")
cadena2 = "Me encanta programar en python."
resultado2 = re.search(r"python", cadena2, re.IGNORECASE)
print("¿Se encontró 'Python' en la cadena? :", bool(resultado2))

# 3. Encuentra todas las apariciones de la palabra "curso" en una cadena.
print("\n------¿Cuántas veces se encontró 'curso' en la cadena?--------")
cadena3 = "Este curso es muy interesante. He aprendido mucho en este curso."
resultado3 = re.findall(r"curso", cadena3)
print("¿Cuántas veces se encontró 'curso' en la cadena? :", len(resultado3))

# 4. Reemplaza todas las apariciones de "lección" por "LECCIÓN".
print("\n------Reemplazando 'lección' por 'LECCIÓN':--------")
cadena4 = "Esta lección es muy importante. He aprendido mucho en esta lección."
resultado4 = re.sub(r"lección", "LECCIÓN", cadena4)
print("Texto original:", cadena4)
print("Texto modificado:", resultado4)

# 5. Divide un texto en partes separadas por comas.
print("\n------Dividiendo el texto en partes por comas:--------")
cadena5 = "manzana,banana,kiwi"
resultado5 = re.split(r",", cadena5)
print("Texto original:", cadena5)
print("Texto dividido:", resultado5)

# 6. Busca la primera palabra que comience con "A" o "a".
print("\n------Buscando la primera palabra que comience con 'A' o 'a':--------")
cadena6 = "Aprender Python es divertido."
resultado6 = re.search(r"\b[Aa]\w*", cadena6)
print("Primera palabra que comienza con 'A' o 'a':", resultado6.group() if resultado6 else "No se encontró.")

# 7. Encuentra todas las palabras en una cadena que terminen en "ción".
print("\n------Buscando palabras que terminen en 'ción':--------")
cadena7 = "La lección fue interesante y la discusión fue profunda."
resultado7 = re.findall(r"\b\w*ción\b", cadena7)
print("Palabras que terminan en 'ción':", resultado7)

# 8. Verifica si una cadena contiene solo números.
print("\n------Verificando si la cadena contiene solo números:--------")
cadena8 = "123456"
resultado8 = re.fullmatch(r"\d+", cadena8)
print("¿La cadena contiene solo números?", bool(resultado8))

# 9. Reemplaza todos los números de una cadena por el texto "[número]".
print("\n------Reemplazando números por '[número]':--------")
cadena9 = "Tengo 2 manzanas y 3 plátanos."
resultado9 = re.sub(r"\d+", "número", cadena9)
print("Texto original:", cadena9)
print("Texto modificado:", resultado9)

# 10. Encuentra todas las palabras de 4 letras exactas en una cadena.
print("\n------Buscando palabras de 4 letras en la cadena:--------")
cadena10 = "Este es un texto de prueba, pero solo algunas palabras tienen cuatro letras."
resultado10 = re.findall(r"\b\w{4}\b", cadena10)
print("Palabras de 4 letras:", resultado10)