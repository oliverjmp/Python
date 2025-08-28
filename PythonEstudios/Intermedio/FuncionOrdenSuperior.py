# 1. Crea una función que reciba una función y un número, y devuelva el resultado de aplicar la función al número.
def aplicar_funcion(funcion, numero):
    return funcion(numero)

resultado = aplicar_funcion(lambda x: x + 100, 23)
print(resultado)  # Salida: 123

# 2. Crea una función que reciba dos números y una función, y devuelva el resultado de sumar los dos números y aplicar la función.
def aplicar_funcion_con_suma(func, num1, num2):
    suma = num1 + num2
    return func(suma)

def triple(x):
    return x * 3

resultado = aplicar_funcion_con_suma(triple, 4, 5)
print(resultado)  # Salida: 27, porque (4 + 5) * 3 = 27


# 3. Crea una función que devuelva otra función que sume un número fijo.
def crear_funcion_suma_fija(valor_fijo):
    def funcion_suma_fija(num):
        return num + valor_fijo
    return funcion_suma_fija
sumar_10 = crear_funcion_suma_fija(10)
print(sumar_10(5))  # Salida: 15

# 4. Usa map() con lambda para multiplicar cada número de una lista por 10.
def multiplicar_por_10(lista):
    return list(map(lambda x: x * 10, lista))

numeros = [1, 2, 3, 4, 5]
resultado = multiplicar_por_10(numeros)
print(resultado)

# 5. Usa filter() con lambda para quedarte solo con los números pares.
def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

numeros = [1, 2, 3, 4, 5, 6]
resultado = filtrar_pares(numeros)
print(resultado)

# 6. Usa reduce() con lambda para obtener la suma total de una lista.
from functools import reduce

def sumar_lista(lista):
    return reduce(lambda x, y: x + y, lista)

numeros = [1, 2, 3, 4, 5]
resultado = sumar_lista(numeros)
print(resultado)

# 7. Escribe una función que devuelva una función que reciba un nombre y devuelva “Hola, ”.
def crear_funcion_saludo(nombre):
    def funcion_saludo():
        return f"Hola, {nombre}"
    return funcion_saludo

print(crear_funcion_saludo("Oliver")()) 

# 8. Crea una función que reciba una lista y una función, y cuente cuántos elementos cumplen con la función.
def contar_cumple(lista, funcion):
    return sum(1 for elemento in lista if funcion(elemento))

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
resultado = contar_cumple(numeros, lambda x: x % 2 == 0)
print(resultado) 

# 9. Crea una función que reciba dos funciones y un número, y las aplique en orden.
def aplicar_funciones_en_orden(func1, func2, num):
    return func2(func1(num))

def duplicar(x):
    return x * 2

def sumar_cinco(x):
    return x + 5

resultado = aplicar_funciones_en_orden(duplicar, sumar_cinco, 3)
print(resultado)  # Salida: 11 → (3 * 2) + 5

# 10. Crea una función que reciba una lista y una función, y aplique esa función a cada elemento usando un bucle (sin map).
def aplicar_funcion_a_lista(lista, funcion):
    resultados = []
    for elemento in lista:
        resultados.append(funcion(elemento))
    return resultados

def elevar_al_cubo(x):
    return x ** 3

numeros = [1, 2, 3, 4]
resultado = aplicar_funcion_a_lista(numeros, elevar_al_cubo)
print(resultado) 