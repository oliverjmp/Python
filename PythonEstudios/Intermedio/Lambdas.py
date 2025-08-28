# 1. Crea una lambda que sume dos numeros.
suma = lambda x, y: x + y

# 2. Crea una lambda que calcule el cuadrado de un numero.
cuadrado = lambda x: x ** 2

# 3. Crea una lambda que devuelva el mayor de dos numeros.
mayor = lambda x, y: x if x > y else y

# 4. Crea una lambda que sume 10 a un numero dado.
suma_diez = lambda x: x + 10

# 5. Crea una lambda que devuelva el último carácter de una cadena.
ultimo_caracter = lambda s: s[-1] if s else None

# 6. Crea una lambda que indique si una palabra tiene más de 6 letras.
mas_seis = lambda s: len(s) > 6

# 7. Crea una lambda que convierta una cadena a minúsculas.
minusculas = lambda s: s.lower() if s else None

# 8. Crea una lambda que devuelva True si un número es positivo.
positivo = lambda x: x > 0

# 9. Crea una lambda que devuelva "Cadena vacía" si el string está vacío.
cadena_vacia = lambda s: s if s else "Cadena vacía"

# 10. Crea una lambda que calcule el precio final con un impuesto añadido del 21%.
precio_final = lambda p: p * 1.21