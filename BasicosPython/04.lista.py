# 1. Crea una lista con los nÃºmeros del 1 al 5 e imprÃ­mela.
myliste=[1,2,3,4,5]
print(myliste)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
print([10, 20, 30, 40, 50][2])  # Imprime el tercer elemento (30) de la lista.

# 3. Agrega el nÃºmero 6 al final de la lista [1, 2, 3, 4, 5] e imprÃ­mela.
myliste.append(6)
print(myliste)

# 4. Inserta el nÃºmero 15 en la posiciÃ³n 2 de la lista [10, 20, 30, 40, 50].
myliste.insert(2, 15)
print(myliste)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
myliste2 = [10, 20, 30, 30, 40, 50]
myliste2.remove(30)
print(myliste2)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.
myliste3 = [1, 2, 3, 4, 5]
ultimo_elemento = myliste3.pop()
print("Último elemento eliminado:", ultimo_elemento)
print(myliste)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.
myliste = [100, 200, 300, 400, 500]
myliste.reverse()
print("Lista invertida:", myliste)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
myliste = [3, 1, 4, 2, 5]
myliste.sort()
print("Lista ordenada:", myliste)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
nueva_lista = [1, 2, 3] + [4, 5, 6]
print("Lista concatenada:", nueva_lista)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
sublista = [10, 20, 30, 40, 50][1:3]
print("Sublista:", sublista)