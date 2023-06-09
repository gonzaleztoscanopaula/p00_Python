class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

rectangulo = Rectangulo(5, 3)

print("Datos del rectangulo: ")
print("La altura del rectangulo es: ", rectangulo.altura)
print("La base del rectangulo es: ", rectangulo.base)
print("El area del rectangulo es: ", rectangulo.calcular_area())
print("El perimetro del rectangulo es: ", rectangulo.calcular_perimetro())
