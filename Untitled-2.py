class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad += 1

# Crear una instancia de Persona
p = Persona(input("Ingrese nombre: "), int(input("Ingrese edad: ")))

# Llamar al método cumpleaños dos veces
p.cumpleaños()
p.cumpleaños()

# Imprimir el resultado
print(f"{p.nombre} cumple {p.edad} años")
