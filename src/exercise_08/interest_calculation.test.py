from io import StringIO
from interest_calculation import InterestCalculation
from unittest.mock import patch

import sys
import unittest

class TestInterestCalculation(unittest.TestCase):
  def setUp(self):
    self.interest_calculation = InterestCalculation()

  def test_calculate_final_value(self):
    result = self.interest_calculation.calculate_final_value(1212, 6, 11)
    self.assertEqual(result, 2300.737852702536)

  @patch('builtins.input', side_effect=['3432', '8', '12'])
  def test_calculate_and_display_final_value(self, mock_input):
    captured_output = StringIO()
    sys.stdout = captured_output
    self.interest_calculation.calculate_and_display_final_value()
    sys.stdout = sys.__stdout__
    expected_output = 'The final value of the investment is: 8642.36\n'
    self.assertEqual(captured_output.getvalue(), expected_output)

  @patch('builtins.input', side_effect=['python', '3', '12'])
  def test_calculate_and_display_final_value_invalid_input(self, mock_input):
    captured_output = StringIO()
    sys.stdout = captured_output
    self.interest_calculation.calculate_and_display_final_value()
    sys.stdout = sys.__stdout__
    expected_output = 'Error: Invalid input. Please enter valid values.\n'
    self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
  unittest.main()
