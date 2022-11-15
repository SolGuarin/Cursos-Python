
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando en bicicleta')


if __name__ == '__main__':
    persona1 = Persona('Soleny')
    persona1.avanza()

    persona2 = Ciclista('David')
    persona2.avanza()
