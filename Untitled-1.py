#Realizar un programa que conste de una clase llamada Estudiante, 
#que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos,
#imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.



class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre} \nNota: {self.nota}")

    def resultados(self):
        if self.nota >= 7:
            print("Has APROBADO felicidades miky ahora puedes descansar!")
        else:
            print("Has REPROBADO oh cielos viejo suerte para la proxima!")


estudiante1 = Estudiante("jose gutierrez ", 4)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("Rodrigo Piedra el mas guapo ", 10)
estudiante2.imprimir()
estudiante2.resultados()
