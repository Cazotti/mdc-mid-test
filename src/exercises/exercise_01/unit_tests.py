import unittest

from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
  def test_addition(self):
    calc = SimpleCalculator(5, 3, '+')
    result = calc.calculate()
    self.assertEqual(result, 8, 'Addition test failed')

  def test_subtraction(self):
    calc = SimpleCalculator(10, 4, '-')
    result = calc.calculate()
    self.assertEqual(result, 6, 'Subtraction test failed')

  def test_multiplication(self):
    calc = SimpleCalculator(2, 5, '*')
    result = calc.calculate()
    self.assertEqual(result, 10, 'Multiplication test failed')

  def test_division(self):
    calc = SimpleCalculator(15, 3, '/')
    result = calc.calculate()
    self.assertEqual(result, 5, 'Division test failed')

  def test_division_by_zero(self):
    calc = SimpleCalculator(10, 0, '/')
    with self.assertRaises(Exception) as context:
      calc.calculate()
    self.assertEqual(context.exception.args[0], 'Error: Division by zero is not allowed.', 'Division by zero test failed')

  def test_invalid_operator(self):
    calc = SimpleCalculator(2, 3, '&')
    with self.assertRaises(Exception) as context:
      calc.calculate()
    self.assertEqual(context.exception.args[0], 'Error: Invalid operator.', 'Invalid operator test failed')

if __name__ == '__main__':
  unittest.main()
