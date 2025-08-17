# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un mÃ©todo "make_sound" que imprima un sonido genÃ©rico.
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("El sonido del animal es genérico.")
print("Animal creado:", Animal("Perro").species)

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacÃ©nala en una propiedad pÃºblica. AÃ±ade el mÃ©todo "make_sound" que imprima un sonido dependiendo de la especie.
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        if self.species == "perro":
            print("Guau!")
        elif self.species == "gato":
            print("Miau!")
        else:
            print("El sonido del animal es genérico.")
print("Animal creado:", Animal("Gato").species)

# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas "brand" y "model". AdemÃ¡s, debe tener una propiedad privada "_speed" que inicialmente serÃ¡ 0.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0

    def accelerate(self):
        self._speed += 10

    def brake(self):
        self._speed -= 10
        if self._speed < 0:
            self._speed = 0
print("Coche creado:", Car("Toyota", "Corolla").brand, Car("Toyota", "Corolla").model)

# 5. Crea una clase "Book" que tenga propiedades como "title" (pÃºblico) y "author" (privado). AÃ±ade un mÃ©todo para obtener el autor y otro para cambiar el tÃ­tulo del libro.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.title = title
print("Libro creado:", Book("1984", "George Orwell").title, Book("1984", "George Orwell").get_author()) 

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. AÃ±ade un mÃ©todo para calcular y devolver la nota media del estudiante.
class Estudiante:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
print("Estudiante creado:", Estudiante("Oliver", "Morales").nombre, Estudiante("Oliver", "Morales").apellido)

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". AÃ±ade mÃ©todos para depositar y retirar dinero, asegurÃ¡ndote de que no se pueda retirar mÃ¡s de lo que hay en la cuenta.
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Fondos insuficientes.")
        else:
            self.balance -= amount
print("Cuenta creada:", BankAccount("Oliver Morales", 1000).owner)

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". AÃ±ade un mÃ©todo que calcule la distancia entre dos puntos.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
print("Punto creado:", Point(3, 4).x, Point(3, 4).y)

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". AÃ±ade un mÃ©todo que calcule el pago total basado en las horas trabajadas y el salario por hora.
class Employee:
    def __init__(self, name, hourly_wage):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = 0

    def add_hours(self, hours):
        self.hours_worked += hours

    def calculate_pay(self):
        return self.hourly_wage * self.hours_worked
print("Empleado creado:", Employee("Oliver Morales", 20).name)

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). AÃ±ade un mÃ©todo para agregar un producto al inventario y otro para mostrar todos los productos disponibles.
class Store:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def show_products(self):
        for product in self.inventory:
            print(product)
store = Store()
store.add_product("Producto 1")
print("Tienda creada:", store.show_products())