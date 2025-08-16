# 1. Crea una función que intente dividir dos números proporcionados por el usuario. Usa try-except para capturar cualquier error de división (por ejemplo, división por cero).
def divide_numbers():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: División por cero no permitida.")
    except ValueError:
        print("Error: Entrada no válida. Por favor ingrese números.")
    else:
        print("El resultado de la división es:", result)
divide_numbers()

# 2. Crea una función que tome una cadena e intente convertirla en un número entero. Usa try-except para capturar cualquier error en la conversión.
def convert_to_integer(string):
    try:
        numero = int(string)
        print(f"Conversión exitosa: {numero}")
        return numero
    except ValueError:
        print("Error: No se pudo convertir la cadena a un número entero.")
        return None
convert_to_integer("123")

# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)
            return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None
leer_archivo("archivo_inexistente.txt")
# 4. Crea una funciÃ³n que realice mÃºltiples operaciones (suma, resta, divisiÃ³n, multiplicaciÃ³n) con dos nÃºmeros. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.
def operaciones(a, b):
    try:
        suma = a + b
        resta = a - b
        multiplicacion = a * b
        division = a / b  # Puede lanzar ZeroDivisionError
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None
    except TypeError:
        print("Error: Ambos valores deben ser números.")
        return None
    else:
        print("✅ Operaciones realizadas con éxito:")
        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        print(f"División: {division}")
        return suma, resta, multiplicacion, division
    finally:
        print("🔚 Fin de la ejecución de la función.")
operaciones(10, 5)
# 5. Crea una funciÃ³n que le pida al usuario su edad y lance un ValueError si la entrada no es un nÃºmero entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.
def pedir_edad():
    try:
        edad = input("Introduce tu edad: ")
        edad = int(edad)
        if edad <= 0:
            raise ValueError("La edad debe ser un número entero positivo.")
    except ValueError as e:
        print(f"Error: {e}")
        return None
    else:
        print(f"✅ Edad válida: {edad} años")
        return edad
pedir_edad()
# 6. Crea una funciÃ³n que intente acceder a un elemento de una lista por Ã­ndice. Usa try-except para manejar el caso donde el Ã­ndice estÃ© fuera de rango.
def acceder_elemento(lista, indice):
    try:
        elemento = lista[indice]
        print(f"Elemento en la posición {indice}: {elemento}")
        return elemento
    except IndexError:
        print(f"Error: El índice {indice} está fuera del rango de la lista.")
        return None
acceder_elemento([1, 2, 3], 5)
# 7. Crea una funciÃ³n que use try-except para manejar mÃºltiples excepciones: ZeroDivisionError, ValueError y TypeError.
def operar(val1, val2):
    try:
        resultado = int(val1) / int(val2)
        print(f"Resultado: {resultado}")
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Uno de los valores no es convertible a entero.")
    except TypeError:
        print("Error: Tipo de dato no válido para la operación.")
    return None
operar(10, 2)

# 8. Crea una funciÃ³n que simule una transacciÃ³n. Lanza una excepciÃ³n personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.
# Definimos la excepción personalizada
class InsufficientFundsError(Exception):
    def __init__(self, mensaje="Fondos insuficientes para completar la transacción."):
        super().__init__(mensaje)

# Función que simula una transacción
def retirar_dinero(saldo, cantidad):
    try:
        if cantidad > saldo:
            raise InsufficientFundsError()
        saldo -= cantidad
        print(f"Transacción exitosa. Nuevo saldo: {saldo}")
        return saldo
    except InsufficientFundsError as e:
        print(f"Error: {e}")
        return saldo
retirar_dinero(100, 80)
# 9. Crea una funciÃ³n que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.
def convert_to_integers(string_list):
    int_list = []
    for item in string_list:
        try:
            int_list.append(int(item))
        except ValueError:
            print(f"No se pudo convertir '{item}' a entero.")
    return int_list

# 10. Crea una funciÃ³n que calcule la raÃ­z cuadrada de un nÃºmero. Lanza un ValueError si el nÃºmero es negativo.
import math

def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    resultado = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {resultado}")
    return resultado
raiz_cuadrada(16)