class Calculadora:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def suma(self):
        resultado = self._num1 + self._num2
        print(f"El resultado de la suma es: {self._num1} + {self._num2} = {resultado}")

    def resta(self):
        resultado = self._num1 - self._num2
        print(f"El resultado de la resta es: {self._num1} - {self._num2} = {resultado}")

    def division(self):
        if self._num2 != 0:  # Manejo de división entre cero
            resultado = self._num1 / self._num2
            print(f"El resultado de la división es: {self._num1} / {self._num2} = {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")

    def multiplicacion(self):
        resultado = self._num1 * self._num2
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")

# Ejecución de operaciones
operacion = Calculadora(35, 14)
operacion.suma()

operacion = Calculadora(25, 39)
operacion.resta()

operacion = Calculadora(40, 3)
operacion.division()

operacion = Calculadora(123, 4)
operacion.multiplicacion()
