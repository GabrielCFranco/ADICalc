import unittest
from ADICalc import calculadora

class TestCalculadora(unittest.TestCase):
    def test_1(self):
        self.assertEqual(calculadora(2, 3, '+'), 5)
    
    def test_2(self):
        self.assertEqual(calculadora(-1, -1, '+'), -2)

    def test_3(self):
        self.assertEqual(calculadora(10, 5, '-'), 5)

    def test_4(self):
        self.assertEqual(calculadora(-1, -1, '-'), 0)
    
    def test_5(self):
        self.assertEqual(calculadora(3, 4, '*'), 12)
    
    def test_6(self):
        self.assertEqual(calculadora(-3, 4, '*'), -12)
    
    def test_7(self):
        self.assertEqual(calculadora(10, 2, '/'), 5)
    
    def test_8(self):
        self.assertEqual(calculadora(10, 0, '/'), None)
    
    def test_9(self):
        self.assertEqual(calculadora(2, 3, '^'), 8)
    
    def test_10(self):
        self.assertEqual(calculadora(4, 0.5, '^'), 2.0)

    def test_11(self):
        self.assertEqual(calculadora(-3, 3, '^'), -27)

    def test_12(self):
        self.assertEqual(calculadora('a', 3, '+'), None)
    
    def test_13(self):
        self.assertEqual(calculadora(2, 'b', '*'), None)
    
    def test_14(self):
        self.assertEqual(calculadora(2, 3, '?'), None)
    
    def test_15(self):
        self.assertEqual(calculadora(-5, -5, '+'), -10)
    
    def test_16(self):
        self.assertEqual(calculadora(-5, -5, '*'), 25)
    
    def test_17(self):
        self.assertEqual(calculadora(5.5, 2.2, '+'), 7.7)
    
    def test_18(self):
        self.assertEqual(calculadora(5.5, 2.2, '/'), 2.5)
    
    def test_19(self):
        self.assertEqual(calculadora(-4, 5, '+'), 1)
    
    def test_20(self):
        self.assertEqual(calculadora(1000000, 1000000, '+'), 2000000)

if __name__ == '__main__':
    unittest.main()