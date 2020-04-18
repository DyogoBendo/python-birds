from unittest import TestCase
from package.modulo import soma


class TestSoma(TestCase):
    def test_soma(self): #sempre usar self ao criar um metodo
        resultado = soma(1, 3)
        self.assertEqual(4, resultado) #verifica se uma coisa é ogual a outra
