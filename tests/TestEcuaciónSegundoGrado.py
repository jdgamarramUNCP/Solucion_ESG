import unittest

from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado


class TestEcuaciónSegundoGrado (unittest.TestCase):
    def test_raices_reales(self):
        ecuacion = EcuacionSegundoGrado(1, -3, 2)
        self.assertAlmostEqual(2, ecuacion.solucion_ecuacion_segundo_grado()[0], delta=0.001)
        self.assertAlmostEqual(1, ecuacion.solucion_ecuacion_segundo_grado()[1], delta=0.001)

    def test_raiz_real_doble(self):
        ecuacion = EcuacionSegundoGrado(1, -2, 1)
        self.assertAlmostEqual(1, ecuacion.solucion_ecuacion_segundo_grado(), delta=0.001)
