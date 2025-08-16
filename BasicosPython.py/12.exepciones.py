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
        return int(string)
    except ValueError:
        print("Error: No se pudo convertir la cadena a un número entero.")
        return None
convert_to_integer("123")

# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.

# 4. Crea una funciÃ³n que realice mÃºltiples operaciones (suma, resta, divisiÃ³n, multiplicaciÃ³n) con dos nÃºmeros. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.

# 5. Crea una funciÃ³n que le pida al usuario su edad y lance un ValueError si la entrada no es un nÃºmero entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.

# 6. Crea una funciÃ³n que intente acceder a un elemento de una lista por Ã­ndice. Usa try-except para manejar el caso donde el Ã­ndice estÃ© fuera de rango.

# 7. Crea una funciÃ³n que use try-except para manejar mÃºltiples excepciones: ZeroDivisionError, ValueError y TypeError.

# 8. Crea una funciÃ³n que simule una transacciÃ³n. Lanza una excepciÃ³n personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.

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