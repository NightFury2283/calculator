import unittest
from main import calculate, format_result


class TestCalc(unittest.TestCase):

    def test_addition_positive(self):
        self.assertEqual(calculate(5, '+', 7), 12)

    def test_subtraction_positive(self):
        self.assertEqual(calculate(15, '-', 4), 11)

    def test_multiplication_positive(self):
        self.assertEqual(calculate(3, '*', 4), 12)

    def test_division_positive(self):
        self.assertEqual(calculate(64, '/', 8), 8)

    def test_division_by_zero(self):
        self.assertEqual(calculate(4, '/', 0), "Ошибка: деление на ноль")

    def test_invalid_operation(self):
        self.assertEqual(calculate(2, '^', 2), "Неизвестная операция")

    def test_non_number_inputs(self):
        self.assertEqual(calculate('a', '+', 3), "Ошибка: аргументы должны быть числами")

    def test_format_normal(self):
        self.assertEqual(format_result(2, '+', 3, 5), "2 + 3 = 5")

    def test_format_error(self):
        self.assertEqual(format_result(6, '/', 0, "Ошибка: деление на ноль"), "Ошибка: деление на ноль")

    def test_addition_negative(self):
        self.assertEqual(calculate(-3, '+', -3), -6)

    def test_subtraction_negative(self):
        self.assertEqual(calculate(-4, '-', -4), 0)

    def test_subtraction_negative_one(self):
        self.assertEqual(calculate(-2, '-', 3), -5)

    def test_multiplication_negative_one(self):
        self.assertEqual(calculate(-2, '*', 2), -4)

    def test_multiplication_negative(self):
        self.assertEqual(calculate(-2, '*', -3), 6)

    def test_division_negative(self):
        self.assertEqual(calculate(-4, '/', -2), 2)

    def test_division_negative_one(self):
        self.assertEqual(calculate(-4, '/', 2), -2)


if __name__ == '__main__':
    unittest.main()
