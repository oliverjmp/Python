# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprÃ­mela.
mi_tupla = (10, 20, 30, 40, 50)
print("Tupla original:", mi_tupla)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muÃ©stralo.
mi_tupla2 = (100, 200, 300, 400, 500)
print("Segundo elemento de la tupla:", mi_tupla2[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
mi_tupla3 = (1, 2, 3)
# mi_tupla3[0] = 10  # Esto generará un error porque las tuplas son inmutables.

# 4. Cuenta cuÃ¡ntas veces aparece el nÃºmero 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
mi_tupla4 = (1, 2, 3, 3, 4, 5, 3)
print("El número 3 aparece", mi_tupla4.count(3), "veces en la tupla.")

# 5. Encuentra el Ã­ndice de la primera apariciÃ³n de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
mi_tupla5 = ("Java", "Python", "JavaScript", "Python")
print("El índice de la primera aparición de 'Python' es:", mi_tupla5.index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
mi_tupla6 = (1, 2, 3) + (4, 5, 6)
print("Tupla concatenada:", mi_tupla6)

# 7. Crea una subtupla con los elementos desde la posiciÃ³n 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
mi_tupla7 = (10, 20, 30, 40, 50)[2:4]
print("Subtupla:", mi_tupla7)

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
mi_tupla8 = ("rojo", "verde", "azul")
mi_lista = list(mi_tupla8)
mi_lista[1] = "amarillo"
mi_tupla8 = tuple(mi_lista)
print("Tupla resultante:", mi_tupla8)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
mi_tupla9 = (1, 2, 3)
del mi_tupla9
# print("Tupla eliminada:", mi_tupla9)  # Esto generará un error porque la tupla ha sido eliminada.
# 10. Crea una tupla con un solo elemento (el nÃºmero 100) e imprÃ­mela. AsegÃºrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
mi_tupla10 = (100,)
print("Tupla con un solo elemento:", mi_tupla10)