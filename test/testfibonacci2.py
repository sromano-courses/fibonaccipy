from unittest import TestCase
from src.fibonacci import Fibonacci


class TestFibonacci(TestCase):

    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_value_0_should_return_0(self):
        self.assertEqual(0, self.fibonacci.calculate(0))

    def test_value_1_should_return_1(self):
        self.assertEqual(1, self.fibonacci.calculate(1))

    def test_value_10_should_return_55(self):
        self.assertEqual(55, self.fibonacci.calculate(10))

    def test_value_minus1_should_raise_exception(self):
        self.assertRaises(ValueError, self.fibonacci.calculate, -1)

    def test_value_93_should_raise_exception(self):
        fibonacci = Fibonacci()
        self.assertRaises(ValueError, self.fibonacci.calculate, 93)
