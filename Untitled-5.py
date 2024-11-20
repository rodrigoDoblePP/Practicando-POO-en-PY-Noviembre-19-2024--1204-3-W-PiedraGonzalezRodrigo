class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio


class Moto(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(
            self._llantas, self._color, self._precio))


class Carro(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(
            self._llantas, self._color, self._precio))


# Creación de objetos y llamadas
print("OBJETO = motoneta ")
moto = Moto(2, "rojo pacion ", "$500")
moto.cantidad()

print("\nOBJETO = mustang")
carro = Carro(4, "Negro con amarillo ", "$800")
carro.cantidad()
