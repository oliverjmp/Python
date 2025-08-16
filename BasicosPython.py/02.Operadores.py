# 1. Realiza las siguientes operaciones aritmÃ©ticas:
# â€¢	Suma: 15 + 25
# â€¢	Resta: 50 - 22
# â€¢	MultiplicaciÃ³n: 8 * 7
# â€¢	DivisiÃ³n: 100 / 20
sum_result = 15 + 25
sub_result = 50 - 22
mul_result = 8 * 7
div_result = 100 / 20
print("Suma:", sum_result)
print("Resta:", sub_result)
print("Multiplicación:", mul_result)
print("División:", div_result)
# 2. Calcula el resto de la divisiÃ³n de 37 entre 5 y almacÃ©nalo en una variable remainder. Luego imprÃ­melo.
remainder = 37 % 5
print("Resto:", remainder)
# 3. Convierte el nÃºmero 7 en una cadena de texto y concatÃ©nalo con la frase â€œ es mi nÃºmero favoritoâ€. Imprime el resultado.
favorite_number = str(7) + " es mi número favorito"
print(favorite_number)
# 4. Repite la palabra â€œPythonâ€ 10 veces usando el operador de multiplicaciÃ³n para cadenas y luego imprÃ­mela.
python_repeated = "Python " * 10
print(python_repeated)
# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.
a = 12
b = 8
resultado = a > b
print("¿Es a mayor que b?", resultado)
# 6. Compara dos cadenas de texto (â€œappleâ€ y â€œbananaâ€) usando los operadores > y < y explica cuÃ¡l tiene mayor orden alfabÃ©tico.
cadena1 = "apple"
cadena2 = "banana"
resultado_cadenas = cadena1 < cadena2
print("¿Es 'apple' menor que 'banana'?", resultado_cadenas)     
# 7. Realiza una comparaciÃ³n lÃ³gica usando and para verificar si el nÃºmero 10 es mayor que 5 y menor que 20. Imprime el resultado.
comparacion_logica = 10 > 5 and 10 < 20
print("¿Es 10 mayor que 5 y menor que 20?", comparacion_logica)
# 8. Usa el operador or para verificar si el nÃºmero 7 es menor que 3 o mayor que 5. Imprime el resultado.
comparacion_or = 7 < 3 or 7 > 5
print("¿Es 7 menor que 3 o mayor que 5?", comparacion_or)
# 9. Aplica el operador not para invertir el resultado de la comparaciÃ³n 15 > 20. Â¿CuÃ¡l es el resultado?
comparacion_not = not (15 > 20)
print("¿Es 15 > 20?", comparacion_not)
# 10. Combina operadores aritmÃ©ticos y lÃ³gicos: Verifica si el nÃºmero resultante de la expresiÃ³n (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
resultado_combinado = (5 * 3) + 2 > 10 and (5 * 3) + 2 < 20
print("¿Es (5 * 3) + 2 mayor que 10 y menor que 20?", resultado_combinado)