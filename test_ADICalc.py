import unittest
from ADICalc import calculadora

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(calculadora(2, 3, '+'), 5)
        self.assertEqual(calculadora(-1, -1, '+'), -2)
        self.assertEqual(calculadora(2.5, 3.5, '+'), 6)

    def test_subtracao(self):
        self.assertEqual(calculadora(10, 5, '-'), 5)
        self.assertEqual(calculadora(-1, -1, '-'), 0)
        self.assertEqual(calculadora(2.5, 1.5, '-'), 1.0)

    def test_multiplicacao(self):
        self.assertEqual(calculadora(3, 4, '*'), 12)
        self.assertEqual(calculadora(-3, 4, '*'), -12)
        self.assertEqual(calculadora(1.5, 2, '*'), 3.0)

    def test_divisao(self):
        self.assertEqual(calculadora(10, 2, '/'), 5)
        self.assertEqual(calculadora(10, 0, '/'), None)
        self.assertEqual(calculadora(9, 3, '/'), 3.0)

    def test_potenciacao(self):
        self.assertEqual(calculadora(2, 3, '^'), 8)
        self.assertEqual(calculadora(4, 0.5, '^'), 2.0)
        self.assertEqual(calculadora(-3, 3, '^'), -27)

    def test_entrada_invalida(self):
        self.assertEqual(calculadora('a', 3, '+'), None)
        self.assertEqual(calculadora(2, 'b', '*'), None)
        self.assertEqual(calculadora(2, 3, '?'), None)

if __name__ == '__main__':
    unittest.main()
