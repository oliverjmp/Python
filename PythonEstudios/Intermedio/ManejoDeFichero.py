# 1. Crea un archivo de texto y escribe en él la frase "Hola desde Python".
print("------Creando y escribiendo en el archivo:--------")
with open("saludo.txt", "w+", encoding="utf-8") as archivo:
    archivo.write("Hola desde Python\n")
    archivo.seek(0)
    print(archivo.read())

# 2. Abre un archivo y lee todo su contenido.
print("\n------Leyendo el contenido del archivo clientes.csv:--------")
with open("clientes.csv", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

# 3. Añade una nueva línea al final del archivo con el texto "Línea añadida".
print("\n------Añadiendo una línea al archivo:--------")
with open("saludo.txt", "a+", encoding="utf-8") as archivo:
    archivo.write("Línea añadida.")
    archivo.seek(0)
    print(archivo.read())

# 4. Lee solo los primeros 10 caracteres del archivo.
print("\n------Leyendo los primeros 10 caracteres del archivo:--------")
with open("saludo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read(10)
    print(contenido)

# 5. Usa seek para volver al inicio del archivo y leer desde ahí.
print("\n------Volviendo al inicio del archivo y leyendo todo:--------")
with open("saludo.txt", "r", encoding="utf-8") as archivo:
    archivo.seek(0)
    contenido = archivo.read()
    print(contenido)

# 6. Lee e imprime el contenido línea por línea usando readline.
print("\n------Leyendo línea por línea:--------")
with open("saludo.txt", "r", encoding="utf-8") as archivo:
    linea = archivo.readline()
    while linea:
        print(linea)
        linea = archivo.readline()

# 7. Lee todas las líneas del archivo en una lista y recórrelas con un bucle.
print("\n------Leyendo todas las líneas en una lista:--------")
with open("saludo.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea)

# 8. Crea un archivo nuevo que sobrescriba si ya existe, y escribe varias lÃ­neas.
print("\n------Creando un nuevo archivo y escribiendo varias líneas:--------")
with open("saludo.txt", "w+", encoding="utf-8") as archivo:
    archivo.write("Soy Oliver Morales.\n")
    archivo.write("tengo 43 años.\n")
    archivo.write("Python es mi lenguaje favorito.\n")
    archivo.seek(0)
    print(archivo.read())


# 9. Usa una función para abrir un archivo, escribir texto y cerrarlo automáticamente con with.
print("\n------Usando una función para manejar el archivo:--------")
def escribir_en_archivo(nombre_archivo, texto):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(texto)
    print(f"✅ Texto escrito en '{nombre_archivo}' correctamente.")

# Uso de la función
escribir_en_archivo("mensaje.txt", "Este es un mensaje escrito desde una función.")


# 10. Lee un archivo línea por línea y muestra solo las que contienen la palabra "Python".
print("\n------Mostrando líneas que contienen 'Python':--------")
def mostrar_lineas_con_python(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if "Python" in linea:
                print(linea.strip())

# Uso de la función
mostrar_lineas_con_python("saludo.txt")