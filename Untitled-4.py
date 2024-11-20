class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def nombre_completo(self):
        print(self.nombre + " " + self.apellido)


class Estudiante(Persona):
    def __init__(self, nom, ape, carr):
        super().__init__(nom, ape)  # Llama al constructor de la clase base
        self.carrera = carr

    def mostrar_carrera(self):
        print(self.carrera)


# Ejemplo de uso
persona = Persona("Juan", "Pérez")
persona.nombre_completo()

estudiante = Estudiante("Ana", "Gómez", "Ingeniería de Software")
estudiante.nombre_completo()
estudiante.mostrar_carrera
