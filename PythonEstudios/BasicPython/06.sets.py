# 1. Crea un set con los nÃºmeros del 1 al 5 e imprÃ­melo.
mi_set = {1, 2, 3, 4, 5}
print("Set original:", mi_set)

# 2. AÃ±ade el nÃºmero 6 al set {1, 2, 3, 4, 5} e imprÃ­melo.
mi_set.add(6)
print("Set después de añadir 6:", mi_set)

# 3. Intenta aÃ±adir el nÃºmero 5 al set {1, 2, 3, 4, 5} nuevamente. Â¿QuÃ© sucede?
mi_set.add(5)
print("Set después de intentar añadir 5 nuevamente:", mi_set)

# 4. Verifica si el nÃºmero 3 estÃ¡ en el set {1, 2, 3, 4, 5} e imprime el resultado.
print("¿El número 3 está en el set?", 3 in mi_set)

# 5. Elimina el nÃºmero 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
mi_set.remove(4)
print("Set después de eliminar 4:", mi_set)

# 6. Usa el mÃ©todo clear() para vaciar un set y luego imprime su longitud.
mi_set.clear()
print("Longitud del set después de clear():", len(mi_set))

# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.
mi_set2 = {"manzana", "naranja", "plátano"}
mi_lista = list(mi_set2)
print("Primer elemento de la lista:", mi_lista[0])

# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
mi_set3 = {1, 2, 3}
mi_set4 = {4, 5, 6}
mi_union = mi_set3 | mi_set4
print("Unión de sets:", mi_union)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
mi_set5 = {1, 2, 3, 4}
mi_set6 = {3, 4, 5, 6}
mi_diferencia = mi_set5 - mi_set6
print("Diferencia de sets:", mi_diferencia)

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
del mi_set