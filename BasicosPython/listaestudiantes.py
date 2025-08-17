# 3. Crea un mÃ³dulo que contenga una lista de nombres de estudiantes y una funciÃ³n que imprima todos los nombres. Importa este mÃ³dulo en otro archivo y usa la funciÃ³n para mostrar la lista.
nombres = ["Ana", "Luis", "Carlos", "María", "Sofía"]

def mostrar_nombres():
    print("Lista de estudiantes:")
    for nombre in nombres:
        print(f"- {nombre}")
        