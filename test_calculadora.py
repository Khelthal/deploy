import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

	def test_2_mas_2(self):
		self.assertEquals(4, Calculadora.sumar(2, 2))

	def test_10_mas_2(self):
		self.assertEquals(11, Calculadora.sumar(10, 2))

if __name__ == '__main__':
	unittest.main()