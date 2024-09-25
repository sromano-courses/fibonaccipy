import unittest
from unittest import TestCase
from src.fibonacci import Fibonacci


class TestFibonacci(TestCase):

    def test_value_0_should_return_0(self):
        fibonacci = Fibonacci()
        self.assertEqual(0, fibonacci.calculate(0))

    def test_value_1_should_return_1(self):
        fibonacci = Fibonacci()
        self.assertEqual(1, fibonacci.calculate(1))

    def test_value_10_should_return_55(self):
        fibonacci = Fibonacci()
        self.assertEqual(55, fibonacci.calculate(10))

    def test_value_minus1_should_raise_exception(self):
        fibonacci = Fibonacci()
        self.assertRaises(ValueError, fibonacci.calculate, -1)

    def test_value_93_should_raise_exception(self):
        fibonacci = Fibonacci()
        self.assertRaises(ValueError, fibonacci.calculate, 93)


    def test_approx(self):
        self.assertAlmostEqual(10.44, 10.445, delta=0.01)
