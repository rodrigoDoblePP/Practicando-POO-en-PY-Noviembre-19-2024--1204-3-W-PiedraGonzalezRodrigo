class Marino:
    def hablar(self):
        print("Hola, soy un animal  marino apunto de exinguirse!")


class Pulpo(Marino):
    def hablar(self):
        print("Hola, soy un pulpo con muchos brazos !")


class Foca(Marino):
    def hablar(self, mensaje):
        print(mensaje)


# Creación de objetos y llamadas
marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola, soy una foca loca !")
