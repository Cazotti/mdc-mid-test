import unittest

from factorial import Factorial

class TestFactorialCalculator(unittest.TestCase) :
  def setUp(self) :
    self.factorial_calculator = Factorial()

  def test_calculate_factorial(self) :
    self.assertEqual(self.factorial_calculator.calculate_factorial(0), 1)
    self.assertEqual(self.factorial_calculator.calculate_factorial(1), 1)
    self.assertEqual(self.factorial_calculator.calculate_factorial(10), 3628800)
    self.assertEqual(self.factorial_calculator.calculate_factorial(5), 120)
    self.assertEqual(self.factorial_calculator.calculate_factorial(7), 5040)

  def test_calculate_and_display_positive(self) :
    result = self.factorial_calculator.calculate_and_display(8)
    self.assertEqual(result, 'The factorial of 8 is 40320')

  def test_calculate_and_display_negative(self) :
    result = self.factorial_calculator.calculate_and_display(-9)
    self.assertEqual(result, 'Factorial is not defined for negative numbers.')

  def test_calculate_and_display_invalid_input(self) :
    result = self.factorial_calculator.calculate_and_display('python')
    self.assertEqual(result, 'Error: Invalid input. Please enter a valid number.')

if __name__ == '__main__' :
  unittest.main()
