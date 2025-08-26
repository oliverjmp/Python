# 1. Crea una variable con la fecha y hora actual.
from datetime import datetime, date, time, timedelta

ahora = datetime.now()
print(ahora)

# 2. Imprime solo el año, mes y día de la fecha actual.
print(ahora.year, ahora.month, ahora.day)

# 3. Crea una fecha específica: 25 de diciembre de 2025 y muéstrala.
navidad = datetime(2025, 12, 25)
print(navidad)

# 4. Muestra solo la hora, los minutos y los segundos de un objeto time.
hora_actual = ahora.time()
print(hora_actual)

# 5. Calcula cuántos días faltan para el 1 de enero del año siguiente.
enero_2026 = datetime(2026, 1, 1)
dias_faltantes = (enero_2026 - ahora).days
print(dias_faltantes)

# 6. Crea una función que reciba una fecha y devuelva su timestamp.
def obtener_timestamp(fecha):
    return fecha.timestamp()

print(obtener_timestamp(ahora))

# 7. Suma 30 días a la fecha actual usando timedelta.
nueva_fecha = ahora + timedelta(days=30)
print(nueva_fecha)

# 8. Crea una fecha y añade 1 mes (consejo: hazlo sumando 30 días como simplificación).
fecha_con_mes = ahora + timedelta(days=30)
print(fecha_con_mes)

# 9. Compara dos fechas y muestra cuál es anterior.
if ahora < navidad:
    print("La fecha actual es anterior a Navidad.")
else:
    print("La fecha actual es posterior a Navidad.")

# 10. Crea una lista con varias fechas y ordénalas cronológicamente.
fechas = [ahora, navidad, enero_2026]
fechas.sort()
print(fechas)