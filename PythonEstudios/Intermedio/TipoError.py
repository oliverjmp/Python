# 1. Genera un SyntaxError al imprimir una cadena sin paréntesis.

#print "Hola, mundo" # Descomentan para error

# 2. Genera un NameError intentando usar una variable no definida.
variable_no_definida = 10  # Comentar para error
print(variable_no_definida)

# 3. Genera un IndexError accediendo a un índice inexistente de una lista.
mi_lista = [1, 2, 3]
#print(mi_lista[5]) #Descomentan para error
print(mi_lista[2])

# 4. Genera un ModuleNotFoundError al importar un módulo inexistente.
#import unicorn_rainbows #Descomentan para error
import pandas as pd  

# 5. Genera un AttributeError accediendo a un atributo que no existe.
texto = "Hola, mundo"
#print(texto.no_existe) #Descomentan para error
print(texto.upper())

# 6. Genera un KeyError al acceder a una clave inexistente de un diccionario.

mi_diccionario = {"nombre": "Oliver", "edad": 30}
# print(mi_diccionario["profesion"]) #Descomentan para error
print(mi_diccionario["nombre"])

# 7. Genera un TypeError usando tipos incorrectos (índice string en lista).
mi_lista = [1, 2, 3]
#print(mi_lista["0"]) #Descomentan para error
print(mi_lista[0])

# 8. Genera un ImportError al importar una función que no existe desde un módulo.
#import unicorn_rainbows  # Descomentan para error

# 9. Genera un ValueError intentando convertir un string no numérico a entero.
entrada = "manzana"
try:
    numero = int(entrada)
except ValueError:
    print(f"No se puede convertir '{entrada}' a entero, ValueError")
    
# 10. Intenta detectar si un error ocurre usando try-except con un KeyError.
mi_diccionario = {"clave": "valor"}
try:
    print(mi_diccionario["clave_inexistente"])
except KeyError:
    print("Se produjo un KeyError")