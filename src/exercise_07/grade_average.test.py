from grade_average import GradeAverage
from io import StringIO
from unittest.mock import patch

import sys
import unittest

class TestGradeCalculator(unittest.TestCase):
  def setUp(self):
    self.grade_calculator = GradeAverage()

  @patch('builtins.input', side_effect=['90', '85', '95'])
  def test_get_and_display_average(self, mock_input):
    captured_output = StringIO()
    sys.stdout = captured_output
    self.grade_calculator.get_and_display_average()
    sys.stdout = sys.__stdout__
    expected_output = 'The average grade is: 90.00\n'
    self.assertEqual(captured_output.getvalue(), expected_output)

  @patch('builtins.input', side_effect=['abc', '85', '95'])
  def test_get_and_display_average_invalid_input(self, mock_input):
    captured_output = StringIO()
    sys.stdout = captured_output
    self.grade_calculator.get_and_display_average()
    sys.stdout = sys.__stdout__
    expected_output = 'Error: Invalid input. Please enter valid grades.\n'
    self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
  unittest.main()
