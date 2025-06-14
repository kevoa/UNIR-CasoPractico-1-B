import pytest
import unittest
from app.calc import Calculator

@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    # Usamos setUp en lugar de setup_method para unittest
    def setUp(self):
        self.calc = Calculator()

    # --- Tests de operaciones básicas exitosas ---
    # Unificamos los tests de suma si son redundantes
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        self.assertEqual(6, self.calc.add(3, 3)) 

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.substract(10, 6))
        self.assertEqual(-2, self.calc.substract(256, 258))
        self.assertEqual(-1, self.calc.substract(-1, 0))
        self.assertEqual(0, self.calc.substract(0, 0))
        # self.assertEqual(0, self.calc.substract(0, 0)) # Esto es una duplicación, se puede eliminar

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(1, 0))
        self.assertEqual(1, self.calc.power(-1, 0))
        self.assertEqual(-27, self.calc.power(-3, 3))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    # --- NUEVOS/MODIFICADOS TESTS PARA COBERTURA 100% ---

    # Test para cubrir la división por cero (ahora espera ZeroDivisionError)
    def test_divide_by_zero_raises_error(self):
        # self.assertRaises(TypeError, self.calc.divide, 2, 0) # Comentado el original
        self.assertRaises(ZeroDivisionError, self.calc.divide, 2, 0) # Espera ZeroDivisionError

    # Test para cubrir la validación de tipos (check_types)
    # Unificamos test_add_method_fails_with_nan_parameter, test_divide_method_fails_with_nan_parameter, etc.
    def test_check_types_raises_type_error(self):
        # Este test cubre check_types para add, pero check_types es el mismo para todos.
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, "0", 0)
        self.assertRaises(TypeError, self.calc.power, "0", 0)
        self.assertRaises(TypeError, self.calc.substract, "0", 0)


# Esto permite ejecutar los tests con 'python -m unittest' o 'pytest'
if __name__ == "__main__":
    unittest.main()


