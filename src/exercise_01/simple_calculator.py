'''
Exercise 01: Simple Calculator

Create a calculator that takes two numbers and an operator (+, -, *, /) and
returns the result of the operation.
'''

class SimpleCalculator:
  def __init__(self, num1, num2, operator):
    self.num1 = num1
    self.num2 = num2
    self.operator = operator

  def calculate(self):
    operators = {
      '+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y if y != 0 else None
    }

    if self.operator in operators:
      result = operators[self.operator](self.num1, self.num2)
      if result is None:
        raise Exception('Error: Division by zero is not allowed.')
      return result
    else:
      raise Exception('Error: Invalid operator.')

def main():
  try:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    operator = input('Enter the operator (+, -, *, /): ')

    calc = SimpleCalculator(num1, num2, operator)
    print('Result:', calc.calculate())
  except ValueError as err :
    print('Error: Invalid input. Please enter valid numbers.')
  except Exception as err :
    print(err.args[0])
