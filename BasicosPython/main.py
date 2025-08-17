import calculator
import convertermodulo

print("funciones para sumar, restar, multiplicar y dividir")
sumar_result = calculator.sumar(5, 3)
print("Suma:", sumar_result)

restar_result = calculator.restar(5, 3)
print("Resta:", restar_result)

multiplicar_result = calculator.multiplicar(5, 3)
print("Multiplicación:", multiplicar_result)

dividir_result = calculator.dividir(5, 3)
print("División:", dividir_result)

print("Funciones para convertir temperaturas entre Celsius y Fahrenheit")
celsius = 60
fahrenheit = convertermodulo.celsius_to_fahrenheit(celsius)
print("Temperatura en Celsius:", celsius)
print("Temperatura en Fahrenheit:", fahrenheit)

print("Convertir de Fahrenheit a Celsius")
fahrenheit = 70
celsius = convertermodulo.fahrenheit_to_celsius(fahrenheit)
print("Temperatura en Fahrenheit:", fahrenheit)
print("Temperatura en Celsius:", celsius)