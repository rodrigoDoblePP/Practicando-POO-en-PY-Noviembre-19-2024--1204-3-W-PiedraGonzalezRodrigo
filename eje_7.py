#Desarrollar un programa con tres clases:
#La primera debe ser Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad).
#La segunda llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante).
#Y por último, una llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad,
#edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

class Universidad:
    def __init__(self, Nombre):
        self.Nombre = Nombre

class Carrera:
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print (" ")
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}.")
print (" ")
persona = Estudiante("Harvard")
persona.carrera("Ingeniería mecatrónica")
persona.datos("Mike", 19)
