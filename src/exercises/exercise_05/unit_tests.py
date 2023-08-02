from io import StringIO
from table import Table
from unittest.mock import patch

import sys
import unittest

class TestTable(unittest.TestCase):
  def setUp(self):
    self.table = Table()

  def test_display_multiplication_table(self):
    captured_output = StringIO()
    sys.stdout = captured_output
    self.table.display_multiplication_table(5)
    sys.stdout = sys.__stdout__
    expected_output = "Multiplication table of 5:\n5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50\n"
    self.assertEqual(captured_output.getvalue(), expected_output)

  @patch('builtins.input', side_effect=["5"])
  def test_generate_and_display_table(self, mock_input):
    captured_output = StringIO()
    sys.stdout = captured_output
    self.table.generate_and_display_table(5)
    sys.stdout = sys.__stdout__
    expected_output = "Multiplication table of 5:\n5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50\n"
    self.assertEqual(captured_output.getvalue(), expected_output)

  @patch('builtins.input', side_effect=["abc"])
  def test_generate_and_display_table_invalid_input(self, mock_input):
    captured_output = StringIO()
    sys.stdout = captured_output
    self.table.generate_and_display_table("abc")
    sys.stdout = sys.__stdout__
    expected_output = "Error: Invalid input. Please enter a valid number.\n"
    self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
  unittest.main()
