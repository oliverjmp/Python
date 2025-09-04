# 1. Importa el modulo math y muestra el valor de pi.
print("------Importando y usando paquetes externos:--------")
import math
print("Valor de pi:", math.pi)
# 2. Crea un array de números usando numpy y multiplicalo por 3.
print("\n------Creando un array con numpy y multiplicándolo por 3:--------")    
import numpy as np
array = np.array([1, 2, 3, 4, 5])
array = array * 3
print("Array multiplicado por 3:", array)

# 3. Muestra la versión instalada de numpy.
print("\n------Mostrando la versión de numpy:--------")
print("Versión de numpy:", np.__version__)

# 4. Realiza una petición HTTP con requests a una API pública y muestra el código de estado.
print("\n------Realizando una petición HTTP con requests:--------")
import requests
# URL de una API pública sencilla
url = "https://api.agify.io?name=oliver"

# Realizar la petición GET
respuesta = requests.get(url)

# Mostrar el código de estado HTTP
print("Código de estado:", respuesta.status_code)

    #200: OK, la petición fue exitosa.

    #404: No encontrado.

    #500: Error interno del servidor.

    #403: Prohibido.

    #301: Redirección permanente.

print("Contenido:", respuesta.json())


# 5. Importa una función llamada sum_two_values desde un paquete personalizado mypackage.arithmetics y utilízala.
print("\n------Importando y usando una función desde un paquete personalizado:--------")
from Mypackage.arithmetics import sum_two_values
print("\n------Usando una función desde un paquete personalizado:--------")
resultado = sum_two_values(5, 10)
print("Resultado de la suma:", resultado)

# 6. Usa pandas para crear un DataFrame con nombres en español.
print("\n------Creando un DataFrame con pandas:--------")

import pandas as pd

# Datos en español
datos = {
    "Nombre": ["Lucía", "Carlos", "María", "José", "Ana"],
    "Edad": [28, 34, 25, 40, 31],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"]
}

# Crear el DataFrame
df = pd.DataFrame(datos)

# Mostrar el DataFrame
print(df)


# 7. Ejecuta el comando para instalar el paquete requests desde la terminal.
print("\n------Instalando el paquete requests desde la terminal:--------")


# 8. Usa requests para obtener datos de una API y extrae solo los nombres de los primeros Pokémon.
print("\n------Obteniendo nombres de los primeros Pokémon usando requests:--------")
import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10")
data = response.json()
pokemon_names = [pokemon['name'] for pokemon in data['results']]
print("Nombres de los primeros 10 Pokémon:", pokemon_names)

# 9. Muestra todos los paquetes instalados con pip desde la terminal.
print("\n------Mostrando todos los paquetes instalados con pip desde la terminal:--------")


# 10. Escribe una línea de código que muestre la ayuda sobre el paquete numpy desde Python.
print("\n------Mostrando la ayuda sobre el paquete numpy:--------")
import numpy as np
help(np)