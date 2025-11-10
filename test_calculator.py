import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add(self):
        self.assertEqual(self.calc.add(5, 2), 7)
    def test_substract(self):
        self.assertEqual(self.calc.subtract(3,1),2)

    def test_substract(self):
        self.assertEqual(self.calc.subtract(4,1),3)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4,2),8)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5,2),10)

    def test_devide(self):
        self.assertEqual(self.calc.divide(10,5),2)

    def test_devide(self):
        self.assertEqual(self.calc.divide(5,5),1)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10,2),0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10,3),1)

if __name__ == '__main__':
    unittest.main()