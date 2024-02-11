import math


class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solucion_ecuacion_segundo_grado(self):
        discriminante = self.b ** 2 - 4 * self.a * self.c

        if discriminante > 0:
            raiz_discriminante = math.sqrt(discriminante)
            x1 = (-self.b + raiz_discriminante) / (2 * self.a)
            x2 = (-self.b - raiz_discriminante) / (2 * self.a)
            return x1, x2
        elif discriminante == 0:
            x = -self.b / (2 * self.a)
            return x