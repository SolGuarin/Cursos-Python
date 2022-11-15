
class Rectangulo:
    # Método constructor
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Método para calcular el área
    def area(self):
        return self.base * self.altura

# Cuadrado hereda de Rectángulo
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == '__main__':
    # Creamos un objeto de la clase Rectangulo
    rectangulo = Rectangulo(base=3, altura=4)
    print(f'El área del rectángulo es: {rectangulo.area()}')

    # Creo un objeto de la clase cuadrado y hereda el área de la clase Rectángulo
    cuadrado = Cuadrado(lado=5)
    print(f'El área del cuadrado es: {cuadrado.area()}')



