# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
mi_diccionario = {
    "name": "Oliver",
    "age": 43,
    "country": "Madrid"
}
print("Diccionario original:", mi_diccionario)

# 2. Accede al valor de la clave name en el diccionario.
print("Nombre:", mi_diccionario["name"])

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
mi_diccionario["job"] = "Analista de Datos"
print("Diccionario actualizado:", mi_diccionario)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
mi_diccionario["age"] = 38
print("Diccionario actualizado:", mi_diccionario)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del mi_diccionario["country"]
print("Diccionario después de eliminar 'country':", mi_diccionario)

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
mi_diccionario_cuadrados = {i: i**2 for i in range(1, 6)}
print("Diccionario de cuadrados:", mi_diccionario_cuadrados)

# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
print("¿La clave 'age' está presente?", "age" in mi_diccionario)

# 8. Imprime solo las claves del diccionario.
print("Claves del diccionario:", mi_diccionario.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
print("Lista de claves:", list(mi_diccionario.keys()))

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
nuevas_claves = ["name", "age", "job"]
mi_nuevo_diccionario = dict.fromkeys(nuevas_claves, "Desconocido")
print("Nuevo diccionario:", mi_nuevo_diccionario)