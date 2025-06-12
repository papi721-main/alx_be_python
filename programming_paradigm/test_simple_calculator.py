#!/usr/bin/env python3
import unittest

from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    # Test addition
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_mixed_sign_numbers(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(1.2, 3.4), 4.6)

    # Test subtraction
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-3, -5), 2)

    def test_subtract_mixed_sign_numbers(self):
        self.assertEqual(self.calc.subtract(5, -2), 7)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(7, 0), 7)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # Test multiplication
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(4, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -5), 10)

    def test_multiply_mixed_sign_numbers(self):
        self.assertEqual(self.calc.multiply(-2, 5), -10)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)

    # Test division
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_divide_zero_by_number(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_mixed_sign_numbers(self):
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_divide_floats(self):
        self.assertAlmostEqual(
            self.calc.divide(7.5, 2.5), 3.0  # pyright: ignore
        )


if __name__ == "__main__":
    unittest.main()
